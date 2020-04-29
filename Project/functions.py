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
    return df.agg(*(countDistinct(col(c)).alias(c) for c in colCat)).collect()[0].asDict()