

# 2020-05-04 17:34:56 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.driver.port', '45063'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.app.id', 'local-1588613662352'), ('spark.rdd.compress', 'True'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-04 17:35:16 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 17:35:34 
__Number of rows:__
2974335

# 2020-05-04 17:35:34 
__No state specified:__


# 2020-05-04 17:35:49 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2)]

# 2020-05-04 17:37:22 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2, Start_Lat_disc=71.0, Start_Lng_disc=62.0, Start_Lat_IDX=13.0, Start_Lng_IDX=2.0, Start_Lat_IDX_vec=SparseVector(99, {13: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {2: 1.0}), position=SparseVector(198, {13: 1.0, 101: 1.0}))]

# 2020-05-04 17:37:22 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-04 17:37:50 
__Missing values:__
[Row(Severity=0, Start_Hour=3163, Start_Month=3163, Weather_Hour=36705, Weather_Month=36705, position=0, Distance(mi)=0, Side=0, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-04 17:38:15 
__Missing values:__
[Row(Severity=0, Start_Hour=3163, Start_Month=3163, Weather_Hour=36705, Weather_Month=36705, position=0, Distance(mi)=0, Side=0, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-04 17:40:37 
__Weather condition:__
[Row(Weather_Condition='Clear', count=808171), Row(Weather_Condition='Mostly Cloudy', count=412528), Row(Weather_Condition='Overcast', count=382480), Row(Weather_Condition='Fair', count=335289), Row(Weather_Condition='Partly Cloudy', count=295439), Row(Weather_Condition='Scattered Clouds', count=204662), Row(Weather_Condition='Light Rain', count=141073), Row(Weather_Condition='Cloudy', count=115496), Row(Weather_Condition=None, count=65932), Row(Weather_Condition='Light Snow', count=42123), Row(Weather_Condition='Haze', count=34315), Row(Weather_Condition='Rain', count=32826), Row(Weather_Condition='Fog', count=22138), Row(Weather_Condition='Heavy Rain', count=12064), Row(Weather_Condition='Light Drizzle', count=10277), Row(Weather_Condition='Light Thunderstorms and Rain', count=4928), Row(Weather_Condition='Snow', count=4796), Row(Weather_Condition='Thunderstorm', count=4438), Row(Weather_Condition='Fair / Windy', count=3759), Row(Weather_Condition='Smoke', count=3602)]
Rows removed: 103931

# 2020-05-04 17:50:35 
__Feature set size:__
2870404

__Feature vector and label:__
[Row(features=SparseVector(380, {13: 1.0, 101: 1.0, 198: 0.0, 199: 0.3651, 200: 0.6628, 201: 0.9091, 202: 0.8983, 203: 0.0714, 204: 0.0085, 218: 1.0, 241: 1.0, 256: 1.0, 279: 1.0, 281: 1.0, 285: 1.0, 316: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0, 375: 1.0, 378: 1.0}), label=3)]

# 2020-05-04 17:50:52 
__Number of rows:__
2870404

# 2020-05-04 17:58:41 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(Side=3), Row(Wind_Direction=24), Row(Weather_Condition=19), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2), Row(position=5426)]

# 2020-05-04 18:00:52 
__PCA - Feature variance:__
Top 50:
[0.1094752  0.03672713 0.02766258 0.02552215 0.02237357 0.02085361
 0.02071694 0.02015519 0.01864973 0.01784251 0.01546965 0.01539601
 0.01495146 0.01459431 0.01445054 0.01438461 0.01427251 0.01404826
 0.01390482 0.01257133 0.01244251 0.0115648  0.01133631 0.011104
 0.01093738 0.01052369 0.00996151 0.00990721 0.00974907 0.00924458
 0.0089352  0.00855806 0.00828106 0.00817457 0.00782569 0.00716806
 0.00624781 0.00615834 0.00578387 0.0056442  0.00531575 0.00511888
 0.00502859 0.00490412 0.00488057 0.00486245 0.00485263 0.0045226
 0.00442267 0.00436187]
Number of items: 250
Sum of variance: 0.9761522441841807

# 2020-05-04 18:03:34 
__Top selected features according to ChiSqSelector:__
[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 213, 214, 215, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 257, 259, 260, 261, 262, 263]
Number of features: 250
Example data:
[Row(features=SparseVector(380, {13: 1.0, 101: 1.0, 198: 0.0, 199: 0.3651, 200: 0.6628, 201: 0.9091, 202: 0.8983, 203: 0.0714, 204: 0.0085, 218: 1.0, 241: 1.0, 256: 1.0, 279: 1.0, 281: 1.0, 285: 1.0, 316: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0, 375: 1.0, 378: 1.0}), label=3, selectedFeatures=SparseVector(250, {12: 1.0, 94: 1.0, 190: 0.0, 191: 0.3651, 192: 0.6628, 193: 0.9091, 194: 0.8983, 195: 0.0714, 196: 0.0085, 230: 1.0})), Row(features=SparseVector(380, {95: 1.0, 183: 1.0, 198: 0.0, 199: 0.3675, 200: 0.5511, 201: 1.0, 202: 0.8965, 203: 0.0214, 204: 0.0056, 205: 1.0, 241: 1.0, 243: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 316: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=3, selectedFeatures=SparseVector(250, {89: 1.0, 175: 1.0, 190: 0.0, 191: 0.3675, 192: 0.5511, 193: 1.0, 194: 0.8965, 195: 0.0214, 196: 0.0056, 197: 1.0, 230: 1.0, 231: 1.0})), Row(features=SparseVector(380, {57: 1.0, 101: 1.0, 198: 0.0, 199: 0.2255, 200: 0.3582, 201: 0.8687, 202: 0.9165, 203: 0.0714, 204: 0.0056, 205: 1.0, 241: 1.0, 244: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 315: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=2, selectedFeatures=SparseVector(250, {53: 1.0, 94: 1.0, 190: 0.0, 191: 0.2255, 192: 0.3582, 193: 0.8687, 194: 0.9165, 195: 0.0714, 196: 0.0056, 197: 1.0, 230: 1.0, 232: 1.0})), Row(features=SparseVector(380, {92: 1.0, 112: 1.0, 199: 0.5556, 200: 0.6628, 201: 0.3333, 202: 0.9086, 203: 0.0714, 204: 0.0043, 205: 1.0, 240: 1.0, 243: 1.0, 278: 1.0, 281: 1.0, 290: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=2, selectedFeatures=SparseVector(250, {86: 1.0, 105: 1.0, 191: 0.5556, 192: 0.6628, 193: 0.3333, 194: 0.9086, 195: 0.0714, 196: 0.0043, 197: 1.0, 229: 1.0, 231: 1.0})), Row(features=SparseVector(380, {39: 1.0, 156: 1.0, 198: 0.0, 199: 0.4084, 200: 0.5959, 201: 0.7071, 202: 0.9107, 203: 0.0714, 204: 0.0098, 217: 1.0, 237: 1.0, 253: 1.0, 275: 1.0, 281: 1.0, 294: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=3, selectedFeatures=SparseVector(250, {37: 1.0, 148: 1.0, 190: 0.0, 191: 0.4084, 192: 0.5959, 193: 0.7071, 194: 0.9107, 195: 0.0714, 196: 0.0098, 208: 1.0, 226: 1.0, 241: 1.0}))]

# 2020-05-04 18:05:18 
__Fitting LR_Model model..:__


# 2020-05-04 18:32:02 
__Predicting LR_Model on testSet..:__


# 2020-05-04 18:32:02 
__Evaluating LR_Model predictions..:__


# 2020-05-04 18:35:15 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 99: 1.0, 199: 0.6239, 200: 0.6628, 201: 0.3333, 202: 0.9116, 203: 0.0714, 204: 0.0043, 212: 1.0, 240: 1.0, 250: 1.0, 278: 1.0, 281: 1.0, 288: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.4274, 200: 0.6628, 201: 0.9394, 202: 0.9083, 203: 0.0286, 204: 0.0043, 205: 1.0, 241: 1.0, 243: 1.0, 279: 1.0, 281: 1.0, 297: 1.0, 312: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.4444, 200: 0.6628, 201: 0.7677, 202: 0.9186, 203: 0.05, 204: 0.007, 207: 1.0, 230: 1.0, 245: 1.0, 268: 1.0, 281: 1.0, 303: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 337: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.453, 200: 0.6628, 201: 0.9394, 202: 0.9165, 203: 0.0014, 204: 0.0085, 207: 1.0, 232: 1.0, 243: 1.0, 270: 1.0, 281: 1.0, 285: 1.0, 321: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.3846, 200: 0.5622, 201: 0.4141, 202: 0.9207, 203: 0.0714, 204: 0.0098, 209: 1.0, 232: 1.0, 249: 1.0, 270: 1.0, 281: 1.0, 294: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}))]
Accuracy: 0.5698276935164841
Parameters:
{Param(parent='LogisticRegression_4020230b9f56', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_4020230b9f56', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_4020230b9f56', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-04 18:35:38 
__Fitting DT_Model model..:__


# 2020-05-04 19:07:24 
__Predicting DT_Model on testSet..:__


# 2020-05-04 19:07:24 
__Evaluating DT_Model predictions..:__


# 2020-05-04 19:10:38 
__Evaluating DT_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 99: 1.0, 199: 0.6239, 200: 0.6628, 201: 0.3333, 202: 0.9116, 203: 0.0714, 204: 0.0043, 212: 1.0, 240: 1.0, 250: 1.0, 278: 1.0, 281: 1.0, 288: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.4274, 200: 0.6628, 201: 0.9394, 202: 0.9083, 203: 0.0286, 204: 0.0043, 205: 1.0, 241: 1.0, 243: 1.0, 279: 1.0, 281: 1.0, 297: 1.0, 312: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.4444, 200: 0.6628, 201: 0.7677, 202: 0.9186, 203: 0.05, 204: 0.007, 207: 1.0, 230: 1.0, 245: 1.0, 268: 1.0, 281: 1.0, 303: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 337: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.453, 200: 0.6628, 201: 0.9394, 202: 0.9165, 203: 0.0014, 204: 0.0085, 207: 1.0, 232: 1.0, 243: 1.0, 270: 1.0, 281: 1.0, 285: 1.0, 321: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.3846, 200: 0.5622, 201: 0.4141, 202: 0.9207, 203: 0.0714, 204: 0.0098, 209: 1.0, 232: 1.0, 249: 1.0, 270: 1.0, 281: 1.0, 294: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}))]
Accuracy: 0.5840808211364495
Parameters:
{}

# 2020-05-04 19:11:01 
__Fitting RF_Model model..:__


# 2020-05-04 20:16:05 
__Predicting RF_Model on testSet..:__


# 2020-05-04 20:16:05 
__Evaluating RF_Model predictions..:__


# 2020-05-04 20:19:22 
__Evaluating RF_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 99: 1.0, 199: 0.6239, 200: 0.6628, 201: 0.3333, 202: 0.9116, 203: 0.0714, 204: 0.0043, 212: 1.0, 240: 1.0, 250: 1.0, 278: 1.0, 281: 1.0, 288: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.4274, 200: 0.6628, 201: 0.9394, 202: 0.9083, 203: 0.0286, 204: 0.0043, 205: 1.0, 241: 1.0, 243: 1.0, 279: 1.0, 281: 1.0, 297: 1.0, 312: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.4444, 200: 0.6628, 201: 0.7677, 202: 0.9186, 203: 0.05, 204: 0.007, 207: 1.0, 230: 1.0, 245: 1.0, 268: 1.0, 281: 1.0, 303: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 337: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.453, 200: 0.6628, 201: 0.9394, 202: 0.9165, 203: 0.0014, 204: 0.0085, 207: 1.0, 232: 1.0, 243: 1.0, 270: 1.0, 281: 1.0, 285: 1.0, 321: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {0: 1.0, 101: 1.0, 198: 0.0, 199: 0.3846, 200: 0.5622, 201: 0.4141, 202: 0.9207, 203: 0.0714, 204: 0.0098, 209: 1.0, 232: 1.0, 249: 1.0, 270: 1.0, 281: 1.0, 294: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}))]
Accuracy: 0.5400091626834861
Parameters:
{Param(parent='RandomForestClassifier_47dc64dbb1d6', name='numTrees', doc='Number of trees to train (>= 1).'): 10}