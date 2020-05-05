

# 2020-05-05 02:07:42 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.app.id', 'local-1588644394139'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.port', '45469'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-05 02:07:43 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-05 02:07:59 
__Number of rows:__
2974335

# 2020-05-05 02:07:59 
__Specified state:__
CA

# 2020-05-05 02:08:13 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 6, 23, 10, 31, 12), Start_Lat=38.653061, Start_Lng=-121.070541, Distance(mi)=0.0, Number=None, Street='Latrobe Rd', Side='R', City='El Dorado Hills', County='El Dorado', State='CA', Zipcode='95762', Country='US', Timezone='US/Pacific', Airport_Code='KMHR', Weather_Timestamp=datetime.datetime(2016, 6, 23, 10, 46), Temperature(F)=77.0, Wind_Chill(F)=None, Humidity(%)=34.0, Pressure(in)=30.02, Visibility(mi)=10.0, Wind_Direction='SW', Wind_Speed(mph)=3.5, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=3, Start_Month=6, Weather_Hour=3, Weather_Month=6)]