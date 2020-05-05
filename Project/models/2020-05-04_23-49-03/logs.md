

# 2020-05-04 23:49:38 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.driver.port', '45635'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.app.id', 'local-1588636145712'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-04 23:49:58 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 23:50:14 
__Number of rows:__
2974335

# 2020-05-04 23:50:15 
__Specified state:__
PA

# 2020-05-04 23:50:29 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 12, 26, 14, 0, 12), Start_Lat=41.338398, Start_Lng=-74.83712, Distance(mi)=0.01, Number=None, Street='I-84 E', Side='R', City='Milford', County='Pike', State='PA', Zipcode='18337', Country='US', Timezone='US/Eastern', Airport_Code='KFWN', Weather_Timestamp=datetime.datetime(2016, 12, 26, 13, 53), Temperature(F)=28.9, Wind_Chill(F)=25.2, Humidity(%)=85.0, Pressure(in)=30.54, Visibility(mi)=3.0, Wind_Direction='East', Wind_Speed(mph)=3.5, Precipitation(in)=0.01, Weather_Condition='Overcast', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=9, Start_Month=12, Weather_Hour=8, Weather_Month=12)]

# 2020-05-04 23:51:55 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 12, 26, 14, 0, 12), Start_Lat=41.338398, Start_Lng=-74.83712, Distance(mi)=0.01, Number=None, Street='I-84 E', Side='R', City='Milford', County='Pike', State='PA', Zipcode='18337', Country='US', Timezone='US/Eastern', Airport_Code='KFWN', Weather_Timestamp=datetime.datetime(2016, 12, 26, 13, 53), Temperature(F)=28.9, Wind_Chill(F)=25.2, Humidity(%)=85.0, Pressure(in)=30.54, Visibility(mi)=3.0, Wind_Direction='East', Wind_Speed(mph)=3.5, Precipitation(in)=0.01, Weather_Condition='Overcast', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=9, Start_Month=12, Weather_Hour=8, Weather_Month=12, Start_Lat_disc=98.0, Start_Lng_disc=99.0, Start_Lat_IDX=69.0, Start_Lng_IDX=8.0, Start_Lat_IDX_vec=SparseVector(99, {69: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {8: 1.0}), position=SparseVector(198, {69: 1.0, 107: 1.0}))]

# 2020-05-04 23:51:55 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-04 23:52:13 
__Missing values:__
[Row(Severity=0, Start_Hour=0, Start_Month=0, Weather_Hour=798, Weather_Month=798, position=0, Distance(mi)=0, Side=0, Temperature(F)=1207, Wind_Chill(F)=53527, Humidity(%)=1343, Pressure(in)=864, Visibility(mi)=1308, Wind_Direction=985, Wind_Speed(mph)=17354, Weather_Condition=1274, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=0, Civil_Twilight=0, Nautical_Twilight=0, Astronomical_Twilight=0)]

# 2020-05-04 23:52:30 
__Missing values:__
[Row(Severity=0, Start_Hour=0, Start_Month=0, Weather_Hour=798, Weather_Month=798, position=0, Distance(mi)=0, Side=0, Temperature(F)=1207, Wind_Chill(F)=53527, Humidity(%)=1343, Pressure(in)=864, Visibility(mi)=1308, Wind_Direction=985, Wind_Speed(mph)=17354, Weather_Condition=1274, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=0, Civil_Twilight=0, Nautical_Twilight=0, Astronomical_Twilight=0)]

# 2020-05-04 23:54:46 
__Weather condition:__
[Row(Weather_Condition='Clear', count=28687), Row(Weather_Condition='Overcast', count=18185), Row(Weather_Condition='Mostly Cloudy', count=9406), Row(Weather_Condition='Fair', count=6915), Row(Weather_Condition='Scattered Clouds', count=6179), Row(Weather_Condition='Partly Cloudy', count=5010), Row(Weather_Condition='Light Rain', count=4833), Row(Weather_Condition='Cloudy', count=3356), Row(Weather_Condition='Light Snow', count=2095), Row(Weather_Condition=None, count=1274), Row(Weather_Condition='Rain', count=996), Row(Weather_Condition='Fog', count=941), Row(Weather_Condition='Haze', count=706), Row(Weather_Condition='Heavy Rain', count=375), Row(Weather_Condition='Snow', count=257), Row(Weather_Condition='Light Drizzle', count=189), Row(Weather_Condition='Light Freezing Rain', count=165), Row(Weather_Condition='Heavy Snow', count=91)]
Rows removed: 2009

# 2020-05-05 00:03:26 
__Feature set size:__
88386

__Feature vector and label:__
[Row(features=SparseVector(376, {69: 1.0, 107: 1.0, 198: 0.0001, 199: 0.3593, 200: 0.4295, 201: 0.8485, 202: 0.9194, 203: 0.0395, 204: 0.098, 216: 1.0, 233: 1.0, 255: 1.0, 271: 1.0, 281: 1.0, 292: 1.0, 310: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}), label=3)]

# 2020-05-05 00:03:43 
__Number of rows:__
88386

# 2020-05-05 00:11:12 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(Side=2), Row(Wind_Direction=24), Row(Weather_Condition=17), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=1), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2), Row(position=5702)]

# 2020-05-05 00:12:07 
__PCA - Feature variance:__
Top 50:
[0.09747934 0.04385494 0.03510259 0.02891582 0.02446922 0.02227481
 0.02125865 0.02044245 0.0198015  0.01905709 0.01870305 0.01758725
 0.01683906 0.01611707 0.01542902 0.01515708 0.01477207 0.01382513
 0.01378958 0.01350883 0.01341387 0.01221855 0.01151044 0.01038226
 0.00992573 0.00967386 0.00960326 0.00901109 0.00864669 0.00853016
 0.00818862 0.00790438 0.00775992 0.00750627 0.00694454 0.00679369
 0.00655251 0.00614309 0.00592227 0.00585048 0.0057049  0.00530083
 0.00512097 0.0048523  0.00459886 0.0045362  0.00446502 0.00445214
 0.00429428 0.00425893]
Number of items: 250
Sum of variance: 0.9686193462729151

# 2020-05-05 00:12:43 
__Top selected features according to ChiSqSelector:__
[0, 2, 3, 5, 6, 8, 11, 17, 20, 21, 22, 23, 27, 29, 30, 31, 32, 36, 37, 39, 44, 45, 47, 48, 50, 52, 53, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 79, 80, 81, 86, 88, 89, 90, 91, 92, 93, 94, 95, 98, 99, 100, 105, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 122, 123, 124, 125, 129, 132, 133, 136, 137, 141, 142, 143, 145, 148, 151, 152, 153, 157, 158, 159, 160, 161, 162, 163, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 180, 184, 186, 187, 188, 189, 194, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 213, 214, 222, 223, 224, 225, 226, 227, 228, 230, 243, 244, 245, 251, 253, 260, 261, 262, 263, 264, 265, 266, 268, 281, 282, 284, 309, 311, 314, 315, 317, 318, 321, 324, 327, 328, 333, 334, 339, 340, 345, 346, 350, 351, 353, 354, 359, 360, 364, 365, 367, 368, 370, 371, 373, 374, 154, 208, 306, 171, 246, 13, 288, 46, 322, 113, 167, 54, 25, 192, 34, 149, 72, 166, 106, 101, 216, 209, 33, 76, 191, 135, 254, 114, 250, 55, 183, 43, 82, 10, 139, 120, 127, 181, 63, 26, 220, 102, 234, 272, 218, 249, 196, 290, 325, 155, 38, 231, 269, 131, 147, 28, 121, 300, 297, 190, 51, 41, 274, 130, 236, 84, 212, 77, 182, 289, 241]
Number of features: 250
Example data:
[Row(features=SparseVector(376, {69: 1.0, 107: 1.0, 198: 0.0001, 199: 0.3593, 200: 0.4295, 201: 0.8485, 202: 0.9194, 203: 0.0395, 204: 0.098, 216: 1.0, 233: 1.0, 255: 1.0, 271: 1.0, 281: 1.0, 292: 1.0, 310: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}), label=3, selectedFeatures=SparseVector(250, {54: 1.0, 83: 1.0, 159: 0.0001, 160: 0.3593, 161: 0.4295, 162: 0.8485, 163: 0.9194, 164: 0.0395, 165: 0.098, 174: 1.0, 209: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(376, {69: 1.0, 107: 1.0, 199: 0.7046, 200: 0.5078, 201: 0.596, 202: 0.8514, 203: 0.1316, 204: 0.1933, 211: 1.0, 232: 1.0, 247: 1.0, 270: 1.0, 282: 1.0, 295: 1.0, 309: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}), label=2, selectedFeatures=SparseVector(250, {54: 1.0, 83: 1.0, 160: 0.7046, 161: 0.5078, 162: 0.596, 163: 0.8514, 164: 0.1316, 165: 0.1933, 210: 1.0, 218: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(376, {69: 1.0, 107: 1.0, 199: 0.7944, 200: 0.5078, 201: 0.6869, 202: 0.8539, 203: 0.1316, 204: 0.1289, 212: 1.0, 234: 1.0, 248: 1.0, 272: 1.0, 281: 1.0, 300: 1.0, 309: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 354: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}), label=2, selectedFeatures=SparseVector(250, {54: 1.0, 83: 1.0, 160: 0.7944, 161: 0.5078, 162: 0.6869, 163: 0.8539, 164: 0.1316, 165: 0.1289, 171: 1.0, 186: 1.0, 207: 1.0, 209: 1.0, 216: 1.0, 218: 1.0, 228: 1.0, 231: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 239: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(376, {36: 1.0, 187: 1.0, 198: 0.0001, 199: 0.5917, 200: 0.5078, 201: 1.0, 202: 0.7078, 203: 0.1316, 204: 0.1625, 214: 1.0, 231: 1.0, 253: 1.0, 269: 1.0, 281: 1.0, 299: 1.0, 310: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}), label=2, selectedFeatures=SparseVector(250, {24: 1.0, 150: 1.0, 159: 0.0001, 160: 0.5917, 161: 0.5078, 162: 1.0, 163: 0.7078, 164: 0.1316, 165: 0.1625, 173: 1.0, 185: 1.0, 196: 1.0, 206: 1.0, 209: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0})), Row(features=SparseVector(376, {9: 1.0, 120: 1.0, 198: 0.0001, 199: 0.6194, 200: 0.5078, 201: 1.0, 202: 0.7179, 203: 0.1053, 204: 0.098, 216: 1.0, 231: 1.0, 254: 1.0, 269: 1.0, 282: 1.0, 298: 1.0, 310: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}), label=2, selectedFeatures=SparseVector(250, {96: 1.0, 159: 0.0001, 160: 0.6194, 161: 0.5078, 162: 1.0, 163: 0.7179, 164: 0.1053, 165: 0.098, 174: 1.0, 185: 1.0, 197: 1.0, 206: 1.0, 210: 1.0, 228: 1.0, 230: 1.0, 232: 1.0, 234: 1.0, 236: 1.0, 238: 1.0, 240: 1.0, 242: 1.0, 244: 1.0, 246: 1.0, 248: 1.0}))]

# 2020-05-05 00:13:24 
__Fitting LR_Model model..:__


# 2020-05-05 00:22:09 
__Predicting LR_Model on testSet..:__


# 2020-05-05 00:22:09 
__Evaluating LR_Model predictions..:__


# 2020-05-05 00:23:12 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(376, {0: 1.0, 106: 1.0, 199: 0.7213, 200: 0.5078, 201: 0.8687, 202: 0.7431, 203: 0.1316, 204: 0.1933, 207: 1.0, 238: 1.0, 244: 1.0, 276: 1.0, 282: 1.0, 285: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(376, {0: 1.0, 106: 1.0, 199: 0.75, 200: 0.5078, 201: 0.5657, 202: 0.7935, 203: 0.1316, 204: 0.2577, 213: 1.0, 230: 1.0, 253: 1.0, 268: 1.0, 281: 1.0, 295: 1.0, 309: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 360: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 198: 0.0001, 199: 0.6667, 200: 0.5078, 201: 0.4343, 202: 0.7355, 203: 0.1316, 204: 0.451, 210: 1.0, 231: 1.0, 247: 1.0, 269: 1.0, 281: 1.0, 287: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 198: 0.0001, 199: 0.2759, 200: 0.2939, 201: 0.5657, 202: 0.932, 203: 0.1316, 204: 0.3221, 218: 1.0, 237: 1.0, 256: 1.0, 275: 1.0, 281: 1.0, 285: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0, 374: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 199: 0.8778, 200: 0.5078, 201: 0.404, 202: 0.8363, 203: 0.1316, 204: 0.3866, 209: 1.0, 234: 1.0, 251: 1.0, 272: 1.0, 282: 1.0, 290: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}))]
Accuracy: 0.7462548167162946
Parameters:
{Param(parent='LogisticRegression_bda6951160bf', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_bda6951160bf', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_bda6951160bf', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-05 00:23:21 
__Fitting DT_Model model..:__


# 2020-05-05 00:32:52 
__Predicting DT_Model on testSet..:__


# 2020-05-05 00:32:52 
__Evaluating DT_Model predictions..:__


# 2020-05-05 00:34:21 
__Evaluating DT_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(376, {0: 1.0, 106: 1.0, 199: 0.7213, 200: 0.5078, 201: 0.8687, 202: 0.7431, 203: 0.1316, 204: 0.1933, 207: 1.0, 238: 1.0, 244: 1.0, 276: 1.0, 282: 1.0, 285: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(376, {0: 1.0, 106: 1.0, 199: 0.75, 200: 0.5078, 201: 0.5657, 202: 0.7935, 203: 0.1316, 204: 0.2577, 213: 1.0, 230: 1.0, 253: 1.0, 268: 1.0, 281: 1.0, 295: 1.0, 309: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 360: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 198: 0.0001, 199: 0.6667, 200: 0.5078, 201: 0.4343, 202: 0.7355, 203: 0.1316, 204: 0.451, 210: 1.0, 231: 1.0, 247: 1.0, 269: 1.0, 281: 1.0, 287: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 198: 0.0001, 199: 0.2759, 200: 0.2939, 201: 0.5657, 202: 0.932, 203: 0.1316, 204: 0.3221, 218: 1.0, 237: 1.0, 256: 1.0, 275: 1.0, 281: 1.0, 285: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0, 374: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 199: 0.8778, 200: 0.5078, 201: 0.404, 202: 0.8363, 203: 0.1316, 204: 0.3866, 209: 1.0, 234: 1.0, 251: 1.0, 272: 1.0, 282: 1.0, 290: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}))]
Accuracy: 0.7194165790626545
Parameters:
{}

# 2020-05-05 00:34:33 
__Fitting RF_Model model..:__


# 2020-05-05 00:49:23 
__Predicting RF_Model on testSet..:__


# 2020-05-05 00:49:23 
__Evaluating RF_Model predictions..:__


# 2020-05-05 00:50:27 
__Evaluating RF_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=2, features=SparseVector(376, {0: 1.0, 106: 1.0, 199: 0.7213, 200: 0.5078, 201: 0.8687, 202: 0.7431, 203: 0.1316, 204: 0.1933, 207: 1.0, 238: 1.0, 244: 1.0, 276: 1.0, 282: 1.0, 285: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=2, features=SparseVector(376, {0: 1.0, 106: 1.0, 199: 0.75, 200: 0.5078, 201: 0.5657, 202: 0.7935, 203: 0.1316, 204: 0.2577, 213: 1.0, 230: 1.0, 253: 1.0, 268: 1.0, 281: 1.0, 295: 1.0, 309: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 360: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 198: 0.0001, 199: 0.6667, 200: 0.5078, 201: 0.4343, 202: 0.7355, 203: 0.1316, 204: 0.451, 210: 1.0, 231: 1.0, 247: 1.0, 269: 1.0, 281: 1.0, 287: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 198: 0.0001, 199: 0.2759, 200: 0.2939, 201: 0.5657, 202: 0.932, 203: 0.1316, 204: 0.3221, 218: 1.0, 237: 1.0, 256: 1.0, 275: 1.0, 281: 1.0, 285: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 334: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0, 374: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(376, {0: 1.0, 113: 1.0, 199: 0.8778, 200: 0.5078, 201: 0.404, 202: 0.8363, 203: 0.1316, 204: 0.3866, 209: 1.0, 234: 1.0, 251: 1.0, 272: 1.0, 282: 1.0, 290: 1.0, 313: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 350: 1.0, 353: 1.0, 356: 1.0, 359: 1.0, 362: 1.0, 364: 1.0, 367: 1.0, 370: 1.0, 373: 1.0}))]
Accuracy: 0.6408044183494136
Parameters:
{Param(parent='RandomForestClassifier_0487058e3897', name='numTrees', doc='Number of trees to train (>= 1).'): 10}