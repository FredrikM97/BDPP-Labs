

# 2020-05-04 01:00:17 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.driver.port', '37053'), ('spark.ui.showConsoleProgress', 'true'), ('spark.app.id', 'local-1588553983663')]

# 2020-05-04 01:00:37 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 01:00:55 
__Number of rows:__
2974335

# 2020-05-04 01:00:55 
__Specified state:__
CA

# 2020-05-04 01:01:10 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 6, 23, 10, 31, 12), Start_Lat=38.653061, Start_Lng=-121.070541, Distance(mi)=0.0, Number=None, Street='Latrobe Rd', Side='R', City='El Dorado Hills', County='El Dorado', State='CA', Zipcode='95762', Country='US', Timezone='US/Pacific', Airport_Code='KMHR', Weather_Timestamp=datetime.datetime(2016, 6, 23, 10, 46), Temperature(F)=77.0, Wind_Chill(F)=None, Humidity(%)=34.0, Pressure(in)=30.02, Visibility(mi)=10.0, Wind_Direction='SW', Wind_Speed(mph)=3.5, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=3, Start_Month=6, Weather_Hour=3, Weather_Month=6)]

# 2020-05-04 01:02:42 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 6, 23, 10, 31, 12), Start_Lat=38.653061, Start_Lng=-121.070541, Distance(mi)=0.0, Number=None, Street='Latrobe Rd', Side='R', City='El Dorado Hills', County='El Dorado', State='CA', Zipcode='95762', Country='US', Timezone='US/Pacific', Airport_Code='KMHR', Weather_Timestamp=datetime.datetime(2016, 6, 23, 10, 46), Temperature(F)=77.0, Wind_Chill(F)=None, Humidity(%)=34.0, Pressure(in)=30.02, Visibility(mi)=10.0, Wind_Direction='SW', Wind_Speed(mph)=3.5, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=3, Start_Month=6, Weather_Hour=3, Weather_Month=6, Start_Lat_disc=95.0, Start_Lng_disc=35.0, Start_Lat_IDX=6.0, Start_Lng_IDX=33.0, Start_Lat_IDX_vec=SparseVector(99, {6: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {33: 1.0}), position=SparseVector(198, {6: 1.0, 132: 1.0}))]

# 2020-05-04 01:02:42 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-04 01:03:03 
__Missing values:__
[Row(Severity=0, Start_Hour=205, Start_Month=205, Weather_Hour=9397, Weather_Month=9397, position=0, Distance(mi)=0, Side=0, Temperature(F)=15125, Wind_Chill(F)=471819, Humidity(%)=16314, Pressure(in)=11242, Visibility(mi)=13196, Wind_Direction=12148, Wind_Speed(mph)=128806, Weather_Condition=12881, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=6, Civil_Twilight=6, Nautical_Twilight=6, Astronomical_Twilight=6)]

# 2020-05-04 01:03:22 
__Missing values:__
[Row(Severity=0, Start_Hour=205, Start_Month=205, Weather_Hour=9397, Weather_Month=9397, position=0, Distance(mi)=0, Side=0, Temperature(F)=15125, Wind_Chill(F)=471819, Humidity(%)=16314, Pressure(in)=11242, Visibility(mi)=13196, Wind_Direction=12148, Wind_Speed(mph)=128806, Weather_Condition=12881, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=6, Civil_Twilight=6, Nautical_Twilight=6, Astronomical_Twilight=6)]

# 2020-05-04 01:05:49 
__Weather condition:__
[Row(Weather_Condition='Clear', count=253070), Row(Weather_Condition='Fair', count=103016), Row(Weather_Condition='Mostly Cloudy', count=60440), Row(Weather_Condition='Partly Cloudy', count=59555), Row(Weather_Condition='Overcast', count=58472), Row(Weather_Condition='Scattered Clouds', count=29356), Row(Weather_Condition='Cloudy', count=24959), Row(Weather_Condition='Haze', count=21830), Row(Weather_Condition='Light Rain', count=20437), Row(Weather_Condition=None, count=12881), Row(Weather_Condition='Rain', count=6438), Row(Weather_Condition='Fog', count=4138), Row(Weather_Condition='Heavy Rain', count=2246), Row(Weather_Condition='Smoke', count=1923), Row(Weather_Condition='Fair / Windy', count=1244)]
Rows removed: 16080

# 2020-05-04 01:15:07 
__Feature set size:__
647124

__Feature vector and label:__
[Row(features=SparseVector(375, {6: 1.0, 132: 1.0, 199: 0.6796, 200: 0.6379, 201: 0.3333, 202: 0.9078, 203: 0.0714, 204: 0.0043, 216: 1.0, 237: 1.0, 251: 1.0, 275: 1.0, 281: 1.0, 291: 1.0, 310: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}), label=2)]

# 2020-05-04 01:15:25 
__Number of rows:__
647124

# 2020-05-04 01:23:06 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(Side=3), Row(Wind_Direction=24), Row(Weather_Condition=14), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2), Row(position=3693)]

# 2020-05-04 01:24:18 
__PCA - Feature variance:__
Top 50:
[0.14062098 0.0329705  0.02612442 0.02464095 0.02313293 0.02028574
 0.01939677 0.0191976  0.01880045 0.0179059  0.01684292 0.01659278
 0.01560103 0.01496458 0.01473948 0.01432929 0.01316542 0.0125107
 0.01198642 0.01168148 0.01123894 0.01081102 0.01036433 0.01015148
 0.0100888  0.00943579 0.00937402 0.00901781 0.00893319 0.00866174
 0.00838808 0.00810419 0.00802553 0.00734117 0.00679608 0.00671823
 0.00633214 0.00573477 0.00570821 0.00566625 0.00545814 0.00516296
 0.0050209  0.00488568 0.00479595 0.00459745 0.00435788 0.00428287
 0.00411806 0.00385347]
Number of items: 250
Sum of variance: 0.972441197930136

# 2020-05-04 01:25:27 
__Top selected features according to ChiSqSelector:__
[0, 1, 2, 6, 7, 8, 9, 11, 13, 14, 15, 17, 18, 20, 21, 22, 23, 24, 25, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 39, 40, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 72, 73, 74, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 94, 95, 96, 97, 98, 100, 102, 103, 105, 106, 107, 108, 109, 110, 112, 113, 114, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 150, 151, 152, 153, 155, 156, 157, 159, 160, 161, 162, 164, 165, 166, 168, 171, 174, 175, 176, 177, 180, 183, 185, 186, 188, 189, 190, 191, 193, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 213, 214, 216, 217, 218, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 243, 244, 246, 247, 251, 252, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273, 274, 275, 276, 277, 278, 279, 281, 282, 285, 286, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 300, 301, 302, 304, 307, 308, 309, 310, 311, 312, 314, 315, 316, 317, 320, 323, 325, 326, 331, 332, 334]
Number of features: 250
Example data:
[Row(features=SparseVector(375, {6: 1.0, 132: 1.0, 199: 0.6796, 200: 0.6379, 201: 0.3333, 202: 0.9078, 203: 0.0714, 204: 0.0043, 216: 1.0, 237: 1.0, 251: 1.0, 275: 1.0, 281: 1.0, 291: 1.0, 310: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}), label=2, selectedFeatures=SparseVector(250, {3: 1.0, 103: 1.0, 150: 0.6796, 151: 0.6379, 152: 0.3333, 153: 0.9078, 154: 0.0714, 155: 0.0043, 164: 1.0, 182: 1.0, 191: 1.0, 209: 1.0, 214: 1.0, 221: 1.0, 236: 1.0, 245: 1.0, 247: 1.0, 249: 1.0})), Row(features=SparseVector(375, {31: 1.0, 135: 1.0, 198: 0.0, 199: 0.4825, 200: 0.4676, 201: 0.7071, 202: 0.9099, 203: 0.0714, 204: 0.0098, 207: 1.0, 240: 1.0, 247: 1.0, 278: 1.0, 281: 1.0, 293: 1.0, 310: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}), label=3, selectedFeatures=SparseVector(250, {22: 1.0, 149: 0.0, 150: 0.4825, 151: 0.4676, 152: 0.7071, 153: 0.9099, 154: 0.0714, 155: 0.0098, 158: 1.0, 185: 1.0, 190: 1.0, 212: 1.0, 214: 1.0, 223: 1.0, 236: 1.0, 245: 1.0, 247: 1.0, 249: 1.0})), Row(features=SparseVector(375, {80: 1.0, 167: 1.0, 199: 0.7298, 200: 0.6379, 201: 0.2424, 202: 0.9056, 203: 0.0714, 204: 0.0098, 207: 1.0, 235: 1.0, 244: 1.0, 273: 1.0, 281: 1.0, 290: 1.0, 310: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}), label=2, selectedFeatures=SparseVector(250, {150: 0.7298, 151: 0.6379, 152: 0.2424, 153: 0.9056, 154: 0.0714, 155: 0.0098, 158: 1.0, 180: 1.0, 188: 1.0, 207: 1.0, 214: 1.0, 220: 1.0, 236: 1.0, 245: 1.0, 247: 1.0, 249: 1.0})), Row(features=SparseVector(375, {47: 1.0, 167: 1.0, 199: 0.7298, 200: 0.6379, 201: 0.2424, 202: 0.9056, 203: 0.0714, 204: 0.0098, 207: 1.0, 235: 1.0, 244: 1.0, 273: 1.0, 281: 1.0, 290: 1.0, 310: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}), label=2, selectedFeatures=SparseVector(250, {36: 1.0, 150: 0.7298, 151: 0.6379, 152: 0.2424, 153: 0.9056, 154: 0.0714, 155: 0.0098, 158: 1.0, 180: 1.0, 188: 1.0, 207: 1.0, 214: 1.0, 220: 1.0, 236: 1.0, 245: 1.0, 247: 1.0, 249: 1.0})), Row(features=SparseVector(375, {67: 1.0, 110: 1.0, 199: 0.6478, 200: 0.6379, 201: 0.4545, 202: 0.9075, 203: 0.0714, 204: 0.0098, 207: 1.0, 235: 1.0, 244: 1.0, 273: 1.0, 281: 1.0, 293: 1.0, 312: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}), label=3, selectedFeatures=SparseVector(250, {54: 1.0, 86: 1.0, 150: 0.6478, 151: 0.6379, 152: 0.4545, 153: 0.9075, 154: 0.0714, 155: 0.0098, 158: 1.0, 180: 1.0, 188: 1.0, 207: 1.0, 214: 1.0, 223: 1.0, 238: 1.0, 245: 1.0, 247: 1.0, 249: 1.0}))]

# 2020-05-04 01:26:27 
__Fitting LR_Model model..:__


# 2020-05-04 01:38:30 
__Predicting LR_Model on testSet..:__


# 2020-05-04 01:38:30 
__Evaluating LR_Model predictions..:__


# 2020-05-04 01:40:06 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6097, 200: 0.6379, 201: 0.697, 202: 0.9044, 203: 0.0714, 204: 0.0196, 207: 1.0, 230: 1.0, 244: 1.0, 268: 1.0, 281: 1.0, 291: 1.0, 312: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 338: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.4882, 200: 0.6379, 201: 0.6263, 202: 0.9215, 203: 0.0714, 204: 0.0056, 209: 1.0, 232: 1.0, 249: 1.0, 270: 1.0, 281: 1.0, 295: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=3.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6097, 200: 0.6379, 201: 0.596, 202: 0.912, 203: 0.0714, 204: 0.0154, 212: 1.0, 239: 1.0, 250: 1.0, 277: 1.0, 281: 1.0, 286: 1.0, 315: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.5779, 200: 0.6379, 201: 0.7475, 202: 0.9117, 203: 0.0714, 204: 0.0084, 213: 1.0, 230: 1.0, 249: 1.0, 268: 1.0, 281: 1.0, 285: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6421, 200: 0.6379, 201: 0.6263, 202: 0.9108, 203: 0.0714, 204: 0.0098, 214: 1.0, 233: 1.0, 253: 1.0, 271: 1.0, 281: 1.0, 286: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}))]
Accuracy: 0.6726110646627255
Parameters:
{Param(parent='LogisticRegression_fd162083331a', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_fd162083331a', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_fd162083331a', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-04 01:40:20 
__Fitting DT_Model model..:__


# 2020-05-04 01:54:54 
__Predicting DT_Model on testSet..:__


# 2020-05-04 01:54:54 
__Evaluating DT_Model predictions..:__


# 2020-05-04 01:56:30 
__Evaluating DT_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6097, 200: 0.6379, 201: 0.697, 202: 0.9044, 203: 0.0714, 204: 0.0196, 207: 1.0, 230: 1.0, 244: 1.0, 268: 1.0, 281: 1.0, 291: 1.0, 312: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 338: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.4882, 200: 0.6379, 201: 0.6263, 202: 0.9215, 203: 0.0714, 204: 0.0056, 209: 1.0, 232: 1.0, 249: 1.0, 270: 1.0, 281: 1.0, 295: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6097, 200: 0.6379, 201: 0.596, 202: 0.912, 203: 0.0714, 204: 0.0154, 212: 1.0, 239: 1.0, 250: 1.0, 277: 1.0, 281: 1.0, 286: 1.0, 315: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.5779, 200: 0.6379, 201: 0.7475, 202: 0.9117, 203: 0.0714, 204: 0.0084, 213: 1.0, 230: 1.0, 249: 1.0, 268: 1.0, 281: 1.0, 285: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6421, 200: 0.6379, 201: 0.6263, 202: 0.9108, 203: 0.0714, 204: 0.0098, 214: 1.0, 233: 1.0, 253: 1.0, 271: 1.0, 281: 1.0, 286: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}))]
Accuracy: 0.5464271085561828
Parameters:
{}

# 2020-05-04 01:56:44 
__Fitting RF_Model model..:__


# 2020-05-04 02:22:38 
__Predicting RF_Model on testSet..:__


# 2020-05-04 02:22:38 
__Evaluating RF_Model predictions..:__


# 2020-05-04 02:24:14 
__Evaluating RF_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6097, 200: 0.6379, 201: 0.697, 202: 0.9044, 203: 0.0714, 204: 0.0196, 207: 1.0, 230: 1.0, 244: 1.0, 268: 1.0, 281: 1.0, 291: 1.0, 312: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 338: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.4882, 200: 0.6379, 201: 0.6263, 202: 0.9215, 203: 0.0714, 204: 0.0056, 209: 1.0, 232: 1.0, 249: 1.0, 270: 1.0, 281: 1.0, 295: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6097, 200: 0.6379, 201: 0.596, 202: 0.912, 203: 0.0714, 204: 0.0154, 212: 1.0, 239: 1.0, 250: 1.0, 277: 1.0, 281: 1.0, 286: 1.0, 315: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.5779, 200: 0.6379, 201: 0.7475, 202: 0.9117, 203: 0.0714, 204: 0.0084, 213: 1.0, 230: 1.0, 249: 1.0, 268: 1.0, 281: 1.0, 285: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(375, {0: 1.0, 105: 1.0, 198: 0.0, 199: 0.6421, 200: 0.6379, 201: 0.6263, 202: 0.9108, 203: 0.0714, 204: 0.0098, 214: 1.0, 233: 1.0, 253: 1.0, 271: 1.0, 281: 1.0, 286: 1.0, 313: 1.0, 325: 1.0, 328: 1.0, 331: 1.0, 334: 1.0, 337: 1.0, 340: 1.0, 343: 1.0, 346: 1.0, 349: 1.0, 352: 1.0, 355: 1.0, 358: 1.0, 361: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0}))]
Accuracy: 0.5411377417434503
Parameters:
{Param(parent='RandomForestClassifier_1c63fc9b5c89', name='numTrees', doc='Number of trees to train (>= 1).'): 10}