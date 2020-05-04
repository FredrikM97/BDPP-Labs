

# 2020-05-04 14:55:10 
__ML - Test - No Quantilization:__
Dont use in production!

# 2020-05-04 14:55:10 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.driver.port', '40959'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.app.id', 'local-1588604074468'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-04 14:55:29 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 14:55:46 
__Number of rows:__
2974335

# 2020-05-04 14:55:46 
__No state specified:__


# 2020-05-04 14:56:01 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2)]

# 2020-05-04 14:57:33 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2, Start_Lat_disc=71.0, Start_Lng_disc=62.0, Start_Lat_IDX=13.0, Start_Lng_IDX=94.0, Start_Lat_IDX_vec=SparseVector(99, {13: 1.0}), Start_Lng_IDX_vec=SparseVector(99, {94: 1.0}), position=SparseVector(198, {13: 1.0, 193: 1.0}))]

# 2020-05-04 14:57:33 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'City', 'State', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-04 14:57:59 
__Missing values:__
[Row(Severity=0, Start_Hour=3163, Start_Month=3163, Weather_Hour=36705, Weather_Month=36705, Distance(mi)=0, City=83, State=0, Side=0, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-04 15:00:24 
__Weather condition:__
[Row(Weather_Condition='Clear', count=808171), Row(Weather_Condition='Mostly Cloudy', count=412528), Row(Weather_Condition='Overcast', count=382480), Row(Weather_Condition='Fair', count=335289), Row(Weather_Condition='Partly Cloudy', count=295439), Row(Weather_Condition='Scattered Clouds', count=204662), Row(Weather_Condition='Light Rain', count=141073), Row(Weather_Condition='Cloudy', count=115496), Row(Weather_Condition=None, count=65932), Row(Weather_Condition='Light Snow', count=42123), Row(Weather_Condition='Haze', count=34315), Row(Weather_Condition='Rain', count=32826), Row(Weather_Condition='Fog', count=22138), Row(Weather_Condition='Heavy Rain', count=12064), Row(Weather_Condition='Light Drizzle', count=10277), Row(Weather_Condition='Light Thunderstorms and Rain', count=4928), Row(Weather_Condition='Snow', count=4796), Row(Weather_Condition='Thunderstorm', count=4438), Row(Weather_Condition='Fair / Windy', count=3759), Row(Weather_Condition='Smoke', count=3602)]
Rows removed: 103931

# 2020-05-04 15:11:14 
__Feature set size:__
2870404

__Feature vector and label:__
[Row(features=SparseVector(11731, {0: 0.0, 1: 0.3651, 2: 0.6628, 3: 0.9091, 4: 0.8983, 5: 0.0714, 6: 0.0085, 20: 1.0, 43: 1.0, 58: 1.0, 81: 1.0, 115: 1.0, 11598: 1.0, 11632: 1.0, 11636: 1.0, 11667: 1.0, 11681: 1.0, 11684: 1.0, 11687: 1.0, 11690: 1.0, 11693: 1.0, 11696: 1.0, 11699: 1.0, 11702: 1.0, 11705: 1.0, 11708: 1.0, 11711: 1.0, 11714: 1.0, 11717: 1.0, 11720: 1.0, 11723: 1.0, 11726: 1.0, 11729: 1.0}), label=3)]

# 2020-05-04 15:11:33 
__Number of rows:__
2870404

# 2020-05-04 15:19:52 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(City=11498), Row(State=49), Row(Side=3), Row(Wind_Direction=24), Row(Weather_Condition=19), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]