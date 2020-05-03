from pyspark.sql.functions import when, count, col, isnan, countDistinct,from_unixtime,from_utc_timestamp, unix_timestamp,split, to_timestamp, hour, month, lit,collect_list
import seaborn as sns 
import matplotlib.pyplot as plt 
from datetime import datetime

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

def write2file(file,info):
    f = open(file, "a")
    f.write("\n\n"+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n" + info)
    f.close()
    
def setup_spark(file=""):
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

        sc = SparkContext(conf=conf)

    except Exception as e:
        sc = spark.SparkContext
        print(e)
    # spark.num.executors is set since we dont have enough ram for 8 
    # Note: 6 running processes each having 2gb => 12 gb ram used
    spark = SparkSession.builder \
        .appName("Spark Project") \
        .master("local[*]") \
        .config("spark.driver.host", "localhost") \
        .config('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener') \
        .config('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar') \
        .config('SPARKMONITOR_UI_HOST','192.168.1.228')\
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    df = spark.read.load(file,format="csv", sep=",", inferSchema="true", header="true")
    return df, sc

def printSparkConf(sc, logs_dir):
    tmp = sc._conf.getAll()
    write2file(logs_dir,"New Spark session: " + "\nSettings for spark:\n" + str(tmp))
    print("Config:",tmp)
    
def setup_variables(df, sc, colLabel, colRem, logs_dir):

    # Dropping data that cant help during model
    df = df.drop(*colRem)

    # Convert boolean to string since PCA cant handle boolean which should be a class
    df = df.select(*[col(c[0]).cast("string").alias(c[0]) if c[1] == 'boolean' else col(c[0]).alias(c[0]) for c in df.dtypes])

    #renamedHousing.select([count(when(col(c).isNull(), c)).alias(c) for c in colNum]).show()
    colCat, colNum = createNewClasses(df, sc, colLabel, logs_dir)

    return df, colCat, colNum

def createNewClasses(df, sc, colLabel, logs_dir):
    rdd = sc.parallelize(df.dtypes)
    colCat = rdd.map(lambda i: i[0] if (i[1]=='string' or i[1]=='boolean' and i[0] not in colLabel) else None).filter(lambda i: i != None).collect()
    colNum = rdd.map(lambda i: i[0] if (i[1]=='double' and i[0] not in colLabel) else None).filter(lambda i: i != None).collect()
    
    write2file(logs_dir,"Defined Label:\n" + str(colLabel) + "\nDefined Categories:\n" + str(colCat) + "\nDefined Numerical:\n" +str(colNum))
    
    print(f"Label: {colCat} \nCategories: {colCat}\nNumerical: {colNum}")
    return colCat, colNum 

def printMissingValues(df, logs_dir):

    # Check data
    df_missingVals_cols = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])

    # Missing value in each column
    tmp = df_missingVals_cols.collect()
    write2file(logs_dir,"Missing values:\n" + str(tmp))
    print("Missing values" + str(tmp))
    
def printCategoricalValues(df, colCat, logs_dir):
    # Checking how many classes that can be used
    tmp = [df.select(countDistinct(c).alias(c)).collect()[0] for c in colCat] 
    print("Unique column values:", tmp)

    write2file(logs_dir,"Categorical values: " + str(tmp))