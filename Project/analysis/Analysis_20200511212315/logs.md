

# 2020-05-11 21:23:50 
__New Spark session:__
[('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.ui.enabled', 'true'), ('spark.app.id', 'local-1589232197216'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.ui.killEnabled', 'false'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.driver.host', '97901d576ca5'), ('spark.driver.port', '46735'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.kryoserializer.buffer.max', '15'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-11 21:23:52 
__Number of rows:__
2925212

# 2020-05-11 21:23:52 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-11 21:23:54 
__Data analysis:__
Rows: 2925212
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

# 2020-05-11 21:24:21 
__Missing values:__
[Row(TMC=678948, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=1, Number=1880955, Street=1, Side=1, City=84, County=1, State=1, Zipcode=804, Country=1, Timezone=2974, Airport_Code=5437, Weather_Timestamp=35687, Temperature(F)=54843, Wind_Chill(F)=1850870, Humidity(%)=57920, Pressure(in)=47054, Visibility(mi)=64348, Wind_Direction=43491, Wind_Speed(mph)=439231, Precipitation(in)=1995584, Weather_Condition=64557, Amenity=1, Bump=1, Crossing=1, Give_Way=1, Junction=1, No_Exit=1, Railway=1, Roundabout=1, Station=1, Stop=1, Traffic_Calming=1, Traffic_Signal=1, Turning_Loop=1, Sunrise_Sunset=94, Civil_Twilight=94, Nautical_Twilight=94, Astronomical_Twilight=94)]

# 2020-05-11 21:25:13 
__Unique column values:__
[Row(Street=159491), Row(Side=3), Row(City=11631), Row(County=1704), Row(State=49), Row(Zipcode=374288), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1990), Row(Wind_Direction=24), Row(Weather_Condition=119), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-11 21:25:51 
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

# 2020-05-11 21:26:12 
__Weather condition distribution:__
               Weather_Condition   count
0                          Clear  808171
1                  Mostly Cloudy  405136
2                       Overcast  382479
3                           Fair  311864
4                  Partly Cloudy  288380
5               Scattered Clouds  204662
6                     Light Rain  139622
7                         Cloudy  109817
8                           None   64557
9                     Light Snow   42109
10                          Haze   33932
11                          Rain   32585
12                           Fog   21853
13                    Heavy Rain   11966
14                 Light Drizzle   10201
15  Light Thunderstorms and Rain    4928
16                          Snow    4795
17                  Thunderstorm    4438
18                         Smoke    3558
19                  Fair / Windy    3547