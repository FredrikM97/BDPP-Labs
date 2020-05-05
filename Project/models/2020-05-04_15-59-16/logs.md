

# 2020-05-04 15:59:53 
__ML - Test - No Quantilization:__
Dont use in production!

# 2020-05-04 15:59:53 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.app.id', 'local-1588607958493'), ('spark.driver.port', '42087'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-04 16:00:12 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 16:00:30 
__Number of rows:__
2974335

# 2020-05-04 16:00:30 
__Specified state:__
CA

# 2020-05-04 16:00:45 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 6, 23, 10, 31, 12), Start_Lat=38.653061, Start_Lng=-121.070541, Distance(mi)=0.0, Number=None, Street='Latrobe Rd', Side='R', City='El Dorado Hills', County='El Dorado', State='CA', Zipcode='95762', Country='US', Timezone='US/Pacific', Airport_Code='KMHR', Weather_Timestamp=datetime.datetime(2016, 6, 23, 10, 46), Temperature(F)=77.0, Wind_Chill(F)=None, Humidity(%)=34.0, Pressure(in)=30.02, Visibility(mi)=10.0, Wind_Direction='SW', Wind_Speed(mph)=3.5, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=3, Start_Month=6, Weather_Hour=3, Weather_Month=6)]

# 2020-05-04 16:02:20 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 6, 23, 10, 31, 12), Start_Lat=38.653061, Start_Lng=-121.070541, Distance(mi)=0.0, Number=None, Street='Latrobe Rd', Side='R', City='El Dorado Hills', County='El Dorado', State='CA', Zipcode='95762', Country='US', Timezone='US/Pacific', Airport_Code='KMHR', Weather_Timestamp=datetime.datetime(2016, 6, 23, 10, 46), Temperature(F)=77.0, Wind_Chill(F)=None, Humidity(%)=34.0, Pressure(in)=30.02, Visibility(mi)=10.0, Wind_Direction='SW', Wind_Speed(mph)=3.5, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=3, Start_Month=6, Weather_Hour=3, Weather_Month=6, Start_Lat_disc=95.0, Start_Lng_disc=35.0, Start_Lat_IDX=6.0, Start_Lng_IDX=40.0, Start_Lat_IDX_vec=SparseVector(99, {6: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {40: 1.0}), position=SparseVector(198, {6: 1.0, 139: 1.0}))]

# 2020-05-04 16:02:20 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'City', 'State', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-04 16:02:42 
__Missing values:__
[Row(Severity=0, Start_Hour=205, Start_Month=205, Weather_Hour=9397, Weather_Month=9397, Distance(mi)=0, City=6, State=0, Side=0, Temperature(F)=15125, Wind_Chill(F)=471819, Humidity(%)=16314, Pressure(in)=11242, Visibility(mi)=13196, Wind_Direction=12148, Wind_Speed(mph)=128806, Weather_Condition=12881, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=6, Civil_Twilight=6, Nautical_Twilight=6, Astronomical_Twilight=6)]

# 2020-05-04 16:05:14 
__Weather condition:__
[Row(Weather_Condition='Clear', count=253070), Row(Weather_Condition='Fair', count=103016), Row(Weather_Condition='Mostly Cloudy', count=60440), Row(Weather_Condition='Partly Cloudy', count=59555), Row(Weather_Condition='Overcast', count=58472), Row(Weather_Condition='Scattered Clouds', count=29356), Row(Weather_Condition='Cloudy', count=24959), Row(Weather_Condition='Haze', count=21830), Row(Weather_Condition='Light Rain', count=20437), Row(Weather_Condition=None, count=12881), Row(Weather_Condition='Rain', count=6438), Row(Weather_Condition='Fog', count=4138), Row(Weather_Condition='Heavy Rain', count=2246), Row(Weather_Condition='Smoke', count=1923), Row(Weather_Condition='Fair / Windy', count=1244)]
Rows removed: 16080

# 2020-05-04 16:15:34 
__Feature set size:__
647124

__Feature vector and label:__
[Row(features=SparseVector(1308, {1: 0.6796, 2: 0.6379, 3: 0.3333, 4: 0.9078, 5: 0.0714, 6: 0.0043, 18: 1.0, 39: 1.0, 53: 1.0, 77: 1.0, 305: 1.0, 1212: 1.0, 1214: 1.0, 1224: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}), label=2)]

# 2020-05-04 16:15:53 
__Number of rows:__
647124

# 2020-05-04 16:24:36 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(City=1128), Row(State=1), Row(Side=3), Row(Wind_Direction=24), Row(Weather_Condition=14), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-04 16:26:00 
__PCA - Feature variance:__
Top 50:
[0.15647288 0.03674622 0.02903741 0.0274143  0.02574009 0.02257426
 0.02160349 0.02137782 0.02088537 0.01993176 0.0187659  0.0184628
 0.01735791 0.01666459 0.01641122 0.01603264 0.01465881 0.0139182
 0.01336794 0.01301084 0.01250828 0.01205251 0.01183846 0.01133615
 0.01126434 0.01067314 0.01042863 0.01037037 0.00997989 0.00988341
 0.00957458 0.00932925 0.00893061 0.00886139 0.00816758 0.00748078
 0.00739187 0.00703781 0.00636361 0.00634665 0.00625429 0.00594456
 0.00569898 0.00552643 0.00543378 0.00521767 0.00505745 0.00482708
 0.00472957 0.00449717]
Number of items: 250
Sum of variance: 0.9715954180081925

# 2020-05-04 16:28:54 
__Top selected features according to ChiSqSelector:__
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 48, 49, 53, 54, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 105, 106, 107, 108, 109, 110, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 148, 149, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 184, 185, 186, 187, 188, 189, 190, 192, 193, 195, 197, 198, 199, 200, 201, 202, 203, 204, 206, 207, 210, 211, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 241, 242, 244, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 259, 260, 261, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 284, 285, 286, 287, 288, 290, 291, 292, 293, 294, 296, 297, 298, 299, 300]
Number of features: 250
Example data:
[Row(features=SparseVector(1308, {1: 0.6796, 2: 0.6379, 3: 0.3333, 4: 0.9078, 5: 0.0714, 6: 0.0043, 18: 1.0, 39: 1.0, 53: 1.0, 77: 1.0, 305: 1.0, 1212: 1.0, 1214: 1.0, 1224: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.6796, 2: 0.6379, 3: 0.3333, 4: 0.9078, 5: 0.0714, 6: 0.0043, 15: 1.0, 33: 1.0, 42: 1.0, 60: 1.0})), Row(features=SparseVector(1308, {0: 0.0, 1: 0.4825, 2: 0.4676, 3: 0.7071, 4: 0.9099, 5: 0.0714, 6: 0.0098, 9: 1.0, 42: 1.0, 49: 1.0, 80: 1.0, 192: 1.0, 1212: 1.0, 1214: 1.0, 1226: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}), label=3, selectedFeatures=SparseVector(250, {0: 0.0, 1: 0.4825, 2: 0.4676, 3: 0.7071, 4: 0.9099, 5: 0.0714, 6: 0.0098, 9: 1.0, 36: 1.0, 41: 1.0, 63: 1.0, 159: 1.0})), Row(features=SparseVector(1308, {1: 0.7298, 2: 0.6379, 3: 0.2424, 4: 0.9056, 5: 0.0714, 6: 0.0098, 9: 1.0, 37: 1.0, 46: 1.0, 75: 1.0, 213: 1.0, 1212: 1.0, 1214: 1.0, 1223: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.7298, 2: 0.6379, 3: 0.2424, 4: 0.9056, 5: 0.0714, 6: 0.0098, 9: 1.0, 31: 1.0, 39: 1.0, 58: 1.0, 174: 1.0})), Row(features=SparseVector(1308, {1: 0.7298, 2: 0.6379, 3: 0.2424, 4: 0.9056, 5: 0.0714, 6: 0.0098, 9: 1.0, 37: 1.0, 46: 1.0, 75: 1.0, 90: 1.0, 1212: 1.0, 1214: 1.0, 1223: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.7298, 2: 0.6379, 3: 0.2424, 4: 0.9056, 5: 0.0714, 6: 0.0098, 9: 1.0, 31: 1.0, 39: 1.0, 58: 1.0, 71: 1.0})), Row(features=SparseVector(1308, {1: 0.6478, 2: 0.6379, 3: 0.4545, 4: 0.9075, 5: 0.0714, 6: 0.0098, 9: 1.0, 37: 1.0, 46: 1.0, 75: 1.0, 85: 1.0, 1212: 1.0, 1214: 1.0, 1226: 1.0, 1245: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}), label=3, selectedFeatures=SparseVector(250, {1: 0.6478, 2: 0.6379, 3: 0.4545, 4: 0.9075, 5: 0.0714, 6: 0.0098, 9: 1.0, 31: 1.0, 39: 1.0, 58: 1.0, 67: 1.0}))]

# 2020-05-04 16:29:55 
__Fitting LR_Model model..:__


# 2020-05-04 16:42:11 
__Predicting LR_Model on testSet..:__


# 2020-05-04 16:42:11 
__Evaluating LR_Model predictions..:__


# 2020-05-04 16:43:50 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6294, 2: 0.6379, 3: 0.6465, 4: 0.9078, 5: 0.0714, 6: 0.0084, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1218: 1.0, 1245: 1.0, 1258: 1.0, 1261: 1.0, 1265: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6726, 2: 0.6379, 3: 0.4747, 4: 0.902, 5: 0.0714, 6: 0.0084, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1218: 1.0, 1248: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(1308, {0: 0.0, 1: 0.5969, 2: 0.6379, 3: 0.7475, 4: 0.9065, 5: 0.0714, 6: 0.007, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1221: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6599, 2: 0.6379, 3: 0.5859, 4: 0.9029, 5: 0.0714, 6: 0.0098, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1221: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6224, 2: 0.6379, 3: 0.697, 4: 0.9053, 5: 0.0714, 6: 0.007, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1225: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}))]
Accuracy: 0.6383886161938083
Parameters:
{Param(parent='LogisticRegression_dee3a77c0f6d', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_dee3a77c0f6d', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_dee3a77c0f6d', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-04 16:44:04 
__Fitting DT_Model model..:__


# 2020-05-04 16:58:49 
__Predicting DT_Model on testSet..:__


# 2020-05-04 16:58:49 
__Evaluating DT_Model predictions..:__


# 2020-05-04 17:00:26 
__Evaluating DT_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6294, 2: 0.6379, 3: 0.6465, 4: 0.9078, 5: 0.0714, 6: 0.0084, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1218: 1.0, 1245: 1.0, 1258: 1.0, 1261: 1.0, 1265: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6726, 2: 0.6379, 3: 0.4747, 4: 0.902, 5: 0.0714, 6: 0.0084, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1218: 1.0, 1248: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(1308, {0: 0.0, 1: 0.5969, 2: 0.6379, 3: 0.7475, 4: 0.9065, 5: 0.0714, 6: 0.007, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1221: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6599, 2: 0.6379, 3: 0.5859, 4: 0.9029, 5: 0.0714, 6: 0.0098, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1221: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6224, 2: 0.6379, 3: 0.697, 4: 0.9053, 5: 0.0714, 6: 0.007, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1225: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}))]
Accuracy: 0.575916867495116
Parameters:
{}

# 2020-05-04 17:00:39 
__Fitting RF_Model model..:__


# 2020-05-04 17:26:15 
__Predicting RF_Model on testSet..:__


# 2020-05-04 17:26:15 
__Evaluating RF_Model predictions..:__


# 2020-05-04 17:27:53 
__Evaluating RF_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6294, 2: 0.6379, 3: 0.6465, 4: 0.9078, 5: 0.0714, 6: 0.0084, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1218: 1.0, 1245: 1.0, 1258: 1.0, 1261: 1.0, 1265: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6726, 2: 0.6379, 3: 0.4747, 4: 0.902, 5: 0.0714, 6: 0.0084, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1218: 1.0, 1248: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(1308, {0: 0.0, 1: 0.5969, 2: 0.6379, 3: 0.7475, 4: 0.9065, 5: 0.0714, 6: 0.007, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1221: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1291: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6599, 2: 0.6379, 3: 0.5859, 4: 0.9029, 5: 0.0714, 6: 0.0098, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1221: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1308, {0: 0.0, 1: 0.6224, 2: 0.6379, 3: 0.697, 4: 0.9053, 5: 0.0714, 6: 0.007, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1212: 1.0, 1214: 1.0, 1225: 1.0, 1243: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0, 1267: 1.0, 1270: 1.0, 1273: 1.0, 1276: 1.0, 1279: 1.0, 1282: 1.0, 1285: 1.0, 1288: 1.0, 1292: 1.0, 1294: 1.0, 1296: 1.0, 1299: 1.0, 1302: 1.0, 1305: 1.0}))]
Accuracy: 0.5397890894328533
Parameters:
{Param(parent='RandomForestClassifier_085092864305', name='numTrees', doc='Number of trees to train (>= 1).'): 20}