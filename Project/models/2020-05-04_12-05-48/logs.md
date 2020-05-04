

# 2020-05-04 12:06:27 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.driver.port', '33565'), ('spark.submit.deployMode', 'client'), ('spark.memory.fraction', '.6'), ('spark.ui.showConsoleProgress', 'true'), ('spark.app.id', 'local-1588593951266')]

# 2020-05-04 12:06:46 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 12:07:03 
__Number of rows:__
2974335

# 2020-05-04 12:07:03 
__No state specified:__


# 2020-05-04 12:07:18 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2)]

# 2020-05-04 12:08:51 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2, Start_Lat_disc=71.0, Start_Lng_disc=62.0, Start_Lat_IDX=11.0, Start_Lng_IDX=2.0, Start_Lat_IDX_vec=SparseVector(99, {11: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {2: 1.0}), position=SparseVector(198, {11: 1.0, 101: 1.0}))]

# 2020-05-04 12:08:51 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-04 12:09:19 
__Missing values:__
[Row(Severity=0, Start_Hour=3163, Start_Month=3163, Weather_Hour=36705, Weather_Month=36705, position=0, Distance(mi)=0, Side=0, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-04 12:09:45 
__Missing values:__
[Row(Severity=0, Start_Hour=3163, Start_Month=3163, Weather_Hour=36705, Weather_Month=36705, position=0, Distance(mi)=0, Side=0, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-04 12:12:12 
__Weather condition:__
[Row(Weather_Condition='Clear', count=808171), Row(Weather_Condition='Mostly Cloudy', count=412528), Row(Weather_Condition='Overcast', count=382480), Row(Weather_Condition='Fair', count=335289), Row(Weather_Condition='Partly Cloudy', count=295439), Row(Weather_Condition='Scattered Clouds', count=204662), Row(Weather_Condition='Light Rain', count=141073), Row(Weather_Condition='Cloudy', count=115496), Row(Weather_Condition=None, count=65932), Row(Weather_Condition='Light Snow', count=42123), Row(Weather_Condition='Haze', count=34315), Row(Weather_Condition='Rain', count=32826), Row(Weather_Condition='Fog', count=22138), Row(Weather_Condition='Heavy Rain', count=12064), Row(Weather_Condition='Light Drizzle', count=10277), Row(Weather_Condition='Light Thunderstorms and Rain', count=4928), Row(Weather_Condition='Snow', count=4796), Row(Weather_Condition='Thunderstorm', count=4438), Row(Weather_Condition='Fair / Windy', count=3759), Row(Weather_Condition='Smoke', count=3602)]
Rows removed: 103931

# 2020-05-04 12:22:23 
__Feature set size:__
2870404

__Feature vector and label:__
[Row(features=SparseVector(380, {11: 1.0, 101: 1.0, 198: 0.0, 199: 0.3651, 200: 0.6628, 201: 0.9091, 202: 0.8983, 203: 0.0714, 204: 0.0085, 218: 1.0, 241: 1.0, 256: 1.0, 279: 1.0, 281: 1.0, 285: 1.0, 316: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0, 375: 1.0, 378: 1.0}), label=3)]

# 2020-05-04 12:22:40 
__Number of rows:__
2870404

# 2020-05-04 12:30:35 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(Side=3), Row(Wind_Direction=24), Row(Weather_Condition=19), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2), Row(position=5406)]

# 2020-05-04 12:32:46 
__PCA - Feature variance:__
Top 50:
[0.10947651 0.03672697 0.02766299 0.02552226 0.02237386 0.02085386
 0.02071722 0.02015545 0.01865006 0.01784276 0.01547023 0.01539626
 0.01495166 0.0145945  0.01445063 0.01438479 0.01427268 0.01404841
 0.01390493 0.01257145 0.01244279 0.01156492 0.01133687 0.01110413
 0.01093771 0.01052406 0.00996134 0.00990643 0.00974911 0.00924468
 0.00893532 0.00855816 0.0082812  0.00817473 0.00782579 0.00716821
 0.00624939 0.0061582  0.00578394 0.00564452 0.00531562 0.00511877
 0.0050283  0.00490412 0.00488036 0.00486251 0.00485231 0.00452256
 0.00442257 0.00436215]
Number of items: 250
Sum of variance: 0.9761698682856236

# 2020-05-04 12:35:25 
__Top selected features according to ChiSqSelector:__
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 213, 214, 215, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 257, 259, 260, 261, 262, 263, 264]
Number of features: 250
Example data:
[Row(features=SparseVector(380, {11: 1.0, 101: 1.0, 198: 0.0, 199: 0.3651, 200: 0.6628, 201: 0.9091, 202: 0.8983, 203: 0.0714, 204: 0.0085, 218: 1.0, 241: 1.0, 256: 1.0, 279: 1.0, 281: 1.0, 285: 1.0, 316: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0, 375: 1.0, 378: 1.0}), label=3, selectedFeatures=SparseVector(250, {11: 1.0, 93: 1.0, 189: 0.0, 190: 0.3651, 191: 0.6628, 192: 0.9091, 193: 0.8983, 194: 0.0714, 195: 0.0085, 229: 1.0})), Row(features=SparseVector(380, {3: 1.0, 181: 1.0, 198: 0.0, 199: 0.3675, 200: 0.5511, 201: 1.0, 202: 0.8965, 203: 0.0214, 204: 0.0056, 205: 1.0, 241: 1.0, 243: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 316: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=3, selectedFeatures=SparseVector(250, {3: 1.0, 172: 1.0, 189: 0.0, 190: 0.3675, 191: 0.5511, 192: 1.0, 193: 0.8965, 194: 0.0214, 195: 0.0056, 196: 1.0, 229: 1.0, 230: 1.0})), Row(features=SparseVector(380, {92: 1.0, 101: 1.0, 198: 0.0, 199: 0.2255, 200: 0.3582, 201: 0.8687, 202: 0.9165, 203: 0.0714, 204: 0.0056, 205: 1.0, 241: 1.0, 244: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 315: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=2, selectedFeatures=SparseVector(250, {86: 1.0, 93: 1.0, 189: 0.0, 190: 0.2255, 191: 0.3582, 192: 0.8687, 193: 0.9165, 194: 0.0714, 195: 0.0056, 196: 1.0, 229: 1.0, 231: 1.0})), Row(features=SparseVector(380, {67: 1.0, 113: 1.0, 199: 0.5556, 200: 0.6628, 201: 0.3333, 202: 0.9086, 203: 0.0714, 204: 0.0043, 205: 1.0, 240: 1.0, 243: 1.0, 278: 1.0, 281: 1.0, 290: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=2, selectedFeatures=SparseVector(250, {62: 1.0, 105: 1.0, 190: 0.5556, 191: 0.6628, 192: 0.3333, 193: 0.9086, 194: 0.0714, 195: 0.0043, 196: 1.0, 228: 1.0, 230: 1.0})), Row(features=SparseVector(380, {73: 1.0, 153: 1.0, 198: 0.0, 199: 0.4084, 200: 0.5959, 201: 0.7071, 202: 0.9107, 203: 0.0714, 204: 0.0098, 217: 1.0, 237: 1.0, 253: 1.0, 275: 1.0, 281: 1.0, 294: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}), label=3, selectedFeatures=SparseVector(250, {68: 1.0, 144: 1.0, 189: 0.0, 190: 0.4084, 191: 0.5959, 192: 0.7071, 193: 0.9107, 194: 0.0714, 195: 0.0098, 207: 1.0, 225: 1.0, 240: 1.0}))]

# 2020-05-04 12:37:11 
__Fitting LR_Model model..:__


# 2020-05-04 13:00:33 
__Predicting LR_Model on testSet..:__


# 2020-05-04 13:00:33 
__Evaluating LR_Model predictions..:__


# 2020-05-04 13:03:49 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(380, {2: 1.0, 99: 1.0, 198: 0.0, 199: 0.4554, 200: 0.6628, 201: 0.7677, 202: 0.9107, 203: 0.0714, 204: 0.021, 205: 1.0, 230: 1.0, 244: 1.0, 268: 1.0, 281: 1.0, 296: 1.0, 312: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(380, {2: 1.0, 99: 1.0, 198: 0.0032, 199: 0.3419, 200: 0.4947, 201: 0.8485, 202: 0.8941, 203: 0.0214, 204: 0.0126, 205: 1.0, 237: 1.0, 243: 1.0, 275: 1.0, 281: 1.0, 288: 1.0, 318: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {2: 1.0, 99: 1.0, 198: 0.0, 199: 0.3656, 200: 0.5323, 201: 0.8182, 202: 0.9162, 203: 0.0714, 204: 0.0112, 205: 1.0, 239: 1.0, 243: 1.0, 277: 1.0, 281: 1.0, 296: 1.0, 315: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(380, {2: 1.0, 99: 1.0, 198: 0.0, 199: 0.2659, 200: 0.3991, 201: 0.8081, 202: 0.9268, 203: 0.0714, 204: 0.0084, 205: 1.0, 241: 1.0, 243: 1.0, 279: 1.0, 281: 1.0, 302: 1.0, 310: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(380, {2: 1.0, 99: 1.0, 198: 0.0, 199: 0.3656, 200: 0.5196, 201: 0.7879, 202: 0.9044, 203: 0.0714, 204: 0.0182, 206: 1.0, 232: 1.0, 244: 1.0, 270: 1.0, 281: 1.0, 293: 1.0, 312: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 368: 1.0, 371: 1.0, 374: 1.0, 377: 1.0}))]
Accuracy: 0.5715905001896042
Parameters:
{Param(parent='LogisticRegression_4a6d07f3b7e4', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_4a6d07f3b7e4', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_4a6d07f3b7e4', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-04 13:04:12 
__Fitting DT_Model model..:__


# 2020-05-04 13:13:08 
__Fitting DT_Model model..:__
