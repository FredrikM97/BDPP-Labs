

# 2020-05-04 15:56:37 
__ML - Test - No Quantilization:__
Dont use in production!

# 2020-05-04 15:56:37 
__New Spark session:__
[('spark.driver.extraClassPath', '/opt/conda/lib/python3.7/site-packages/sparkmonitor/listener.jar'), ('SPARKMONITOR_UI_HOST', '192.168.1.228'), ('spark.driver.port', '45665'), ('spark.executor.id', 'driver'), ('spark.driver.host', 'localhost'), ('spark.app.id', 'local-1588607762117'), ('spark.app.name', 'Spark Project'), ('spark.executor.cores', '4'), ('executor-memory', '6'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.num.executors', '6'), ('spark.kryoserializer.buffer.max', '10'), ('spark.extraListeners', 'sparkmonitor.listener.JupyterSparkMonitorListener'), ('spark.rdd.compress', 'True'), ('spark.driver.memory', '8g'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.memory.fraction', '.6'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true')]

# 2020-05-04 15:56:57 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-04 15:57:15 
__Number of rows:__
2974335

# 2020-05-04 15:57:15 
__No state specified:__


# 2020-05-04 15:57:30 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night', Start_Hour=0, Start_Month=2, Weather_Hour=0, Weather_Month=2)]