

# 2020-05-06 01:09:58 
__New Spark session:__
[('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.executor.id', 'driver'), ('spark.driver.port', '39677'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.driver.host', '97901d576ca5'), ('spark.kryoserializer.buffer.max', '10'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.app.id', 'local-1588727361250'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-06 01:10:00 
__Number of rows:__
2974335

# 2020-05-06 01:10:00 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-06 01:10:02 
__Data analysis:__
Rows: 2974335
Columns 43
root
 |-- TMC: double (nullable = true)
 |-- Severity: integer (nullable = true)
 |-- Start_Time: timestamp (nullable = true)
 |-- Start_Lat: double (nullable = true)
 |-- Start_Lng: double (nullable = true)
 |-- Distance(mi): double (nullable = true)
 |-- Number: double (nullable = true)
 |-- Street: string (nullable = true)
 |-- Side: string (nullable = true)
 |-- City: string (nullable = true)
 |-- County: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Timezone: string (nullable = true)
 |-- Airport_Code: string (nullable = true)
 |-- Weather_Timestamp: timestamp (nullable = true)
 |-- Temperature(F): double (nullable = true)
 |-- Wind_Chill(F): double (nullable = true)
 |-- Humidity(%): double (nullable = true)
 |-- Pressure(in): double (nullable = true)
 |-- Visibility(mi): double (nullable = true)
 |-- Wind_Direction: string (nullable = true)
 |-- Wind_Speed(mph): double (nullable = true)
 |-- Precipitation(in): double (nullable = true)
 |-- Weather_Condition: string (nullable = true)
 |-- Amenity: string (nullable = true)
 |-- Bump: string (nullable = true)
 |-- Crossing: string (nullable = true)
 |-- Give_Way: string (nullable = true)
 |-- Junction: string (nullable = true)
 |-- No_Exit: string (nullable = true)
 |-- Railway: string (nullable = true)
 |-- Roundabout: string (nullable = true)
 |-- Station: string (nullable = true)
 |-- Stop: string (nullable = true)
 |-- Traffic_Calming: string (nullable = true)
 |-- Traffic_Signal: string (nullable = true)
 |-- Turning_Loop: string (nullable = true)
 |-- Sunrise_Sunset: string (nullable = true)
 |-- Civil_Twilight: string (nullable = true)
 |-- Nautical_Twilight: string (nullable = true)
 |-- Astronomical_Twilight: string (nullable = true)
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night')]

# 2020-05-06 01:10:29 
__Missing values:__
[Row(TMC=728071, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=0, Number=1917605, Street=0, Side=0, City=83, County=0, State=0, Zipcode=880, Country=0, Timezone=3163, Airport_Code=5691, Weather_Timestamp=36705, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Precipitation(in)=1998358, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-06 01:13:00 
__Categorical values:__
[Row(Street=160715), Row(Side=3), Row(City=11685), Row(County=1713), Row(State=49), Row(Zipcode=377152), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1995), Row(Wind_Direction=24), Row(Weather_Condition=120), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-06 01:17:20 
__Correlation matrix:__
DenseMatrix([[ 1.00000000e+00, -3.29968079e-02, -4.23709318e-02,
               6.48521350e-02,  4.88102771e-02,  2.89427459e-02,
               3.07391705e-02, -6.70493470e-03,  4.59513996e-03,
               2.21819466e-02, -1.61669692e-03, -1.80310455e-03],
             [-3.29968079e-02,  1.00000000e+00, -5.22492702e-03,
               5.01751676e-02, -3.17558810e-02, -4.68351247e-01,
              -4.69159899e-01,  9.79378608e-02, -1.18202158e-01,
              -1.54998940e-01,  9.15359600e-02,  5.03876348e-03],
             [-4.23709318e-02, -5.22492702e-03,  1.00000000e+00,
              -7.53412624e-03, -1.85446020e-01, -6.29347088e-02,
              -7.17865446e-02,  1.97789478e-01,  2.74148682e-01,
              -8.96066993e-02,  3.69653763e-02,  1.71422780e-02],
             [ 6.48521350e-02,  5.01751676e-02, -7.53412624e-03,
               1.00000000e+00,  2.39536246e-02, -2.59661162e-02,
              -2.52581670e-02,  1.25991397e-02, -4.31332807e-02,
              -1.74274857e-03, -3.02094605e-05,  5.51084719e-04],
             [ 4.88102771e-02, -3.17558810e-02, -1.85446020e-01,
               2.39536246e-02,  1.00000000e+00,  9.15996465e-03,
               1.14585147e-02, -5.41486806e-03, -3.01287122e-02,
               1.54279877e-02, -1.55270941e-02, -3.57307853e-03],
             [ 2.89427459e-02, -4.68351247e-01, -6.29347088e-02,
              -2.59661162e-02,  9.15996465e-03,  1.00000000e+00,
               9.94635527e-01, -4.33436493e-01, -5.74036079e-02,
               3.59398479e-01, -5.70376387e-02, -3.18768976e-02],
             [ 3.07391705e-02, -4.69159899e-01, -7.17865446e-02,
              -2.52581670e-02,  1.14585147e-02,  9.94635527e-01,
               1.00000000e+00, -4.17693108e-01, -6.40984846e-02,
               3.71812190e-01, -1.07307690e-01, -3.27164732e-02],
             [-6.70493470e-03,  9.79378608e-02,  1.97789478e-01,
               1.25991397e-02, -5.41486806e-03, -4.33436493e-01,
              -4.17693108e-01,  1.00000000e+00,  2.37124810e-01,
              -4.32133625e-01, -1.32366631e-01,  7.35304410e-02],
             [ 4.59513996e-03, -1.18202158e-01,  2.74148682e-01,
              -4.31332807e-02, -3.01287122e-02, -5.74036079e-02,
              -6.40984846e-02,  2.37124810e-01,  1.00000000e+00,
              -1.45464758e-01, -2.46856204e-02,  1.82447540e-02],
             [ 2.21819466e-02, -1.54998940e-01, -8.96066993e-02,
              -1.74274857e-03,  1.54279877e-02,  3.59398479e-01,
               3.71812190e-01, -4.32133625e-01, -1.45464758e-01,
               1.00000000e+00, -4.80546183e-02, -1.11093421e-01],
             [-1.61669692e-03,  9.15359600e-02,  3.69653763e-02,
              -3.02094605e-05, -1.55270941e-02, -5.70376387e-02,
              -1.07307690e-01, -1.32366631e-01, -2.46856204e-02,
              -4.80546183e-02,  1.00000000e+00,  2.50120835e-02],
             [-1.80310455e-03,  5.03876348e-03,  1.71422780e-02,
               5.51084719e-04, -3.57307853e-03, -3.18768976e-02,
              -3.27164732e-02,  7.35304410e-02,  1.82447540e-02,
              -1.11093421e-01,  2.50120835e-02,  1.00000000e+00]])

# 2020-05-06 01:20:00 
__New Spark session:__
[('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.driver.port', '37939'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.driver.host', '97901d576ca5'), ('spark.kryoserializer.buffer.max', '10'), ('spark.app.id', 'local-1588727933594'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-06 01:20:04 
__Number of rows:__
2974335

# 2020-05-06 01:20:04 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-06 01:20:07 
__Data analysis:__
Rows: 2974335
Columns 43
root
 |-- TMC: double (nullable = true)
 |-- Severity: integer (nullable = true)
 |-- Start_Time: timestamp (nullable = true)
 |-- Start_Lat: double (nullable = true)
 |-- Start_Lng: double (nullable = true)
 |-- Distance(mi): double (nullable = true)
 |-- Number: double (nullable = true)
 |-- Street: string (nullable = true)
 |-- Side: string (nullable = true)
 |-- City: string (nullable = true)
 |-- County: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Timezone: string (nullable = true)
 |-- Airport_Code: string (nullable = true)
 |-- Weather_Timestamp: timestamp (nullable = true)
 |-- Temperature(F): double (nullable = true)
 |-- Wind_Chill(F): double (nullable = true)
 |-- Humidity(%): double (nullable = true)
 |-- Pressure(in): double (nullable = true)
 |-- Visibility(mi): double (nullable = true)
 |-- Wind_Direction: string (nullable = true)
 |-- Wind_Speed(mph): double (nullable = true)
 |-- Precipitation(in): double (nullable = true)
 |-- Weather_Condition: string (nullable = true)
 |-- Amenity: string (nullable = true)
 |-- Bump: string (nullable = true)
 |-- Crossing: string (nullable = true)
 |-- Give_Way: string (nullable = true)
 |-- Junction: string (nullable = true)
 |-- No_Exit: string (nullable = true)
 |-- Railway: string (nullable = true)
 |-- Roundabout: string (nullable = true)
 |-- Station: string (nullable = true)
 |-- Stop: string (nullable = true)
 |-- Traffic_Calming: string (nullable = true)
 |-- Traffic_Signal: string (nullable = true)
 |-- Turning_Loop: string (nullable = true)
 |-- Sunrise_Sunset: string (nullable = true)
 |-- Civil_Twilight: string (nullable = true)
 |-- Nautical_Twilight: string (nullable = true)
 |-- Astronomical_Twilight: string (nullable = true)
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night')]

# 2020-05-06 01:21:01 
__Missing values:__
[Row(TMC=728071, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=0, Number=1917605, Street=0, Side=0, City=83, County=0, State=0, Zipcode=880, Country=0, Timezone=3163, Airport_Code=5691, Weather_Timestamp=36705, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Precipitation(in)=1998358, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-06 01:24:09 
__Categorical values:__
[Row(Street=160715), Row(Side=3), Row(City=11685), Row(County=1713), Row(State=49), Row(Zipcode=377152), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1995), Row(Wind_Direction=24), Row(Weather_Condition=120), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-06 01:25:27 
__Correlation matrix:__
DenseMatrix([[ 1.00000000e+00, -3.29968079e-02, -4.23709318e-02,
               6.48521350e-02,  4.88102771e-02,  2.89427459e-02,
               3.07391705e-02, -6.70493470e-03,  4.59513996e-03,
               2.21819466e-02, -1.61669692e-03, -1.80310455e-03],
             [-3.29968079e-02,  1.00000000e+00, -5.22492702e-03,
               5.01751676e-02, -3.17558810e-02, -4.68351247e-01,
              -4.69159899e-01,  9.79378608e-02, -1.18202158e-01,
              -1.54998940e-01,  9.15359600e-02,  5.03876348e-03],
             [-4.23709318e-02, -5.22492702e-03,  1.00000000e+00,
              -7.53412624e-03, -1.85446020e-01, -6.29347088e-02,
              -7.17865446e-02,  1.97789478e-01,  2.74148682e-01,
              -8.96066993e-02,  3.69653763e-02,  1.71422780e-02],
             [ 6.48521350e-02,  5.01751676e-02, -7.53412624e-03,
               1.00000000e+00,  2.39536246e-02, -2.59661162e-02,
              -2.52581670e-02,  1.25991397e-02, -4.31332807e-02,
              -1.74274857e-03, -3.02094605e-05,  5.51084719e-04],
             [ 4.88102771e-02, -3.17558810e-02, -1.85446020e-01,
               2.39536246e-02,  1.00000000e+00,  9.15996465e-03,
               1.14585147e-02, -5.41486806e-03, -3.01287122e-02,
               1.54279877e-02, -1.55270941e-02, -3.57307853e-03],
             [ 2.89427459e-02, -4.68351247e-01, -6.29347088e-02,
              -2.59661162e-02,  9.15996465e-03,  1.00000000e+00,
               9.94635527e-01, -4.33436493e-01, -5.74036079e-02,
               3.59398479e-01, -5.70376387e-02, -3.18768976e-02],
             [ 3.07391705e-02, -4.69159899e-01, -7.17865446e-02,
              -2.52581670e-02,  1.14585147e-02,  9.94635527e-01,
               1.00000000e+00, -4.17693108e-01, -6.40984846e-02,
               3.71812190e-01, -1.07307690e-01, -3.27164732e-02],
             [-6.70493470e-03,  9.79378608e-02,  1.97789478e-01,
               1.25991397e-02, -5.41486806e-03, -4.33436493e-01,
              -4.17693108e-01,  1.00000000e+00,  2.37124810e-01,
              -4.32133625e-01, -1.32366631e-01,  7.35304410e-02],
             [ 4.59513996e-03, -1.18202158e-01,  2.74148682e-01,
              -4.31332807e-02, -3.01287122e-02, -5.74036079e-02,
              -6.40984846e-02,  2.37124810e-01,  1.00000000e+00,
              -1.45464758e-01, -2.46856204e-02,  1.82447540e-02],
             [ 2.21819466e-02, -1.54998940e-01, -8.96066993e-02,
              -1.74274857e-03,  1.54279877e-02,  3.59398479e-01,
               3.71812190e-01, -4.32133625e-01, -1.45464758e-01,
               1.00000000e+00, -4.80546183e-02, -1.11093421e-01],
             [-1.61669692e-03,  9.15359600e-02,  3.69653763e-02,
              -3.02094605e-05, -1.55270941e-02, -5.70376387e-02,
              -1.07307690e-01, -1.32366631e-01, -2.46856204e-02,
              -4.80546183e-02,  1.00000000e+00,  2.50120835e-02],
             [-1.80310455e-03,  5.03876348e-03,  1.71422780e-02,
               5.51084719e-04, -3.57307853e-03, -3.18768976e-02,
              -3.27164732e-02,  7.35304410e-02,  1.82447540e-02,
              -1.11093421e-01,  2.50120835e-02,  1.00000000e+00]])

# 2020-05-06 01:26:14 
__Weather condition distribution:__
               Weather_Condition   count
0                          Clear  808171
1                  Mostly Cloudy  412528
2                       Overcast  382480
3                           Fair  335289
4                  Partly Cloudy  295439
5               Scattered Clouds  204662
6                     Light Rain  141073
7                         Cloudy  115496
8                           None   65932
9                     Light Snow   42123
10                          Haze   34315
11                          Rain   32826
12                           Fog   22138
13                    Heavy Rain   12064
14                 Light Drizzle   10277
15  Light Thunderstorms and Rain    4928
16                          Snow    4796
17                  Thunderstorm    4438
18                  Fair / Windy    3759
19                         Smoke    3602

# 2020-05-06 01:30:25 
__New Spark session:__
[('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.serializer.objectStreamReset', '200'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.app.id', 'local-1588728550600'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.driver.host', '97901d576ca5'), ('spark.rdd.compress', 'True'), ('spark.driver.port', '41191'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.kryoserializer.buffer.max', '15'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-06 01:30:30 
__Number of rows:__
2974335

# 2020-05-06 01:30:30 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-06 01:30:33 
__Data analysis:__
Rows: 2974335
Columns 43
root
 |-- TMC: double (nullable = true)
 |-- Severity: integer (nullable = true)
 |-- Start_Time: timestamp (nullable = true)
 |-- Start_Lat: double (nullable = true)
 |-- Start_Lng: double (nullable = true)
 |-- Distance(mi): double (nullable = true)
 |-- Number: double (nullable = true)
 |-- Street: string (nullable = true)
 |-- Side: string (nullable = true)
 |-- City: string (nullable = true)
 |-- County: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Timezone: string (nullable = true)
 |-- Airport_Code: string (nullable = true)
 |-- Weather_Timestamp: timestamp (nullable = true)
 |-- Temperature(F): double (nullable = true)
 |-- Wind_Chill(F): double (nullable = true)
 |-- Humidity(%): double (nullable = true)
 |-- Pressure(in): double (nullable = true)
 |-- Visibility(mi): double (nullable = true)
 |-- Wind_Direction: string (nullable = true)
 |-- Wind_Speed(mph): double (nullable = true)
 |-- Precipitation(in): double (nullable = true)
 |-- Weather_Condition: string (nullable = true)
 |-- Amenity: string (nullable = true)
 |-- Bump: string (nullable = true)
 |-- Crossing: string (nullable = true)
 |-- Give_Way: string (nullable = true)
 |-- Junction: string (nullable = true)
 |-- No_Exit: string (nullable = true)
 |-- Railway: string (nullable = true)
 |-- Roundabout: string (nullable = true)
 |-- Station: string (nullable = true)
 |-- Stop: string (nullable = true)
 |-- Traffic_Calming: string (nullable = true)
 |-- Traffic_Signal: string (nullable = true)
 |-- Turning_Loop: string (nullable = true)
 |-- Sunrise_Sunset: string (nullable = true)
 |-- Civil_Twilight: string (nullable = true)
 |-- Nautical_Twilight: string (nullable = true)
 |-- Astronomical_Twilight: string (nullable = true)
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night')]

# 2020-05-06 01:31:31 
__Missing values:__
[Row(TMC=728071, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=0, Number=1917605, Street=0, Side=0, City=83, County=0, State=0, Zipcode=880, Country=0, Timezone=3163, Airport_Code=5691, Weather_Timestamp=36705, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Precipitation(in)=1998358, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-06 01:34:23 
__Categorical values:__
[Row(Street=160715), Row(Side=3), Row(City=11685), Row(County=1713), Row(State=49), Row(Zipcode=377152), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1995), Row(Wind_Direction=24), Row(Weather_Condition=120), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-06 01:35:53 
__Correlation matrix:__
DenseMatrix([[ 1.00000000e+00, -3.29968079e-02, -4.23709318e-02,
               6.48521350e-02,  4.88102771e-02,  2.89427459e-02,
               3.07391705e-02, -6.70493470e-03,  4.59513996e-03,
               2.21819466e-02, -1.61669692e-03, -1.80310455e-03],
             [-3.29968079e-02,  1.00000000e+00, -5.22492702e-03,
               5.01751676e-02, -3.17558810e-02, -4.68351247e-01,
              -4.69159899e-01,  9.79378608e-02, -1.18202158e-01,
              -1.54998940e-01,  9.15359600e-02,  5.03876348e-03],
             [-4.23709318e-02, -5.22492702e-03,  1.00000000e+00,
              -7.53412624e-03, -1.85446020e-01, -6.29347088e-02,
              -7.17865446e-02,  1.97789478e-01,  2.74148682e-01,
              -8.96066993e-02,  3.69653763e-02,  1.71422780e-02],
             [ 6.48521350e-02,  5.01751676e-02, -7.53412624e-03,
               1.00000000e+00,  2.39536246e-02, -2.59661162e-02,
              -2.52581670e-02,  1.25991397e-02, -4.31332807e-02,
              -1.74274857e-03, -3.02094605e-05,  5.51084719e-04],
             [ 4.88102771e-02, -3.17558810e-02, -1.85446020e-01,
               2.39536246e-02,  1.00000000e+00,  9.15996465e-03,
               1.14585147e-02, -5.41486806e-03, -3.01287122e-02,
               1.54279877e-02, -1.55270941e-02, -3.57307853e-03],
             [ 2.89427459e-02, -4.68351247e-01, -6.29347088e-02,
              -2.59661162e-02,  9.15996465e-03,  1.00000000e+00,
               9.94635527e-01, -4.33436493e-01, -5.74036079e-02,
               3.59398479e-01, -5.70376387e-02, -3.18768976e-02],
             [ 3.07391705e-02, -4.69159899e-01, -7.17865446e-02,
              -2.52581670e-02,  1.14585147e-02,  9.94635527e-01,
               1.00000000e+00, -4.17693108e-01, -6.40984846e-02,
               3.71812190e-01, -1.07307690e-01, -3.27164732e-02],
             [-6.70493470e-03,  9.79378608e-02,  1.97789478e-01,
               1.25991397e-02, -5.41486806e-03, -4.33436493e-01,
              -4.17693108e-01,  1.00000000e+00,  2.37124810e-01,
              -4.32133625e-01, -1.32366631e-01,  7.35304410e-02],
             [ 4.59513996e-03, -1.18202158e-01,  2.74148682e-01,
              -4.31332807e-02, -3.01287122e-02, -5.74036079e-02,
              -6.40984846e-02,  2.37124810e-01,  1.00000000e+00,
              -1.45464758e-01, -2.46856204e-02,  1.82447540e-02],
             [ 2.21819466e-02, -1.54998940e-01, -8.96066993e-02,
              -1.74274857e-03,  1.54279877e-02,  3.59398479e-01,
               3.71812190e-01, -4.32133625e-01, -1.45464758e-01,
               1.00000000e+00, -4.80546183e-02, -1.11093421e-01],
             [-1.61669692e-03,  9.15359600e-02,  3.69653763e-02,
              -3.02094605e-05, -1.55270941e-02, -5.70376387e-02,
              -1.07307690e-01, -1.32366631e-01, -2.46856204e-02,
              -4.80546183e-02,  1.00000000e+00,  2.50120835e-02],
             [-1.80310455e-03,  5.03876348e-03,  1.71422780e-02,
               5.51084719e-04, -3.57307853e-03, -3.18768976e-02,
              -3.27164732e-02,  7.35304410e-02,  1.82447540e-02,
              -1.11093421e-01,  2.50120835e-02,  1.00000000e+00]])

# 2020-05-06 01:39:49 
__Weather condition distribution:__
               Weather_Condition   count
0                          Clear  808171
1                  Mostly Cloudy  412528
2                       Overcast  382480
3                           Fair  335289
4                  Partly Cloudy  295439
5               Scattered Clouds  204662
6                     Light Rain  141073
7                         Cloudy  115496
8                           None   65932
9                     Light Snow   42123
10                          Haze   34315
11                          Rain   32826
12                           Fog   22138
13                    Heavy Rain   12064
14                 Light Drizzle   10277
15  Light Thunderstorms and Rain    4928
16                          Snow    4796
17                  Thunderstorm    4438
18                  Fair / Windy    3759
19                         Smoke    3602

# 2020-05-06 01:43:31 
__New Spark session:__
[('spark.driver.port', '40755'), ('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.driver.host', '97901d576ca5'), ('spark.rdd.compress', 'True'), ('spark.app.id', 'local-1588729341471'), ('spark.executor.instances', '1'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-06 01:43:36 
__Number of rows:__
2974335

# 2020-05-06 01:43:36 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-06 01:43:38 
__Data analysis:__
Rows: 2974335
Columns 43
root
 |-- TMC: double (nullable = true)
 |-- Severity: integer (nullable = true)
 |-- Start_Time: timestamp (nullable = true)
 |-- Start_Lat: double (nullable = true)
 |-- Start_Lng: double (nullable = true)
 |-- Distance(mi): double (nullable = true)
 |-- Number: double (nullable = true)
 |-- Street: string (nullable = true)
 |-- Side: string (nullable = true)
 |-- City: string (nullable = true)
 |-- County: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Timezone: string (nullable = true)
 |-- Airport_Code: string (nullable = true)
 |-- Weather_Timestamp: timestamp (nullable = true)
 |-- Temperature(F): double (nullable = true)
 |-- Wind_Chill(F): double (nullable = true)
 |-- Humidity(%): double (nullable = true)
 |-- Pressure(in): double (nullable = true)
 |-- Visibility(mi): double (nullable = true)
 |-- Wind_Direction: string (nullable = true)
 |-- Wind_Speed(mph): double (nullable = true)
 |-- Precipitation(in): double (nullable = true)
 |-- Weather_Condition: string (nullable = true)
 |-- Amenity: string (nullable = true)
 |-- Bump: string (nullable = true)
 |-- Crossing: string (nullable = true)
 |-- Give_Way: string (nullable = true)
 |-- Junction: string (nullable = true)
 |-- No_Exit: string (nullable = true)
 |-- Railway: string (nullable = true)
 |-- Roundabout: string (nullable = true)
 |-- Station: string (nullable = true)
 |-- Stop: string (nullable = true)
 |-- Traffic_Calming: string (nullable = true)
 |-- Traffic_Signal: string (nullable = true)
 |-- Turning_Loop: string (nullable = true)
 |-- Sunrise_Sunset: string (nullable = true)
 |-- Civil_Twilight: string (nullable = true)
 |-- Nautical_Twilight: string (nullable = true)
 |-- Astronomical_Twilight: string (nullable = true)
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night')]

# 2020-05-06 01:44:13 
__Missing values:__
[Row(TMC=728071, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=0, Number=1917605, Street=0, Side=0, City=83, County=0, State=0, Zipcode=880, Country=0, Timezone=3163, Airport_Code=5691, Weather_Timestamp=36705, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Precipitation(in)=1998358, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-06 01:45:56 
__Categorical values:__
[Row(Street=160715), Row(Side=3), Row(City=11685), Row(County=1713), Row(State=49), Row(Zipcode=377152), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1995), Row(Wind_Direction=24), Row(Weather_Condition=120), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-06 01:46:47 
__Correlation matrix:__
DenseMatrix([[ 1.00000000e+00, -3.29968079e-02, -4.23709318e-02,
               6.48521350e-02,  4.88102771e-02,  2.89427459e-02,
               3.07391705e-02, -6.70493470e-03,  4.59513996e-03,
               2.21819466e-02, -1.61669692e-03, -1.80310455e-03],
             [-3.29968079e-02,  1.00000000e+00, -5.22492702e-03,
               5.01751676e-02, -3.17558810e-02, -4.68351247e-01,
              -4.69159899e-01,  9.79378608e-02, -1.18202158e-01,
              -1.54998940e-01,  9.15359600e-02,  5.03876348e-03],
             [-4.23709318e-02, -5.22492702e-03,  1.00000000e+00,
              -7.53412624e-03, -1.85446020e-01, -6.29347088e-02,
              -7.17865446e-02,  1.97789478e-01,  2.74148682e-01,
              -8.96066993e-02,  3.69653763e-02,  1.71422780e-02],
             [ 6.48521350e-02,  5.01751676e-02, -7.53412624e-03,
               1.00000000e+00,  2.39536246e-02, -2.59661162e-02,
              -2.52581670e-02,  1.25991397e-02, -4.31332807e-02,
              -1.74274857e-03, -3.02094605e-05,  5.51084719e-04],
             [ 4.88102771e-02, -3.17558810e-02, -1.85446020e-01,
               2.39536246e-02,  1.00000000e+00,  9.15996465e-03,
               1.14585147e-02, -5.41486806e-03, -3.01287122e-02,
               1.54279877e-02, -1.55270941e-02, -3.57307853e-03],
             [ 2.89427459e-02, -4.68351247e-01, -6.29347088e-02,
              -2.59661162e-02,  9.15996465e-03,  1.00000000e+00,
               9.94635527e-01, -4.33436493e-01, -5.74036079e-02,
               3.59398479e-01, -5.70376387e-02, -3.18768976e-02],
             [ 3.07391705e-02, -4.69159899e-01, -7.17865446e-02,
              -2.52581670e-02,  1.14585147e-02,  9.94635527e-01,
               1.00000000e+00, -4.17693108e-01, -6.40984846e-02,
               3.71812190e-01, -1.07307690e-01, -3.27164732e-02],
             [-6.70493470e-03,  9.79378608e-02,  1.97789478e-01,
               1.25991397e-02, -5.41486806e-03, -4.33436493e-01,
              -4.17693108e-01,  1.00000000e+00,  2.37124810e-01,
              -4.32133625e-01, -1.32366631e-01,  7.35304410e-02],
             [ 4.59513996e-03, -1.18202158e-01,  2.74148682e-01,
              -4.31332807e-02, -3.01287122e-02, -5.74036079e-02,
              -6.40984846e-02,  2.37124810e-01,  1.00000000e+00,
              -1.45464758e-01, -2.46856204e-02,  1.82447540e-02],
             [ 2.21819466e-02, -1.54998940e-01, -8.96066993e-02,
              -1.74274857e-03,  1.54279877e-02,  3.59398479e-01,
               3.71812190e-01, -4.32133625e-01, -1.45464758e-01,
               1.00000000e+00, -4.80546183e-02, -1.11093421e-01],
             [-1.61669692e-03,  9.15359600e-02,  3.69653763e-02,
              -3.02094605e-05, -1.55270941e-02, -5.70376387e-02,
              -1.07307690e-01, -1.32366631e-01, -2.46856204e-02,
              -4.80546183e-02,  1.00000000e+00,  2.50120835e-02],
             [-1.80310455e-03,  5.03876348e-03,  1.71422780e-02,
               5.51084719e-04, -3.57307853e-03, -3.18768976e-02,
              -3.27164732e-02,  7.35304410e-02,  1.82447540e-02,
              -1.11093421e-01,  2.50120835e-02,  1.00000000e+00]])

# 2020-05-06 01:47:11 
__Weather condition distribution:__
               Weather_Condition   count
0                          Clear  808171
1                  Mostly Cloudy  412528
2                       Overcast  382480
3                           Fair  335289
4                  Partly Cloudy  295439
5               Scattered Clouds  204662
6                     Light Rain  141073
7                         Cloudy  115496
8                           None   65932
9                     Light Snow   42123
10                          Haze   34315
11                          Rain   32826
12                           Fog   22138
13                    Heavy Rain   12064
14                 Light Drizzle   10277
15  Light Thunderstorms and Rain    4928
16                          Snow    4796
17                  Thunderstorm    4438
18                  Fair / Windy    3759
19                         Smoke    3602

# 2020-05-06 12:03:47 
__New Spark session:__
[('spark.driver.port', '45103'), ('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.driver.host', '97901d576ca5'), ('spark.app.id', 'local-1588766585344'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.kryoserializer.buffer.max', '15'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-06 12:03:50 
__Number of rows:__
2974335

# 2020-05-06 12:03:50 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-06 12:03:52 
__Data analysis:__
Rows: 2974335
Columns 43
root
 |-- TMC: double (nullable = true)
 |-- Severity: integer (nullable = true)
 |-- Start_Time: timestamp (nullable = true)
 |-- Start_Lat: double (nullable = true)
 |-- Start_Lng: double (nullable = true)
 |-- Distance(mi): double (nullable = true)
 |-- Number: double (nullable = true)
 |-- Street: string (nullable = true)
 |-- Side: string (nullable = true)
 |-- City: string (nullable = true)
 |-- County: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Timezone: string (nullable = true)
 |-- Airport_Code: string (nullable = true)
 |-- Weather_Timestamp: timestamp (nullable = true)
 |-- Temperature(F): double (nullable = true)
 |-- Wind_Chill(F): double (nullable = true)
 |-- Humidity(%): double (nullable = true)
 |-- Pressure(in): double (nullable = true)
 |-- Visibility(mi): double (nullable = true)
 |-- Wind_Direction: string (nullable = true)
 |-- Wind_Speed(mph): double (nullable = true)
 |-- Precipitation(in): double (nullable = true)
 |-- Weather_Condition: string (nullable = true)
 |-- Amenity: string (nullable = true)
 |-- Bump: string (nullable = true)
 |-- Crossing: string (nullable = true)
 |-- Give_Way: string (nullable = true)
 |-- Junction: string (nullable = true)
 |-- No_Exit: string (nullable = true)
 |-- Railway: string (nullable = true)
 |-- Roundabout: string (nullable = true)
 |-- Station: string (nullable = true)
 |-- Stop: string (nullable = true)
 |-- Traffic_Calming: string (nullable = true)
 |-- Traffic_Signal: string (nullable = true)
 |-- Turning_Loop: string (nullable = true)
 |-- Sunrise_Sunset: string (nullable = true)
 |-- Civil_Twilight: string (nullable = true)
 |-- Nautical_Twilight: string (nullable = true)
 |-- Astronomical_Twilight: string (nullable = true)
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night')]

# 2020-05-06 12:04:25 
__Missing values:__
[Row(TMC=728071, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=0, Number=1917605, Street=0, Side=0, City=83, County=0, State=0, Zipcode=880, Country=0, Timezone=3163, Airport_Code=5691, Weather_Timestamp=36705, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Precipitation(in)=1998358, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-06 12:06:07 
__Categorical values:__
[Row(Street=160715), Row(Side=3), Row(City=11685), Row(County=1713), Row(State=49), Row(Zipcode=377152), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1995), Row(Wind_Direction=24), Row(Weather_Condition=120), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-06 12:27:40 
__New Spark session:__
[('spark.app.id', 'local-1588768024964'), ('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.driver.port', '37603'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.driver.host', '97901d576ca5'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.kryoserializer.buffer.max', '15'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-06 12:27:42 
__Number of rows:__
2974335

# 2020-05-06 12:27:42 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-06 12:27:44 
__Data analysis:__
Rows: 2974335
Columns 43
root
 |-- TMC: double (nullable = true)
 |-- Severity: integer (nullable = true)
 |-- Start_Time: timestamp (nullable = true)
 |-- Start_Lat: double (nullable = true)
 |-- Start_Lng: double (nullable = true)
 |-- Distance(mi): double (nullable = true)
 |-- Number: double (nullable = true)
 |-- Street: string (nullable = true)
 |-- Side: string (nullable = true)
 |-- City: string (nullable = true)
 |-- County: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Timezone: string (nullable = true)
 |-- Airport_Code: string (nullable = true)
 |-- Weather_Timestamp: timestamp (nullable = true)
 |-- Temperature(F): double (nullable = true)
 |-- Wind_Chill(F): double (nullable = true)
 |-- Humidity(%): double (nullable = true)
 |-- Pressure(in): double (nullable = true)
 |-- Visibility(mi): double (nullable = true)
 |-- Wind_Direction: string (nullable = true)
 |-- Wind_Speed(mph): double (nullable = true)
 |-- Precipitation(in): double (nullable = true)
 |-- Weather_Condition: string (nullable = true)
 |-- Amenity: string (nullable = true)
 |-- Bump: string (nullable = true)
 |-- Crossing: string (nullable = true)
 |-- Give_Way: string (nullable = true)
 |-- Junction: string (nullable = true)
 |-- No_Exit: string (nullable = true)
 |-- Railway: string (nullable = true)
 |-- Roundabout: string (nullable = true)
 |-- Station: string (nullable = true)
 |-- Stop: string (nullable = true)
 |-- Traffic_Calming: string (nullable = true)
 |-- Traffic_Signal: string (nullable = true)
 |-- Turning_Loop: string (nullable = true)
 |-- Sunrise_Sunset: string (nullable = true)
 |-- Civil_Twilight: string (nullable = true)
 |-- Nautical_Twilight: string (nullable = true)
 |-- Astronomical_Twilight: string (nullable = true)
[Row(TMC=201.0, Severity=3, Start_Time=datetime.datetime(2016, 2, 8, 5, 46), Start_Lat=39.865147, Start_Lng=-84.058723, Distance(mi)=0.01, Number=None, Street='I-70 E', Side='R', City='Dayton', County='Montgomery', State='OH', Zipcode='45424', Country='US', Timezone='US/Eastern', Airport_Code='KFFO', Weather_Timestamp=datetime.datetime(2016, 2, 8, 5, 58), Temperature(F)=36.9, Wind_Chill(F)=None, Humidity(%)=91.0, Pressure(in)=29.68, Visibility(mi)=10.0, Wind_Direction='Calm', Wind_Speed(mph)=None, Precipitation(in)=0.02, Weather_Condition='Light Rain', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Night', Civil_Twilight='Night', Nautical_Twilight='Night', Astronomical_Twilight='Night')]

# 2020-05-06 12:28:13 
__Missing values:__
[Row(TMC=728071, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=0, Number=1917605, Street=0, Side=0, City=83, County=0, State=0, Zipcode=880, Country=0, Timezone=3163, Airport_Code=5691, Weather_Timestamp=36705, Temperature(F)=56063, Wind_Chill(F)=1852623, Humidity(%)=59173, Pressure(in)=48142, Visibility(mi)=65691, Wind_Direction=45101, Wind_Speed(mph)=440840, Precipitation(in)=1998358, Weather_Condition=65932, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=93, Civil_Twilight=93, Nautical_Twilight=93, Astronomical_Twilight=93)]

# 2020-05-06 12:29:55 
__Categorical values:__
[Row(Street=160715), Row(Side=3), Row(City=11685), Row(County=1713), Row(State=49), Row(Zipcode=377152), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1995), Row(Wind_Direction=24), Row(Weather_Condition=120), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-06 12:30:41 
__Correlation matrix:__
DenseMatrix([[ 1.00000000e+00, -3.29968079e-02, -4.23709318e-02,
               6.48521350e-02,  4.88102771e-02,  2.89427459e-02,
               3.07391705e-02, -6.70493470e-03,  4.59513996e-03,
               2.21819466e-02, -1.61669692e-03, -1.80310455e-03],
             [-3.29968079e-02,  1.00000000e+00, -5.22492702e-03,
               5.01751676e-02, -3.17558810e-02, -4.68351247e-01,
              -4.69159899e-01,  9.79378608e-02, -1.18202158e-01,
              -1.54998940e-01,  9.15359600e-02,  5.03876348e-03],
             [-4.23709318e-02, -5.22492702e-03,  1.00000000e+00,
              -7.53412624e-03, -1.85446020e-01, -6.29347088e-02,
              -7.17865446e-02,  1.97789478e-01,  2.74148682e-01,
              -8.96066993e-02,  3.69653763e-02,  1.71422780e-02],
             [ 6.48521350e-02,  5.01751676e-02, -7.53412624e-03,
               1.00000000e+00,  2.39536246e-02, -2.59661162e-02,
              -2.52581670e-02,  1.25991397e-02, -4.31332807e-02,
              -1.74274857e-03, -3.02094605e-05,  5.51084719e-04],
             [ 4.88102771e-02, -3.17558810e-02, -1.85446020e-01,
               2.39536246e-02,  1.00000000e+00,  9.15996465e-03,
               1.14585147e-02, -5.41486806e-03, -3.01287122e-02,
               1.54279877e-02, -1.55270941e-02, -3.57307853e-03],
             [ 2.89427459e-02, -4.68351247e-01, -6.29347088e-02,
              -2.59661162e-02,  9.15996465e-03,  1.00000000e+00,
               9.94635527e-01, -4.33436493e-01, -5.74036079e-02,
               3.59398479e-01, -5.70376387e-02, -3.18768976e-02],
             [ 3.07391705e-02, -4.69159899e-01, -7.17865446e-02,
              -2.52581670e-02,  1.14585147e-02,  9.94635527e-01,
               1.00000000e+00, -4.17693108e-01, -6.40984846e-02,
               3.71812190e-01, -1.07307690e-01, -3.27164732e-02],
             [-6.70493470e-03,  9.79378608e-02,  1.97789478e-01,
               1.25991397e-02, -5.41486806e-03, -4.33436493e-01,
              -4.17693108e-01,  1.00000000e+00,  2.37124810e-01,
              -4.32133625e-01, -1.32366631e-01,  7.35304410e-02],
             [ 4.59513996e-03, -1.18202158e-01,  2.74148682e-01,
              -4.31332807e-02, -3.01287122e-02, -5.74036079e-02,
              -6.40984846e-02,  2.37124810e-01,  1.00000000e+00,
              -1.45464758e-01, -2.46856204e-02,  1.82447540e-02],
             [ 2.21819466e-02, -1.54998940e-01, -8.96066993e-02,
              -1.74274857e-03,  1.54279877e-02,  3.59398479e-01,
               3.71812190e-01, -4.32133625e-01, -1.45464758e-01,
               1.00000000e+00, -4.80546183e-02, -1.11093421e-01],
             [-1.61669692e-03,  9.15359600e-02,  3.69653763e-02,
              -3.02094605e-05, -1.55270941e-02, -5.70376387e-02,
              -1.07307690e-01, -1.32366631e-01, -2.46856204e-02,
              -4.80546183e-02,  1.00000000e+00,  2.50120835e-02],
             [-1.80310455e-03,  5.03876348e-03,  1.71422780e-02,
               5.51084719e-04, -3.57307853e-03, -3.18768976e-02,
              -3.27164732e-02,  7.35304410e-02,  1.82447540e-02,
              -1.11093421e-01,  2.50120835e-02,  1.00000000e+00]])

# 2020-05-06 12:32:34 
__Weather condition distribution:__
               Weather_Condition   count
0                          Clear  808171
1                  Mostly Cloudy  412528
2                       Overcast  382480
3                           Fair  335289
4                  Partly Cloudy  295439
5               Scattered Clouds  204662
6                     Light Rain  141073
7                         Cloudy  115496
8                           None   65932
9                     Light Snow   42123
10                          Haze   34315
11                          Rain   32826
12                           Fog   22138
13                    Heavy Rain   12064
14                 Light Drizzle   10277
15  Light Thunderstorms and Rain    4928
16                          Snow    4796
17                  Thunderstorm    4438
18                  Fair / Windy    3759
19                         Smoke    3602