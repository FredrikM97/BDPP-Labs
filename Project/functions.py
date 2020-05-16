from pyspark.sql.functions import when, count, col, isnan, countDistinct,from_unixtime,from_utc_timestamp, unix_timestamp,split, to_timestamp, hour, month, lit,collect_list, max
from pyspark.mllib.evaluation import MulticlassMetrics
import seaborn as sns 
import matplotlib.pyplot as plt 
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.ml.tuning import CrossValidator
from datetime import datetime
from numpy import argmax

class logging():
    def __init__(self, models_dir, logs_dir, image_dir, foldername, enabled=False):
        self.timeSignature = str(datetime.now().strftime("%Y%m%d%H%M%S"))
        foldername = foldername + "_" +self.timeSignature
        self.models_dir = models_dir + "/" +foldername +"/" 
        self.logs_dir = logs_dir + "/" +foldername + "/logs.md" 
        self.image_dir = image_dir +"/" + foldername +"/" 
        
        self.enabled = enabled
        
        self.createDirectory(self.logs_dir)
        
    
    def createDirectory(self,folder):
        """
        Creates empty folder if it does not exist

        Parameters
        ----------
        folder: string
            Path to folder
        Return
        ----------
        """
        if self.enabled==False: return None
        import os
        os.makedirs(os.path.dirname(folder))
        
        
    def write2file(self, title, info, logs_dir=None):
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
        
        if self.enabled==False: return None
        if logs_dir == None: logs_dir = self.logs_dir
            
        f = open(logs_dir, "a")
        f.write(f"\n\n# {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n__{title}:__\n{info}")
        f.close()
        
    def saveImage(self, image, name, image_dir=None):
        """
        Save file to disk
        Parameters
        ----------
        image: obj
            Image object
        name: string
            Name of file
        image_dir: string, Optional, Default=None
            Alternative path to file

        Return
        ----------
        """
        if self.enabled==False: return None
        if image_dir == None: image_dir = self.image_dir
        try:
            image.figure.savefig(image_dir +"/" + name)
        except:
            image.savefig(image_dir +"/" + name)
            
    def write2fileModel(self, model, model_name, models_dir=None):
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
        if self.enabled==False: return None
        if models_dir == None: models_dir = self.models_dir
            
        print(f"Saving into: {models_dir}{model_name}")
        try:
            model.write.format('parquet').mode('overwrite').option("header", "true").save(f"{models_dir}/{model_name}")
            print("Saving through format 1")
        except Exception as e:
            print(e)
            model.write().overwrite().save(f"{models_dir}/{model_name}")
            print("Saving through format 2")
           
    def setLogDir(self, logs_dir):
        self.logs_dir = logs_dir
    
    def setModelsDir(self, models_dir):
        self.models_dir = models_dir

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
        conf.set('spark.driver.memory', '4g')
        conf.set('spark.executor.memory', '4g')
        conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        conf.set("spark.kryoserializer.buffer.max", "15")
        conf.set('spark.ui.enabled', 'true')
        conf.set('spark.ui.killEnabled', 'false')
        conf.set('spark.serializer.objectStreamReset', '100')
        conf.set('spark.driver.cores', '1')
        conf.set('spark.executor.id', 'driver')
        conf.set('spark.executor.cores', '1')
        conf.set('spark.ui.showConsoleProgress', 'true')
        conf.set('spark.executor.instances', '1')
        conf.set('spark.rdd.compress', 'True')
        sc = SparkContext(conf=conf)
        
        spark = SparkSession.builder \
        .appName("Spark Project") \
        .master("local[*]") \
        .getOrCreate()
        spark.sparkContext.setLogLevel("WARN")
        
    except Exception as e:
        print(e)

    df = spark.read.load(file,format="csv", sep=",", inferSchema="true", header="true")
    return df, sc, spark

def setup_variables(df, sc, colLabel, colRem):
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
    colCat, colNum = createNewClasses(df, sc, colLabel)

    return df, colCat, colNum

def createNewClasses(df, sc, colLabel):
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
    
    print(f"Label: {colLabel} \nCategories: {colCat}\nNumerical: {colNum}")
    return colCat, colNum 

def printMissingValues(df, logger):
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
    logger.write2file("Missing values", str(tmp))
    print("Missing values" + str(tmp))
    
def printCategoricalValues(df, colCat, logger):
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

    logger.write2file("Categorical values", str(tmp))

def evaluateModel(estimator, 
                  paramGrid, 
                  modelType, 
                  trainSet, 
                  testSet, 
                  evaluator, 
                  k=10,
                  seed=None,
                  logger=None):
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
    logger.write2file("Fitting "+str(modelType)+" model..","")
    
    model = cv.fit(trainSet)
    
    print("Predicting on testSet..")
    logger.write2file("Predicting "+str(modelType)+" on testSet..","")
    
    predictions = model.transform(testSet)
    samplePredict = predictions.select("prediction", "label", "features")
    
    print("Evaluating predictions..")
    logger.write2file("Evaluating "+ str(modelType) +" predictions..","")
    
    accuracy = evaluator.evaluate(predictions)
    params = model.getEstimatorParamMaps()[argmax(model.avgMetrics)]
    
    logger.write2file("Evaluating "+ str(modelType),"Display 5 datapoints:\n" + str(samplePredict.take(5)) + "\nAccuracy: " + str(accuracy)+"\nParameters:\n" + str(params))
    logger.write2fileModel(model, str(modelType))
    samplePredict.show(5)
    print("Accuracy: ",accuracy, "\nParameters\n",params)

    predLabel = predictions.select([col('label').cast('float'),col('prediction').cast('float')])
    metrics = MulticlassMetrics(predLabel.rdd)

    print("Confusion matrix:", metrics.confusionMatrix())

    
    return model, predictions