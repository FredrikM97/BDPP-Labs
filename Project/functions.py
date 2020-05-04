from pyspark.sql.functions import when, count, col, isnan, countDistinct,from_unixtime,from_utc_timestamp, unix_timestamp,split, to_timestamp, hour, month, lit,collect_list
import seaborn as sns 
import matplotlib.pyplot as plt 
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.ml.tuning import CrossValidator
from numpy import argmax # TODO replace with something else

def createDirectory(folder):
    """
    Creates empty folder if it does not exist
    
    Parameters
    ----------
    folder: string
        Path to folder
    Return
    ----------
    """
    import os
    os.makedirs(os.path.dirname(folder))

def write2file(file,title,info):
    """
    Write data to filelog
    
    Parameters
    ----------
    file: string
        Path to file
    title: string
        Title for info
    info: string
        Data that shall be stored
    
    Return
    ----------
    """
    f = open(file, "a")
    f.write(f"\n\n# {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n__{title}:__\n{info}")
    f.close()
    
def setup_spark(file):
    """
    Setup spark config and server and load datafile
    
    Parameters
    ----------
    file: string
        File to be loaded
    
    Return
    ----------
    """
    try:
        spark.close()
    except: 
        pass

    try:
        conf = SparkConf().setAppName('Spark Project')
        conf.set('executor-memory','6')
        conf.set('spark.driver.memory', '8g')
        conf.set('spark.executor.cores', '4')
        conf.set("spark.num.executors","6")
        conf.set('spark.memory.fraction','.6')
        conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        conf.set("spark.kryoserializer.buffer.max", "10")

        sc = SparkContext(conf=conf)
        
        spark = SparkSession.builder \
        .appName("Spark Project") \
        .master("local[*]") \
        .config("spark.driver.host", "localhost") \
        .config('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener') \
        .config('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar') \
        .config('SPARKMONITOR_UI_HOST','192.168.1.228')\
        .getOrCreate()
        spark.sparkContext.setLogLevel("WARN")
        
    except Exception as e:
        print(e)
        sc = spark.SparkContext
    # spark.num.executors is set since we dont have enough ram for 8 
    # Note: 6 running processes each having 2gb => 12 gb ram used
    

    
    
            
    df = spark.read.load(file,format="csv", sep=",", inferSchema="true", header="true")
    return df, sc, spark

def printSparkConf(sc, logs_dir):
    """
    Print spark config
    
    Parameters
    ----------
    sc: SparkContext object
        SparkContext object
    logs_dir: string
        Directory for log file
    Return
    ----------
    """
    tmp = sc._conf.getAll()
    write2file(logs_dir,"New Spark session", str(tmp))
    print("Config:",tmp)
    
def setup_variables(df, sc, colLabel, colRem, logs_dir):
    """
    Creates the column items for category and numerical values.
    
    Parameters
    ----------
    df: Dataframe
        Spark Dataframe
    sc: SparkContext object
        SparkContext object
    colLabel: List
        Items that considered Label
    colRem: List
        Items that should be removed before analysis
    logs_dir: string
        Directory for log file
    Return
    ----------
    df: Dataframe
        Spark Dataframe
    colCat: List
        Items that is considered categories
    colNum: List
        Items that is considered numerical values
    """
    # Dropping data that cant help during model
    df = df.drop(*colRem)

    # Convert boolean to string since PCA cant handle boolean which should be a class
    df = df.select(*[col(c[0]).cast("string").alias(c[0]) if c[1] == 'boolean' else col(c[0]).alias(c[0]) for c in df.dtypes])

    #renamedHousing.select([count(when(col(c).isNull(), c)).alias(c) for c in colNum]).show()
    colCat, colNum = createNewClasses(df, sc, colLabel, logs_dir)

    return df, colCat, colNum

def createNewClasses(df, sc, colLabel, logs_dir):
    """
    Divide the data into classes
    
    Parameters
    ----------
    df: Dataframe
        Spark Dataframe
    sc: SparkContext object
        SparkContext object
    colLabel: List
        Items that considered Label
        
    logs_dir: string
        Directory for log file
        
    Return
    ----------
    colCat: List
        Items that is considered categories
    colNum: List
        Items that is considered numerical values
    """
    rdd = sc.parallelize(df.dtypes)
    colCat = rdd.map(lambda i: i[0] if (i[1]=='string' or i[1]=='boolean' and i[0] not in colLabel) else None).filter(lambda i: i != None).collect()
    colNum = rdd.map(lambda i: i[0] if (i[1]=='double' and i[0] not in colLabel) else None).filter(lambda i: i != None).collect()
    
    write2file(logs_dir,"Categorical groups","Defined Label:\n" + str(colLabel) + "\nDefined Categories:\n" + str(colCat) + "\nDefined Numerical:\n" +str(colNum))
    
    print(f"Label: {colCat} \nCategories: {colCat}\nNumerical: {colNum}")
    return colCat, colNum 

def printMissingValues(df, logs_dir):
    """
    Print missing values in Dataframe
    
    Parameters
    ----------
    df: Dataframe
        Spark Dataframe
    logs_dir: string
        Directory for log file
        
    Return
    ----------
    """
    # Check data
    df_missingVals_cols = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])

    # Missing value in each column
    tmp = df_missingVals_cols.collect()
    write2file(logs_dir,"Missing values", str(tmp))
    print("Missing values" + str(tmp))
    
def printCategoricalValues(df, colCat, logs_dir):
    """
    Print the count of unique values from categories
    
    Parameters
    ----------
    df: Dataframe
        Spark Dataframe
    colCat: List
        Items that is considered categories
    logs_dir: string
        Directory for log file
        
    Return
    ----------
    """
    # Checking how many classes that can be used
    tmp = [df.select(countDistinct(c).alias(c)).collect()[0] for c in colCat] 
    print("Unique column values:", tmp)

    write2file(logs_dir,"Categorical values", str(tmp))
    
def write2fileModel(model, models_dir, model_name, timeSignature):
    """
    Write the model to filesystem
    
    Parameters
    ----------
    model: obj
        Model object
    
    models_dir:
        Directory for the model
    
    model_name: string
        Name of the model
    
    timeSignature: string
        Time when program started
        
    Return
    ----------
    """
    print(f"Saving into: {models_dir}/{timeSignature}/{model_name}")
    try:
        model.write.format('parquet').mode('overwrite').option("header", "true").save(f"{models_dir}/{timeSignature}/{model_name}")
        print("Saving through format 1")
    except Exception as e:
        model.write().overwrite().save(f"{models_dir}/{timeSignature}/{model_name}")
        print("Saving through format 2")

def evaluateModel(estimator, 
                  paramGrid, 
                  modelType, 
                  trainSet, 
                  testSet, 
                  timeSignature,
                  evaluator, 
                  k=10,
                  seed=None,
                  logs_dir=None,
                  models_dir=None):
    """
    Evaluate model through CrossValidator, save model, and check accuracy
    
    Parameters
    ----------
    estimator: Obj
        Algorithm used for fitting model
    paramGrid: paramGrid
        Params that will be tested and evaluated
    modelType: string
        Name of the model
    trainSet: Dataframe
        Training set
    testSet: Dataframe
        Test set
    timeSignature: string
        Time when program started
    evaluator: Obj, Optional, Default: MulticlassClassificationEvaluator
        Evaluator
    k: int
        Number of folds
    seed:
        Seed
    logs_dir: string
        Directory for log file
    models_dir:
        Directory for the model
    Return
    ----------
    model: Obj
        Model that is fitted
    predictions: obj
        Predictions that is transformed based on the model and testSet
    """
    cv =  CrossValidator(estimator=estimator, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=k, seed=seed) 
    
    print("Fitting model..")
    write2file(logs_dir,"Fitting "+str(modelType)+" model..","")
    
    model = cv.fit(trainSet)
    
    print("Predicting on testSet..")
    write2file(logs_dir,"Predicting "+str(modelType)+" on testSet..","")
    
    predictions = model.transform(testSet)
    samplePredict = predictions.select("prediction", "label", "features")
    
    print("Evaluating predictions..")
    write2file(logs_dir,"Evaluating "+ str(modelType) +" predictions..","")
    
    accuracy = evaluator.evaluate(predictions)
    params = model.getEstimatorParamMaps()[ argmax(model.avgMetrics)]
    
    write2file(logs_dir,"Evaluating "+ str(modelType),"Display 5 datapoints:\n" + str(samplePredict.take(5)) + "\nAccuracy: " + str(accuracy)+"\nParameters:\n" + str(params))
    write2fileModel(model, models_dir, str(modelType), timeSignature)
    samplePredict.show(5)
    print("Accuracy: ",accuracy, "\nParameters\n",params)
    
    return model, predictions