

# 2020-05-21 23:49:53 
__Number of rows:__
2925212

# 2020-05-21 23:49:53 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['TMC', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'Number', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']

# 2020-05-21 23:49:53 
__New Spark session:__
[('spark.driver.memory', '4g'), ('spark.executor.memory', '4g'), ('spark.driver.host', '4082e07eadd9'), ('spark.ui.enabled', 'true'), ('spark.executor.id', 'driver'), ('spark.app.name', 'Spark Project'), ('spark.app.id', 'local-1590104959030'), ('spark.ui.killEnabled', 'false'), ('spark.driver.port', '45579'), ('spark.serializer', 'org.apache.spark.serializer.KryoSerializer'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.executor.instances', '1'), ('spark.master', 'local[*]'), ('spark.executor.cores', '1'), ('spark.submit.deployMode', 'client'), ('spark.kryoserializer.buffer.max', '15'), ('spark.ui.showConsoleProgress', 'true'), ('spark.driver.cores', '1')]

# 2020-05-21 23:49:55 
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

# 2020-05-21 23:50:23 
__Missing values:__
[Row(TMC=678948, Severity=0, Start_Time=0, Start_Lat=0, Start_Lng=0, Distance(mi)=1, Number=1880955, Street=1, Side=1, City=84, County=1, State=1, Zipcode=804, Country=1, Timezone=2974, Airport_Code=5437, Weather_Timestamp=35687, Temperature(F)=54843, Wind_Chill(F)=1850870, Humidity(%)=57920, Pressure(in)=47054, Visibility(mi)=64348, Wind_Direction=43491, Wind_Speed(mph)=439231, Precipitation(in)=1995584, Weather_Condition=64557, Amenity=1, Bump=1, Crossing=1, Give_Way=1, Junction=1, No_Exit=1, Railway=1, Roundabout=1, Station=1, Stop=1, Traffic_Calming=1, Traffic_Signal=1, Turning_Loop=1, Sunrise_Sunset=94, Civil_Twilight=94, Nautical_Twilight=94, Astronomical_Twilight=94)]

# 2020-05-21 23:51:15 
__Unique column values:__
[Row(Street=159491), Row(Side=3), Row(City=11631), Row(County=1704), Row(State=49), Row(Zipcode=374288), Row(Country=1), Row(Timezone=4), Row(Airport_Code=1990), Row(Wind_Direction=24), Row(Weather_Condition=119), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-21 23:51:54 
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

# 2020-05-21 23:52:25 
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

# 2020-05-21 23:53:21 
__Specified state:__
TX

# 2020-05-21 23:53:30 
__Dataset after modifying UTC timestamp:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 11, 30, 16, 3, 54), Start_Lat=30.336502, Start_Lng=-97.755646, Distance(mi)=0.01, Number=None, Street='Mopac Expy S', Side='R', City='Austin', County='Travis', State='TX', Zipcode='78731', Country='US', Timezone='US/Central', Airport_Code='KATT', Weather_Timestamp=datetime.datetime(2016, 11, 30, 15, 51), Temperature(F)=66.0, Wind_Chill(F)=None, Humidity(%)=24.0, Pressure(in)=30.01, Visibility(mi)=10.0, Wind_Direction='NNW', Wind_Speed(mph)=5.8, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=10, Start_Month=11, Weather_Hour=9, Weather_Month=11)]

# 2020-05-21 23:55:11 
__Clustering:__
k: 399 Cost: 0.1850916987205652

# 2020-05-21 23:56:15 
__Clustering:__
k: 400 Cost: 0.18438905881729487

# 2020-05-21 23:57:31 
__Clustering:__
k: 401 Cost: 0.18490236661377182

# 2020-05-21 23:58:37 
__Clustering:__
k: 402 Cost: 0.1907940260622686

# 2020-05-22 00:01:18 
__Dataset after adding quantiles:__
[Row(TMC=201.0, Severity=2, Start_Time=datetime.datetime(2016, 11, 30, 16, 3, 54), Start_Lat=30.336502, Start_Lng=-97.755646, Distance(mi)=0.01, Number=None, Street='Mopac Expy S', Side='R', City='Austin', County='Travis', State='TX', Zipcode='78731', Country='US', Timezone='US/Central', Airport_Code='KATT', Weather_Timestamp=datetime.datetime(2016, 11, 30, 15, 51), Temperature(F)=66.0, Wind_Chill(F)=None, Humidity(%)=24.0, Pressure(in)=30.01, Visibility(mi)=10.0, Wind_Direction='NNW', Wind_Speed(mph)=5.8, Precipitation(in)=None, Weather_Condition='Clear', Amenity='false', Bump='false', Crossing='false', Give_Way='false', Junction='false', No_Exit='false', Railway='false', Roundabout='false', Station='false', Stop='false', Traffic_Calming='false', Traffic_Signal='false', Turning_Loop='false', Sunrise_Sunset='Day', Civil_Twilight='Day', Nautical_Twilight='Day', Astronomical_Twilight='Day', Start_Hour=10, Start_Month=11, Weather_Hour=9, Weather_Month=11, position_features=DenseVector([30.3365, -97.7556]), position_scaledFeatures=DenseVector([0.4222, 0.6865]), cluster_position=328)]

# 2020-05-22 00:01:18 
__Categorical groups:__
Defined Label:
['Severity']
Defined Categories:
['Start_Hour', 'Start_Month', 'Weather_Hour', 'Weather_Month', 'cluster_position', 'Side', 'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']
Defined Numerical:
['Distance(mi)', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# 2020-05-22 00:01:50 
__Unique column values:__
[Row(Start_Hour=24), Row(Start_Month=12), Row(Weather_Hour=24), Row(Weather_Month=12), Row(cluster_position=400), Row(Side=2), Row(Wind_Direction=24), Row(Weather_Condition=64), Row(Amenity=2), Row(Bump=2), Row(Crossing=2), Row(Give_Way=2), Row(Junction=2), Row(No_Exit=2), Row(Railway=2), Row(Roundabout=2), Row(Station=2), Row(Stop=2), Row(Traffic_Calming=2), Row(Traffic_Signal=2), Row(Turning_Loop=1), Row(Sunrise_Sunset=2), Row(Civil_Twilight=2), Row(Nautical_Twilight=2), Row(Astronomical_Twilight=2)]

# 2020-05-22 00:02:11 
__Missing values:__
[Row(Severity=0, Start_Hour=25, Start_Month=25, Weather_Hour=4791, Weather_Month=4791, cluster_position=0, Distance(mi)=0, Side=0, Temperature(F)=5950, Wind_Chill(F)=220789, Humidity(%)=6205, Pressure(in)=5682, Visibility(mi)=6616, Wind_Direction=5112, Wind_Speed(mph)=36559, Weather_Condition=6761, Amenity=0, Bump=0, Crossing=0, Give_Way=0, Junction=0, No_Exit=0, Railway=0, Roundabout=0, Station=0, Stop=0, Traffic_Calming=0, Traffic_Signal=0, Turning_Loop=0, Sunrise_Sunset=0, Civil_Twilight=0, Nautical_Twilight=0, Astronomical_Twilight=0)]

# 2020-05-22 00:02:35 
__Weather condition:__
[Row(Weather_Condition='Clear', count=76753), Row(Weather_Condition='Mostly Cloudy', count=47475), Row(Weather_Condition='Overcast', count=45135), Row(Weather_Condition='Partly Cloudy', count=36649), Row(Weather_Condition='Scattered Clouds', count=25356), Row(Weather_Condition='Fair', count=23857), Row(Weather_Condition='Light Rain', count=10439), Row(Weather_Condition='Cloudy', count=8963), Row(Weather_Condition=None, count=6761), Row(Weather_Condition='Rain', count=2445), Row(Weather_Condition='Fog', count=2303), Row(Weather_Condition='Haze', count=2182), Row(Weather_Condition='Light Drizzle', count=1320), Row(Weather_Condition='Heavy Rain', count=893), Row(Weather_Condition='Light Thunderstorms and Rain', count=831), Row(Weather_Condition='Thunderstorm', count=586), Row(Weather_Condition='Thunderstorms and Rain', count=395), Row(Weather_Condition='Heavy Thunderstorms and Rain', count=373), Row(Weather_Condition='Light Rain with Thunder', count=342)]
Rows removed: 9747

# 2020-05-22 00:02:48 
__Dropping columns with 1 class:__
['Turning_Loop']

# 2020-05-22 00:03:20 
__Feature set size:__
285999

__Feature vector and label:__
[Row(features=SparseVector(530, {0: 0.0001, 1: 0.5258, 2: 0.8011, 3: 0.2083, 4: 0.9684, 5: 0.0901, 6: 0.0357, 14: 1.0, 31: 1.0, 51: 1.0, 65: 1.0, 137: 1.0, 473: 1.0, 481: 1.0, 497: 1.0, 514: 1.0, 515: 1.0, 516: 1.0, 517: 1.0, 518: 1.0, 519: 1.0, 520: 1.0, 521: 1.0, 522: 1.0, 523: 1.0, 524: 1.0, 525: 1.0, 526: 1.0, 527: 1.0, 528: 1.0, 529: 1.0}), label=2)]

# 2020-05-22 00:03:20 
__Number of rows:__
285999

# 2020-05-22 00:03:23 
__PCA - Feature variance:__
Top 50:
[0.06677006 0.03298092 0.02986547 0.02951486 0.02802247 0.02697695
 0.02547417 0.0244275  0.02356756 0.02237812 0.02159853 0.02098871
 0.02027918 0.01971675 0.01955663 0.01900003 0.01813022 0.01727087
 0.01681889 0.01564397 0.01505559 0.01462081 0.01406345 0.01385096
 0.01308637 0.01292194 0.01241537 0.01236878 0.01217753 0.01113013
 0.01100257 0.01073842 0.00999495 0.00980379 0.00962919 0.00906867
 0.00832408 0.00814237 0.00751642 0.00643214 0.00631255 0.00626352
 0.00579643 0.00571398 0.0054591  0.00532978 0.00518167 0.00479288
 0.00464259 0.00451983]
Number of items: 250
Sum of variance: 0.9743451389410756

# 2020-05-22 00:03:36 
__Top selected features according to ChiSqSelector:__
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 21, 24, 25, 26, 27, 28, 29, 41, 42, 44, 45, 46, 47, 49, 50, 51, 53, 54, 57, 59, 60, 61, 62, 63, 75, 76, 77, 78, 80, 81, 83, 85, 86, 87, 91, 92, 94, 95, 96, 98, 99, 100, 101, 104, 105, 106, 108, 109, 110, 111, 113, 116, 118, 119, 120, 121, 122, 124, 125, 128, 129, 132, 133, 135, 136, 137, 138, 139, 141, 142, 143, 144, 146, 149, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 166, 167, 168, 169, 170, 171, 173, 174, 175, 179, 180, 182, 183, 184, 185, 187, 192, 194, 195, 197, 198, 199, 203, 204, 205, 207, 208, 209, 210, 211, 213, 215, 217, 219, 221, 222, 223, 225, 226, 227, 228, 230, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 243, 246, 251, 254, 255, 257, 259, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 282, 283, 284, 285, 286, 287, 288, 289, 290, 292, 293, 294, 295, 296, 298, 299, 301, 302, 303, 304, 305, 306, 307, 309, 310, 311, 312, 314, 315, 318, 320, 321, 322, 323, 324, 325, 326, 328, 329, 330, 331, 332, 334, 337, 339, 340, 341, 343, 344, 345, 348, 352, 353, 354, 356, 358, 361, 362, 363, 364, 366, 369, 374, 375, 376, 377, 378, 380, 381]
Number of features: 250
Example data:
[Row(features=SparseVector(530, {0: 0.0001, 1: 0.5258, 2: 0.8011, 3: 0.2083, 4: 0.9684, 5: 0.0901, 6: 0.0357, 14: 1.0, 31: 1.0, 51: 1.0, 65: 1.0, 137: 1.0, 473: 1.0, 481: 1.0, 497: 1.0, 514: 1.0, 515: 1.0, 516: 1.0, 517: 1.0, 518: 1.0, 519: 1.0, 520: 1.0, 521: 1.0, 522: 1.0, 523: 1.0, 524: 1.0, 525: 1.0, 526: 1.0, 527: 1.0, 528: 1.0, 529: 1.0}), label=2, selectedFeatures=SparseVector(250, {0: 0.0001, 1: 0.5258, 2: 0.8011, 3: 0.2083, 4: 0.9684, 5: 0.0901, 6: 0.0357, 33: 1.0, 83: 1.0})), Row(features=SparseVector(530, {1: 0.5064, 2: 0.8011, 3: 0.2188, 4: 0.969, 5: 0.0901, 6: 0.0283, 14: 1.0, 31: 1.0, 48: 1.0, 65: 1.0, 84: 1.0, 477: 1.0, 497: 1.0, 514: 1.0, 515: 1.0, 516: 1.0, 517: 1.0, 518: 1.0, 519: 1.0, 520: 1.0, 521: 1.0, 522: 1.0, 523: 1.0, 524: 1.0, 525: 1.0, 526: 1.0, 527: 1.0, 528: 1.0, 529: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.5064, 2: 0.8011, 3: 0.2188, 4: 0.969, 5: 0.0901, 6: 0.0283})), Row(features=SparseVector(530, {1: 0.5064, 2: 0.8011, 3: 0.2188, 4: 0.969, 5: 0.0901, 6: 0.0283, 14: 1.0, 31: 1.0, 48: 1.0, 65: 1.0, 84: 1.0, 473: 1.0, 477: 1.0, 497: 1.0, 514: 1.0, 515: 1.0, 516: 1.0, 517: 1.0, 518: 1.0, 519: 1.0, 520: 1.0, 521: 1.0, 523: 1.0, 524: 1.0, 526: 1.0, 527: 1.0, 528: 1.0, 529: 1.0}), label=2, selectedFeatures=SparseVector(250, {1: 0.5064, 2: 0.8011, 3: 0.2188, 4: 0.969, 5: 0.0901, 6: 0.0283})), Row(features=SparseVector(530, {0: 0.0001, 1: 0.4965, 2: 0.8011, 3: 0.2083, 4: 0.9681, 5: 0.0901, 6: 0.0357, 14: 1.0, 31: 1.0, 51: 1.0, 65: 1.0, 116: 1.0, 473: 1.0, 478: 1.0, 497: 1.0, 514: 1.0, 515: 1.0, 516: 1.0, 517: 1.0, 518: 1.0, 519: 1.0, 520: 1.0, 521: 1.0, 522: 1.0, 523: 1.0, 524: 1.0, 525: 1.0, 526: 1.0, 527: 1.0, 528: 1.0, 529: 1.0}), label=2, selectedFeatures=SparseVector(250, {0: 0.0001, 1: 0.4965, 2: 0.8011, 3: 0.2083, 4: 0.9681, 5: 0.0901, 6: 0.0357, 33: 1.0, 69: 1.0})), Row(features=SparseVector(530, {0: 0.0001, 1: 0.501, 2: 0.8011, 3: 0.1875, 4: 0.9684, 5: 0.0901, 6: 0.0283, 14: 1.0, 31: 1.0, 51: 1.0, 65: 1.0, 76: 1.0, 473: 1.0, 481: 1.0, 497: 1.0, 514: 1.0, 515: 1.0, 516: 1.0, 517: 1.0, 518: 1.0, 519: 1.0, 520: 1.0, 521: 1.0, 522: 1.0, 523: 1.0, 524: 1.0, 525: 1.0, 526: 1.0, 527: 1.0, 528: 1.0, 529: 1.0}), label=3, selectedFeatures=SparseVector(250, {0: 0.0001, 1: 0.501, 2: 0.8011, 3: 0.1875, 4: 0.9684, 5: 0.0901, 6: 0.0283, 33: 1.0, 43: 1.0}))]

# 2020-05-22 00:03:38 
__Fitting LR_Model model..:__


# 2020-05-22 00:05:10 
__Predicting LR_Model on testSet..:__


# 2020-05-22 00:05:10 
__Evaluating LR_Model predictions..:__


# 2020-05-22 00:05:12 
__Evaluating LR_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=1, features=SparseVector(250, {0: 0.0001, 1: 0.4365, 2: 0.8011, 3: 0.7292, 4: 0.9808, 5: 0.0901, 6: 0.1066, 16: 1.0, 32: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {0: 0.0001, 1: 0.4018, 2: 0.5886, 3: 0.7812, 4: 0.9707, 5: 0.0901, 6: 0.0641, 19: 1.0, 36: 1.0, 55: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.5823, 2: 0.8011, 3: 0.9583, 4: 0.9664, 5: 0.0901, 6: 0.0357, 9: 1.0, 27: 1.0, 229: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.6195, 2: 0.8011, 3: 0.6354, 4: 0.9684, 5: 0.0811, 6: 0.0924, 13: 1.0, 27: 1.0, 211: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.6151, 2: 0.8011, 3: 0.6458, 4: 0.969, 5: 0.0901, 6: 0.0641, 16: 1.0, 32: 1.0}))]
Accuracy: 0.7018654405622372
Parameters:
{Param(parent='LogisticRegression_4b52fe2343df', name='regParam', doc='regularization parameter (>= 0).'): 0.01, Param(parent='LogisticRegression_4b52fe2343df', name='maxIter', doc='max number of iterations (>= 0).'): 10, Param(parent='LogisticRegression_4b52fe2343df', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.'): 0.6}

# 2020-05-22 00:05:15 
__Fitting DT_Model model..:__


# 2020-05-22 00:05:50 
__Predicting DT_Model on testSet..:__


# 2020-05-22 00:05:50 
__Evaluating DT_Model predictions..:__


# 2020-05-22 00:05:52 
__Evaluating DT_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=1, features=SparseVector(250, {0: 0.0001, 1: 0.4365, 2: 0.8011, 3: 0.7292, 4: 0.9808, 5: 0.0901, 6: 0.1066, 16: 1.0, 32: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {0: 0.0001, 1: 0.4018, 2: 0.5886, 3: 0.7812, 4: 0.9707, 5: 0.0901, 6: 0.0641, 19: 1.0, 36: 1.0, 55: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.5823, 2: 0.8011, 3: 0.9583, 4: 0.9664, 5: 0.0901, 6: 0.0357, 9: 1.0, 27: 1.0, 229: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.6195, 2: 0.8011, 3: 0.6354, 4: 0.9684, 5: 0.0811, 6: 0.0924, 13: 1.0, 27: 1.0, 211: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.6151, 2: 0.8011, 3: 0.6458, 4: 0.969, 5: 0.0901, 6: 0.0641, 16: 1.0, 32: 1.0}))]
Accuracy: 0.6567321384820869
Parameters:
{}

# 2020-05-22 00:05:55 
__Fitting RF_Model model..:__


# 2020-05-22 00:06:39 
__Predicting RF_Model on testSet..:__


# 2020-05-22 00:06:39 
__Evaluating RF_Model predictions..:__


# 2020-05-22 00:06:41 
__Evaluating RF_Model:__
Display 5 datapoints:
[Row(prediction=2.0, label=1, features=SparseVector(250, {0: 0.0001, 1: 0.4365, 2: 0.8011, 3: 0.7292, 4: 0.9808, 5: 0.0901, 6: 0.1066, 16: 1.0, 32: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {0: 0.0001, 1: 0.4018, 2: 0.5886, 3: 0.7812, 4: 0.9707, 5: 0.0901, 6: 0.0641, 19: 1.0, 36: 1.0, 55: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.5823, 2: 0.8011, 3: 0.9583, 4: 0.9664, 5: 0.0901, 6: 0.0357, 9: 1.0, 27: 1.0, 229: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.6195, 2: 0.8011, 3: 0.6354, 4: 0.9684, 5: 0.0811, 6: 0.0924, 13: 1.0, 27: 1.0, 211: 1.0})), Row(prediction=2.0, label=1, features=SparseVector(250, {1: 0.6151, 2: 0.8011, 3: 0.6458, 4: 0.969, 5: 0.0901, 6: 0.0641, 16: 1.0, 32: 1.0}))]
Accuracy: 0.6150791110781917
Parameters:
{Param(parent='RandomForestClassifier_eb0d9417c632', name='numTrees', doc='Number of trees to train (>= 1).'): 15}

# 2020-05-22 00:06:44 
__Program finished!:__
