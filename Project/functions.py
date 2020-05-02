# This file contains all functions availible

def setup_spark(projName='Spark Project', file="data/US_Accidents_Dec19.csv"):
    from pyspark.sql import SparkSession
    from pyspark import SparkContext, SparkConf

    try:
        spark.close()
    except: 
        pass

    try:
        conf = SparkConf().setAppName(projName)
        sc = SparkContext(conf=conf)
    except Exception as e:
        print(e)

    spark = SparkSession.builder \
        .appName(projName) \
        .master("local[*]") \
        .config("spark.executor.cores", "4") \
        .config("spark.executor.memory", "70g") \
        .config("spark.driver.memory", "12g") \
        .config("spark.memory.offHeap.enabled",True) \
         .config("spark.memory.offHeap.size","16g")  \
        .config("spark.yarn.executor.memoryOverhead",200) \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.default.parallelism", "6") \
        .getOrCreate()

    df = spark.read.load(file,format="csv", sep=",", inferSchema="true", header="true")

def preprocessing():
    pass

def setup_pipeline():
    f
    imputer = Imputer(inputCols=colNum, outputCols=colNum)
    imputer.setStrategy("median")
    
    num_assembler = VectorAssembler(inputCols=colNum, outputCol="num_features",handleInvalid="keep")
    scaler = StandardScaler(inputCol="num_features", withMean=True, withStd=True, outputCol="scaledFeatures")
    
    indexers = [StringIndexer(inputCol = c, outputCol = c +'_IDX', handleInvalid='keep') for c in colCat]
    
    encoder = OneHotEncoder(inputCols=[indexer.getOutputCol() for indexer in indexers], outputCols=["{0}_vec".format(indexer.getOutputCol()) for indexer in indexers],handleInvalid="keep")

def create_col_list(df):
    rdd = sc.parallelize(df.dtypes)

    colCat = rdd.map(lambda i: i[0] if (i[1]=='string' or i[1]=='boolean' and i[0]) else None).filter(lambda i: i != None).collect()
    colNum = rdd.map(lambda i: i[0] if (i[1]=='double' and i[0]) else None).filter(lambda i: i != None).collect()

def filter_on_group(column='State',group="CA"):
    df = df.filter(df[column] == group) # Lowers the dataset quite a lot
    return df

def get_missingVals(df):
    df_missingVals_cols = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])

    # Missing value in each column
    df_missingVals_cols.collect()

def remove_occurance(df,param="Weather_Condition",procent=0.01, asc=False):
    
    n = int(df.count()*procent) # Limit the plot to ignore conditions below an limit
    old_cnt = df.count()
    
    freq_df = df.groupBy(param).count().orderBy('count',ascending=asc)
    df_filtered = freq_df.filter(freq_df['count'] > n)
    filtered_conditions = df_filtered.select("Weather_Condition").rdd.flatMap(lambda x: x).collect()
    df = df.filter(df['Weather_Condition'].isin(*filtered_conditions))

    diff_cnt = old_cnt - df.count()
    
    return df, df_filtered, diff_cnt
    
def count_cat(df, colCat):
    return [df.select(countDistinct(c).alias(c)).collect()[0] for c in colCat] # TODO CHECK SO IT WORKS

def createParams(algorithm, evaluator=MulticlassClassificationEvaluator(), k=10):
    """
    Create a crossValidator object for each algorithm with corresponding parameters
    
    Parameters
    ----------
    algorithm: 2D-list with tuple object 
        Carries the model object, and corresponding parameters
    evaluator: obj, Optional, default='MulticlassClassificationEvaluator()'
        Evaluator algorithm
    k: int, Optional, default='10'
        how many folds for CV
    
    Return
    ----------
    cvAlgs: list
        List of Crossvalidator objects
    """
    
    cvAlgs = []
    for model in algorithm:
        pipeline = Pipeline(stages=[model[0][0]])
        print("Model:",model[0][0])
        paramGrid = ParamGridBuilder()
        
        for index, param in enumerate(model[1:]):
            if index == 0: pass
            print("Parameter Added:",*param)
            paramGrid.addGrid(*param) 
        
        cv = CrossValidator(estimator=pipeline,
                          estimatorParamMaps=paramGrid.build(),
                          evaluator=evaluator,
                          numFolds=k) # Replace with 10 
        cvAlgs.append(cv)
        
    return cvAlgs

def evaluateAlgorithm(models, trainSet):
    """
    Fit each of the Crossvalidator objects and returns the best model
    
    Parameters
    ----------
    models: list
        Each of the models that shall be fitted
    trainSet: Dataframe
        Dataset for training
  
    
    Return
    ----------
    bestModels: list
        Best model from each Crossvalidator
    """
    
    
    bestModels = []
    for cv in models:
        print("Fitting model:",cv)
        cvModel = cv.fit(trainSet).bestModel
        bestModels.append(cvModel)
        print(cvModel)
        
    return bestModels

def makePredictions(model, testSet):
    """
    Make predictions based on model and testSet
    
    Parameters
    ----------
    model: Object
        Model
    testSet: Dataframe
        Set of dataframe to test the model
        
    Return
    ----------
    Result: Object
        Result of model
    """
    
    return cvModel.transform(testSet)
    
def getBestModel(bestModels,testSet):
    """
    Decides which model that is considered best (Final model) 
    
    TODO: Change criteria for best model.
    
    Parameters
    ----------
    bestModels: list
        Each model
    
    Return
    ----------
    bestModel: Object
        The final model decided
    """
   
    bestModel = (None,0)
    for cvModel in bestModels:
        
        try:
            trainingSummary = cvModel.stages[-1].summary
        except Exception as e:
            derp = trainingSummary = cvModel.stages[-1]
            #derp = makePredictions(model, testSet).select('prediction')
            print("Error occured! Decision tree?",derp)
            #print("Evaluate model:",cvModel, "Accuracy:",cvModel.)
            print(derp.toDebugString) 
            print(e)
           
        
        
        print("Evaluate model:",cvModel, "Accuracy:",trainingSummary.accuracy)
        if bestModel[1] < trainingSummary.weightedFMeasure():
            bestModel = (cvModel, trainingSummary.weightedFMeasure())
    return bestModel[0]