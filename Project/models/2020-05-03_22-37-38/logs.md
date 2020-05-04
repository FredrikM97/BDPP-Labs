

# 2020-05-03 22:38:14 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.driver.port', '38559'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.app.id', 'local-1588545460284'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-03 22:38:33 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-03 22:38:51 
__Number of rows:__
297402

# 2020-05-03 22:38:51 
__Specified state:__
CA

# 2020-05-03 22:39:06 
__Dataset after modifying UTC timestamp:__
[Row(TMC=245.0, Severity=3, Start_Time=datetime.datetime(2016, 4, 5, 15, 57, 10), Start_Lat=33.913029, Start_Lng=-118.125389, Distance(mi)=0.0, Number=None, Street='Bellflower Blvd', Side='R', City='Downey', County='Los Angeles', State='CA', Zipcode='90242', Country='US', Timezone='US/Pacific', Airport_Code='KLGB', Weather_Timestamp=datetime.datetime(2016, 4, 5, 15, 53), Temperature(F)=82.9, Wind_Chill(F)=None, Humidity(%)=24.0, Pressure(in)=29.97, Visibility(mi)=10.0, Wind_Direction='South', Wind_Speed(mph)=6.9, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=8, Start_Month=4, Weather_Hour=8, Weather_Month=4)]

# 2020-05-03 22:40:39 
__Dataset after adding quantiles:__
[Row(TMC=245.0, Severity=3, Start_Time=datetime.datetime(2016, 4, 5, 15, 57, 10), Start_Lat=33.913029, Start_Lng=-118.125389, Distance(mi)=0.0, Number=None, Street='Bellflower Blvd', Side='R', City='Downey', County='Los Angeles', State='CA', Zipcode='90242', Country='US', Timezone='US/Pacific', Airport_Code='KLGB', Weather_Timestamp=datetime.datetime(2016, 4, 5, 15, 53), Temperature(F)=82.9, Wind_Chill(F)=None, Humidity(%)=24.0, Pressure(in)=29.97, Visibility(mi)=10.0, Wind_Direction='South', Wind_Speed(mph)=6.9, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=8, Start_Month=4, Weather_Hour=8, Weather_Month=4, Start_Lat_disc=20.0, Start_Lng_disc=66.0, Start_Lat_IDX=57.0, Start_Lng_IDX=66.0, Start_Lat_IDX_vec=SparseVector(99, {57: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {66: 1.0}), position=SparseVector(198, {57: 1.0, 165: 1.0}))]

# 2020-05-03 22:40:39 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-03 22:40:59 
__Missing values:__
[Row(Severity=0, Start_Hour=23, Start_Month=23, Weather_Hour=928, Weather_Month=928, position=0, Distance(mi)=0, Side=0, Temperature(F)=1508, Wind_Chill(F)=47336, Humidity(%)=1626, Pressure(in)=1095, Visibility(mi)=1302, Wind_Direction=1199, Wind_Speed(mph)=12937, Weather_Condition=1253, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=0, Civil_Twilight=0, Nautical_Twilight=0, Astronomical_Twilight=0)]

# 2020-05-03 22:41:18 
__Missing values:__
[Row(Severity=0, Start_Hour=23, Start_Month=23, Weather_Hour=928, Weather_Month=928, position=0, Distance(mi)=0, Side=0, Temperature(F)=1508, Wind_Chill(F)=47336, Humidity(%)=1626, Pressure(in)=1095, Visibility(mi)=1302, Wind_Direction=1199, Wind_Speed(mph)=12937, Weather_Condition=1253, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=0, Civil_Twilight=0, Nautical_Twilight=0, Astronomical_Twilight=0)]

# 2020-05-03 22:43:48 
__Weather condition:__
[Row(Weather_Condition='Clear', count=25365), Row(Weather_Condition='Fair', count=10205), Row(Weather_Condition='Mostly Cloudy', count=6056), Row(Weather_Condition='Overcast', count=5934), Row(Weather_Condition='Partly Cloudy', count=5866), Row(Weather_Condition='Scattered Clouds', count=2888), Row(Weather_Condition='Cloudy', count=2554), Row(Weather_Condition='Haze', count=2249), Row(Weather_Condition='Light Rain', count=2070), Row(Weather_Condition=None, count=1253), Row(Weather_Condition='Rain', count=647), Row(Weather_Condition='Fog', count=401), Row(Weather_Condition='Heavy Rain', count=225), Row(Weather_Condition='Smoke', count=195), Row(Weather_Condition='Fair / Windy', count=120)]
Rows removed: 1592

# 2020-05-03 22:53:21 
__Feature set size:__
64775

__Feature vector and label:__
[Row(features=SparseVector(374, {57: 1.0, 165: 1.0, 199: 0.7383, 200: 0.5599, 201: 0.2323, 202: 0.9761, 203: 0.125, 204: 0.0084, 207: 1.0, 235: 1.0, 244: 1.0, 273: 1.0, 281: 1.0, 293: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}), label=3)]

# 2020-05-03 22:53:39 
__Number of rows:__
64775

# 2020-05-03 23:01:52 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(Side=2), Row(Wind_Direction=24), Row(Weather_Condition=14), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2), Row(position=2765)]

# 2020-05-03 23:02:51 
__PCA - Feature variance:__
Top 50:
[0.14037738 0.03285348 0.02607584 0.02466152 0.02275149 0.02035519
 0.01963028 0.01933186 0.01885241 0.01821285 0.01685931 0.01651596
 0.01567224 0.01500666 0.01466128 0.01443375 0.01317393 0.0125247
 0.01204053 0.01173031 0.0112018  0.01084424 0.01044339 0.01016612
 0.00997856 0.00943219 0.00932183 0.00906002 0.00895639 0.00857022
 0.00842774 0.00815491 0.0079836  0.00731973 0.00686601 0.00673965
 0.00636585 0.00579052 0.00571454 0.00567805 0.00546248 0.00518956
 0.00512702 0.00486473 0.00477337 0.00452355 0.00437144 0.00429224
 0.00411031 0.00386909]
Number of items: 200
Sum of variance: 0.929249937844132

# 2020-05-03 23:03:28 
__Top selected features according to ChiSqSelector:__
[0, 6, 7, 8, 10, 12, 15, 17, 19, 20, 25, 31, 33, 34, 40, 47, 48, 50, 53, 67, 69, 73, 95, 96, 97, 103, 106, 114, 119, 121, 122, 126, 132, 134, 135, 138, 143, 153, 157, 161, 162, 163, 170, 173, 175, 182, 185, 187, 191, 198, 199, 200, 201, 202, 204, 226, 227, 230, 231, 232, 237, 243, 263, 266, 268, 269, 270, 275, 281, 282, 284, 285, 286, 297, 301, 303, 306, 309, 310, 312, 315, 330, 331, 351, 352, 357, 358, 362, 363, 365, 366, 368, 369, 371, 372, 120, 307, 123, 5, 139, 228, 265, 128, 238, 276, 45, 58, 205, 156, 273, 46, 314, 235, 239, 13, 37, 277, 125, 43, 207, 75, 150, 287, 104, 32, 178, 108, 144, 93, 244, 189, 292, 206, 183, 98, 52, 274, 236, 111, 295, 90, 319, 68, 291, 83, 278, 240, 109, 154, 222, 102, 57, 190, 133, 221, 60, 316, 89, 92, 241, 78, 256, 279, 127, 141, 22, 151, 101, 300, 65, 66, 77, 246, 220, 3, 23, 174, 296, 158, 85, 100, 290, 110, 29, 131, 196, 166, 14, 213, 184, 258, 26, 62, 324, 325, 59, 247, 261, 84, 225]
Number of features: 200
Example data:
[Row(features=SparseVector(374, {57: 1.0, 165: 1.0, 199: 0.7383, 200: 0.5599, 201: 0.2323, 202: 0.9761, 203: 0.125, 204: 0.0084, 207: 1.0, 235: 1.0, 244: 1.0, 273: 1.0, 281: 1.0, 293: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}), label=3, selectedFeatures=SparseVector(200, {33: 1.0, 114: 0.7383, 115: 0.5599, 116: 0.2323, 117: 0.9761, 118: 0.0084, 121: 1.0, 133: 1.0, 141: 1.0, 153: 1.0, 160: 1.0, 177: 1.0, 184: 1.0, 186: 1.0, 188: 1.0, 190: 1.0, 192: 1.0, 194: 1.0, 196: 1.0, 198: 1.0})), Row(features=SparseVector(374, {6: 1.0, 106: 1.0, 198: 0.0001, 199: 0.453, 200: 0.5599, 201: 0.5152, 202: 0.9801, 203: 0.125, 204: 0.0084, 207: 1.0, 240: 1.0, 246: 1.0, 278: 1.0, 281: 1.0, 293: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 337: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}), label=2, selectedFeatures=SparseVector(200, {3: 1.0, 63: 1.0, 113: 0.0001, 114: 0.453, 115: 0.5599, 116: 0.5152, 117: 0.9801, 118: 0.0084, 121: 1.0, 138: 1.0, 142: 1.0, 158: 1.0, 160: 1.0, 177: 1.0, 184: 1.0, 186: 1.0, 188: 1.0, 190: 1.0, 192: 1.0, 194: 1.0, 196: 1.0, 198: 1.0})), Row(features=SparseVector(374, {57: 1.0, 118: 1.0, 199: 0.7475, 200: 0.5599, 201: 0.2626, 202: 0.9754, 203: 0.125, 204: 0.0084, 205: 1.0, 235: 1.0, 243: 1.0, 273: 1.0, 281: 1.0, 288: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}), label=3, selectedFeatures=SparseVector(200, {33: 1.0, 114: 0.7475, 115: 0.5599, 116: 0.2626, 117: 0.9754, 118: 0.0084, 119: 1.0, 133: 1.0, 140: 1.0, 153: 1.0, 160: 1.0, 177: 1.0, 184: 1.0, 186: 1.0, 188: 1.0, 190: 1.0, 192: 1.0, 194: 1.0, 196: 1.0, 198: 1.0})), Row(features=SparseVector(374, {52: 1.0, 102: 1.0, 199: 0.6628, 200: 0.5599, 201: 0.3232, 202: 0.9761, 203: 0.125, 204: 0.0098, 205: 1.0, 235: 1.0, 243: 1.0, 273: 1.0, 282: 1.0, 285: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 331: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 343: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}), label=2, selectedFeatures=SparseVector(200, {31: 1.0, 60: 1.0, 114: 0.6628, 115: 0.5599, 116: 0.3232, 117: 0.9761, 118: 0.0098, 119: 1.0, 133: 1.0, 140: 1.0, 153: 1.0, 161: 1.0, 163: 1.0, 177: 1.0, 184: 1.0, 187: 1.0, 188: 1.0, 190: 1.0, 192: 1.0, 194: 1.0, 196: 1.0, 198: 1.0})), Row(features=SparseVector(374, {74: 1.0, 168: 1.0, 199: 0.8062, 200: 0.5599, 201: 0.1717, 202: 0.9754, 203: 0.125, 204: 0.0182, 205: 1.0, 235: 1.0, 243: 1.0, 273: 1.0, 281: 1.0, 289: 1.0, 311: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}), label=2, selectedFeatures=SparseVector(200, {114: 0.8062, 115: 0.5599, 116: 0.1717, 117: 0.9754, 118: 0.0182, 119: 1.0, 133: 1.0, 140: 1.0, 153: 1.0, 160: 1.0, 184: 1.0, 186: 1.0, 188: 1.0, 190: 1.0, 192: 1.0, 194: 1.0, 196: 1.0, 198: 1.0}))]

# 2020-05-03 23:04:12 
__Fitting LR_Model model..:__


# 2020-05-03 23:13:18 
__Predicting LR_Model on testSet..:__


# 2020-05-03 23:13:18 
__Evaluating LR_Model predictions..:__


# 2020-05-03 23:14:25 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0429, 199: 0.4883, 200: 0.5599, 201: 0.5152, 202: 0.9776, 203: 0.125, 204: 0.0112, 209: 1.0, 241: 1.0, 250: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.5872, 200: 0.5599, 201: 0.5556, 202: 0.9797, 203: 0.125, 204: 0.0043, 214: 1.0, 230: 1.0, 249: 1.0, 268: 1.0, 281: 1.0, 296: 1.0, 312: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.4958, 200: 0.5599, 201: 1.0, 202: 0.9787, 203: 0.0375, 204: 0.007, 218: 1.0, 232: 1.0, 256: 1.0, 270: 1.0, 281: 1.0, 294: 1.0, 312: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=3.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.4471, 200: 0.5599, 201: 0.8687, 202: 0.9783, 203: 0.0375, 204: 0.014, 218: 1.0, 233: 1.0, 256: 1.0, 271: 1.0, 281: 1.0, 288: 1.0, 318: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 199: 0.7148, 200: 0.5599, 201: 0.4242, 202: 0.9721, 203: 0.125, 204: 0.0168, 206: 1.0, 237: 1.0, 243: 1.0, 275: 1.0, 281: 1.0, 285: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}))]
Accuracy: 0.6589217691221422
Parameters:
{Param(parent='LogisticRegression_461d296745c9', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_461d296745c9', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_461d296745c9', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-03 23:14:34 
__Fitting DT_Model model..:__


# 2020-05-03 23:24:11 
__Predicting DT_Model on testSet..:__


# 2020-05-03 23:24:11 
__Evaluating DT_Model predictions..:__


# 2020-05-03 23:25:19 
__Evaluating DT_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0429, 199: 0.4883, 200: 0.5599, 201: 0.5152, 202: 0.9776, 203: 0.125, 204: 0.0112, 209: 1.0, 241: 1.0, 250: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.5872, 200: 0.5599, 201: 0.5556, 202: 0.9797, 203: 0.125, 204: 0.0043, 214: 1.0, 230: 1.0, 249: 1.0, 268: 1.0, 281: 1.0, 296: 1.0, 312: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.4958, 200: 0.5599, 201: 1.0, 202: 0.9787, 203: 0.0375, 204: 0.007, 218: 1.0, 232: 1.0, 256: 1.0, 270: 1.0, 281: 1.0, 294: 1.0, 312: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.4471, 200: 0.5599, 201: 0.8687, 202: 0.9783, 203: 0.0375, 204: 0.014, 218: 1.0, 233: 1.0, 256: 1.0, 271: 1.0, 281: 1.0, 288: 1.0, 318: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 199: 0.7148, 200: 0.5599, 201: 0.4242, 202: 0.9721, 203: 0.125, 204: 0.0168, 206: 1.0, 237: 1.0, 243: 1.0, 275: 1.0, 281: 1.0, 285: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}))]
Accuracy: 0.5426858453307785
Parameters:
{}

# 2020-05-03 23:25:28 
__Fitting RF_Model model..:__


# 2020-05-03 23:37:28 
__Predicting RF_Model on testSet..:__


# 2020-05-03 23:37:28 
__Evaluating RF_Model predictions..:__


# 2020-05-03 23:38:36 
__Evaluating RF_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0429, 199: 0.4883, 200: 0.5599, 201: 0.5152, 202: 0.9776, 203: 0.125, 204: 0.0112, 209: 1.0, 241: 1.0, 250: 1.0, 279: 1.0, 281: 1.0, 288: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.5872, 200: 0.5599, 201: 0.5556, 202: 0.9797, 203: 0.125, 204: 0.0043, 214: 1.0, 230: 1.0, 249: 1.0, 268: 1.0, 281: 1.0, 296: 1.0, 312: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.4958, 200: 0.5599, 201: 1.0, 202: 0.9787, 203: 0.0375, 204: 0.007, 218: 1.0, 232: 1.0, 256: 1.0, 270: 1.0, 281: 1.0, 294: 1.0, 312: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 198: 0.0001, 199: 0.4471, 200: 0.5599, 201: 0.8687, 202: 0.9783, 203: 0.0375, 204: 0.014, 218: 1.0, 233: 1.0, 256: 1.0, 271: 1.0, 281: 1.0, 288: 1.0, 318: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 363: 1.0, 366: 1.0, 369: 1.0, 372: 1.0})), Row(prediction=2.0, label=3, features=SparseVector(374, {0: 1.0, 108: 1.0, 199: 0.7148, 200: 0.5599, 201: 0.4242, 202: 0.9721, 203: 0.125, 204: 0.0168, 206: 1.0, 237: 1.0, 243: 1.0, 275: 1.0, 281: 1.0, 285: 1.0, 309: 1.0, 324: 1.0, 327: 1.0, 330: 1.0, 333: 1.0, 336: 1.0, 339: 1.0, 342: 1.0, 345: 1.0, 348: 1.0, 351: 1.0, 354: 1.0, 357: 1.0, 360: 1.0, 362: 1.0, 365: 1.0, 368: 1.0, 371: 1.0}))]
Accuracy: 0.5429333376374423
Parameters:
{Param(parent='RandomForestClassifier_29fed1b45df2', name='numTrees', doc='Number of trees to train (>= 1).'): 10}