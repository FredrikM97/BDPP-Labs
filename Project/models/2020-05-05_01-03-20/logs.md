

# 2020-05-05 01:04:04 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.app.id', 'local-1588640602873'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.port', '41849')]

# 2020-05-05 01:04:31 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-05 01:04:53 
__Number of rows:__
2974335

# 2020-05-05 01:04:53 
__Specified state:__
PA

# 2020-05-05 01:05:07 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 12, 26, 14, 0, 12), Start_Lat=41.338398, Start_Lng=-74.83712, Distance(mi)=0.01, Number=None, Street='I-84 E', Side='R', City='Milford', County='Pike', State='PA', Zipcode='18337', Country='US', Timezone='US/Eastern', Airport_Code='KFWN', Weather_Timestamp=datetime.datetime(2016, 12, 26, 13, 53), Temperature(F)=28.9, Wind_Chill(F)=25.2, Humidity(%)=85.0, Pressure(in)=30.54, Visibility(mi)=3.0, Wind_Direction='East', Wind_Speed(mph)=3.5, Precipitation(in)=0.01, Weather_Condition='Overcast', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=9, Start_Month=12, Weather_Hour=8, Weather_Month=12)]

# 2020-05-05 01:06:40 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 12, 26, 14, 0, 12), Start_Lat=41.338398, Start_Lng=-74.83712, Distance(mi)=0.01, Number=None, Street='I-84 E', Side='R', City='Milford', County='Pike', State='PA', Zipcode='18337', Country='US', Timezone='US/Eastern', Airport_Code='KFWN', Weather_Timestamp=datetime.datetime(2016, 12, 26, 13, 53), Temperature(F)=28.9, Wind_Chill(F)=25.2, Humidity(%)=85.0, Pressure(in)=30.54, Visibility(mi)=3.0, Wind_Direction='East', Wind_Speed(mph)=3.5, Precipitation(in)=0.01, Weather_Condition='Overcast', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=9, Start_Month=12, Weather_Hour=8, Weather_Month=12, Start_Lat_disc=98.0, Start_Lng_disc=99.0, Start_Lat_IDX=91.0, Start_Lng_IDX=16.0, Start_Lat_IDX_vec=SparseVector(99, {91: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {16: 1.0}), position=SparseVector(198, {91: 1.0, 115: 1.0}))]

# 2020-05-05 01:06:40 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'City', 'State', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-05 01:06:59 
__Missing values:__
[Row(Severity=0, Start_Hour=0, Start_Month=0, Weather_Hour=798, Weather_Month=798, Distance(mi)=0, City=0, State=0, Side=0, Temperature(F)=1207, Wind_Chill(F)=53527, Humidity(%)=1343, Pressure(in)=864, Visibility(mi)=1308, Wind_Direction=985, Wind_Speed(mph)=17354, Weather_Condition=1274, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=0, Civil_Twilight=0, Nautical_Twilight=0, Astronomical_Twilight=0)]

# 2020-05-05 01:09:24 
__Weather condition:__
[Row(Weather_Condition='Clear', count=28687), Row(Weather_Condition='Overcast', count=18185), Row(Weather_Condition='Mostly Cloudy', count=9406), Row(Weather_Condition='Fair', count=6915), Row(Weather_Condition='Scattered Clouds', count=6179), Row(Weather_Condition='Partly Cloudy', count=5010), Row(Weather_Condition='Light Rain', count=4833), Row(Weather_Condition='Cloudy', count=3356), Row(Weather_Condition='Light Snow', count=2095), Row(Weather_Condition=None, count=1274), Row(Weather_Condition='Rain', count=996), Row(Weather_Condition='Fog', count=941), Row(Weather_Condition='Haze', count=706), Row(Weather_Condition='Heavy Rain', count=375), Row(Weather_Condition='Snow', count=257), Row(Weather_Condition='Light Drizzle', count=189), Row(Weather_Condition='Light Freezing Rain', count=165), Row(Weather_Condition='Heavy Snow', count=91)]
Rows removed: 2009

# 2020-05-05 01:19:34 
__Feature set size:__
88386

__Feature vector and label:__
[Row(features=SparseVector(1267, {0: 0.0001, 1: 0.3593, 2: 0.4295, 3: 0.8485, 4: 0.9194, 5: 0.0395, 6: 0.098, 18: 1.0, 35: 1.0, 57: 1.0, 73: 1.0, 373: 1.0, 1170: 1.0, 1172: 1.0, 1183: 1.0, 1201: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}), label=3)]

# 2020-05-05 01:19:52 
__Number of rows:__
88386

# 2020-05-05 01:28:12 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(City=1086), Row(State=1), Row(Side=2), Row(Wind_Direction=24), Row(Weather_Condition=17), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=1), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-05 01:29:18 
__PCA - Feature variance:__
Top 50:
[0.1084606  0.04887023 0.0391047  0.03223598 0.02727851 0.02479509
 0.0236579  0.02274469 0.02203286 0.02121568 0.02080695 0.01960652
 0.01874708 0.01795997 0.01717408 0.01686945 0.01646196 0.01543653
 0.01534089 0.01507955 0.01492685 0.01365635 0.01281599 0.01157016
 0.01104464 0.01076146 0.01072034 0.01003153 0.00962655 0.0094986
 0.00923856 0.00881244 0.00865981 0.00839613 0.00786474 0.00773318
 0.00750525 0.00730812 0.00700776 0.00680787 0.00658201 0.00636836
 0.00630263 0.00600014 0.00588419 0.00568452 0.00540776 0.00526724
 0.00505954 0.00503982]
Number of items: 250
Sum of variance: 0.9803030484952425

# 2020-05-05 01:30:48 
__Top selected features according to ChiSqSelector:__
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 24, 25, 26, 27, 28, 29, 30, 32, 45, 46, 47, 53, 55, 62, 63, 64, 65, 66, 67, 68, 70, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 110, 111, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 135, 137, 141, 145, 149, 156, 157, 161, 162, 164, 168, 169, 170, 171, 172, 178, 179, 183, 185, 187, 197, 198, 203, 207, 208, 213, 216, 220, 222, 223, 225, 229, 230, 233, 234, 238, 242, 249, 252, 256, 258, 264, 266, 268, 272, 275, 277, 280, 283, 285, 298, 300, 315, 324, 329, 332, 333, 343, 358, 361, 365, 368, 369, 374, 382, 386, 396, 413, 414, 424, 432, 442, 448, 457, 458, 460, 476, 479, 486, 524, 551, 556, 566, 580, 604, 605, 612, 614, 628, 636, 663, 678, 721, 745, 1172, 1173, 1175, 1200, 1202, 1205, 1206, 1208, 1209, 1212, 1215, 1218, 1219, 1224, 1225, 1230, 1231, 1236, 1237, 1241, 1242, 1244, 1245, 1250, 1251, 1255, 1256, 1258, 1259, 1261, 1262, 1264, 1265, 128, 199, 271, 360, 10, 98, 362, 1197, 48, 733, 218, 491, 722, 236, 1179, 577, 1213, 251, 811, 833, 834, 841, 181, 122, 344, 163, 559, 562, 630, 632, 109, 144, 289, 246, 158, 314, 18, 11, 112, 286, 94, 316, 150, 139, 354, 418, 702, 301, 453]
Number of features: 250
Example data:
[Row(features=SparseVector(1267, {0: 0.0001, 1: 0.3593, 2: 0.4295, 3: 0.8485, 4: 0.9194, 5: 0.0395, 6: 0.098, 18: 1.0, 35: 1.0, 57: 1.0, 73: 1.0, 373: 1.0, 1170: 1.0, 1172: 1.0, 1183: 1.0, 1201: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}), label=3, selectedFeatures=SparseVector(250, {0: 0.0001, 1: 0.3593, 2: 0.4295, 3: 0.8485, 4: 0.9194, 5: 0.0395, 6: 0.098, 14: 1.0, 214: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(1267, {1: 0.7046, 2: 0.5071, 3: 0.596, 4: 0.8514, 5: 0.1316, 6: 0.1933, 13: 1.0, 34: 1.0, 49: 1.0, 72: 1.0, 852: 1.0, 1170: 1.0, 1173: 1.0, 1186: 1.0, 1200: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.7046, 2: 0.5071, 3: 0.596, 4: 0.8514, 5: 0.1316, 6: 0.1933, 215: 1.0, 219: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(1267, {1: 0.7944, 2: 0.5071, 3: 0.6869, 4: 0.8539, 5: 0.1316, 6: 0.1289, 14: 1.0, 36: 1.0, 50: 1.0, 74: 1.0, 373: 1.0, 1170: 1.0, 1172: 1.0, 1191: 1.0, 1200: 1.0, 1218: 1.0, 1221: 1.0, 1225: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1245: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.7944, 2: 0.5071, 3: 0.6869, 4: 0.8539, 5: 0.1316, 6: 0.1289, 214: 1.0, 219: 1.0, 228: 1.0, 231: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 239: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(1267, {0: 0.0001, 1: 0.5917, 2: 0.5071, 3: 1.0, 4: 0.7078, 5: 0.1316, 6: 0.1625, 16: 1.0, 33: 1.0, 55: 1.0, 71: 1.0, 86: 1.0, 1170: 1.0, 1172: 1.0, 1190: 1.0, 1201: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}), label=2, selectedFeatures=SparseVector(250, {0: 0.0001, 1: 0.5917, 2: 0.5071, 3: 1.0, 4: 0.7078, 5: 0.1316, 6: 0.1625, 13: 1.0, 28: 1.0, 40: 1.0, 214: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(1267, {0: 0.0001, 1: 0.6194, 2: 0.5071, 3: 1.0, 4: 0.7179, 5: 0.1053, 6: 0.098, 18: 1.0, 33: 1.0, 56: 1.0, 71: 1.0, 88: 1.0, 1170: 1.0, 1173: 1.0, 1189: 1.0, 1201: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}), label=2, selectedFeatures=SparseVector(250, {0: 0.0001, 1: 0.6194, 2: 0.5071, 3: 1.0, 4: 0.7179, 5: 0.1053, 6: 0.098, 14: 1.0, 42: 1.0, 215: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0}))]

# 2020-05-05 01:31:38 
__Fitting LR_Model model..:__


# 2020-05-05 01:40:43 
__Predicting LR_Model on testSet..:__


# 2020-05-05 01:40:43 
__Evaluating LR_Model predictions..:__


# 2020-05-05 01:41:50 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(1267, {0: 0.0001, 1: 0.5444, 2: 0.5071, 3: 0.6061, 4: 0.8489, 5: 0.1316, 6: 0.1289, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 83: 1.0, 1170: 1.0, 1172: 1.0, 1180: 1.0, 1201: 1.0, 1218: 1.0, 1221: 1.0, 1225: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1251: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1267, {0: 0.0001, 1: 0.6194, 2: 0.5071, 3: 0.7677, 4: 0.801, 5: 0.0526, 6: 0.2913, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 84: 1.0, 1170: 1.0, 1172: 1.0, 1179: 1.0, 1206: 1.0, 1218: 1.0, 1221: 1.0, 1225: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1251: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1267, {0: 0.0001, 1: 0.5546, 2: 0.5071, 3: 0.798, 4: 0.7884, 5: 0.1316, 6: 0.1625, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 84: 1.0, 1170: 1.0, 1173: 1.0, 1192: 1.0, 1205: 1.0, 1218: 1.0, 1221: 1.0, 1225: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1251: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1267, {0: 0.0001, 1: 0.4611, 2: 0.4976, 3: 0.8889, 4: 0.869, 5: 0.1316, 6: 0.2577, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 85: 1.0, 1170: 1.0, 1173: 1.0, 1183: 1.0, 1201: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1250: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(1267, {0: 0.0001, 1: 0.5546, 2: 0.5071, 3: 1.0, 4: 0.7859, 5: 0.0026, 6: 0.1933, 7: 1.0, 32: 1.0, 45: 1.0, 70: 1.0, 86: 1.0, 1170: 1.0, 1172: 1.0, 1175: 1.0, 1210: 1.0, 1218: 1.0, 1221: 1.0, 1224: 1.0, 1227: 1.0, 1230: 1.0, 1233: 1.0, 1236: 1.0, 1239: 1.0, 1241: 1.0, 1244: 1.0, 1247: 1.0, 1251: 1.0, 1253: 1.0, 1255: 1.0, 1258: 1.0, 1261: 1.0, 1264: 1.0}))]
Accuracy: 0.7685628819876815
Parameters:
{Param(parent='LogisticRegression_cfa0f73f3e2f', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_cfa0f73f3e2f', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_cfa0f73f3e2f', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-05 01:41:59 
__Fitting DT_Model model..:__
