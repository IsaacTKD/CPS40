import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

#-----------------------------------------------------------------------------
#2

df = pd.read_csv('subject1/activities_data.csv',header=None)
activities = []
for i in range(0, len(df),5):
    activity = [df[0][i],df[1][i],df[2][i],df[3][i]]
    activities.append(activity) 
   
ndf = pd.DataFrame(activities, columns=['Activity','Date','StartTime', 'EndTime'])
ndf['StartTime'] = pd.to_datetime(ndf['StartTime'],errors='coerce')
ndf['EndTime'] = pd.to_datetime(ndf['EndTime'], errors='coerce')

Duration = []
for index, row in ndf.iterrows():
   Duration.append(row['EndTime'] - row['StartTime'])

ndf['Duration'] = Duration
ndf['StartTime'] = pd.to_datetime(ndf['StartTime'],errors='coerce').dt.time
ndf['EndTime'] = pd.to_datetime(ndf['EndTime'], errors='coerce').dt.time

temp = ndf.loc[(ndf['Activity']=='Bathing')]

print temp['Duration'].mean()
print len(temp['Duration'])

temp = ndf.loc[(ndf['Activity']=='Cleaning')]

print temp['Duration'].mean()
print len(temp['Duration'])

temp = ndf.loc[(ndf['Activity']=='Doing laundry')]

print temp['Duration'].mean()
print len(temp['Duration'])

# to check if a person is a workaholic or healthy (work + relax)
temp = ndf.loc[(ndf['Activity']=='Going out to work')]

print "Going out to work:"
print temp['Duration'].mean()
print len(temp['Duration'])

temp = ndf.loc[(ndf['Activity']=='Watching TV')]

print "Wacthing TV:"
print temp['Duration'].mean()
print len(temp['Duration'])

temp = ndf.loc[(ndf['Activity']=='Going out for entertainment')]

print "Going out for entertainment:"
print temp['Duration'].mean()
print len(temp['Duration'])

temp = ndf.loc[(ndf['Activity']=='Going out for shopping')]

print "Going out for shopping:"
print temp['Duration'].mean()
print len(temp['Duration'])
# Result
# List of activities
#    Bathing
#    Toileting
#    Going out to work
#    Preparing lunch
#    Preparing dinner
#    Preparing breakfast
#    Dressing
#    Grooming
#    Preparing a snack
#    Preparing a beverage
#    Washing dishes
#    Doing laundry
#    Cleaning
#    Putting away dishes
#    Washing hands
#    Putting away groceries
#    Other
#    Watching TV
#    Going out for shopping
#    Going out for entertainment
#    Lawnwork
#    Putting away laundry
# The average time of bathing is 23:49 minutes. (18 times from 3/27/03 to 4/11/03)
# The average time of cleaning is 18:39 minutes (9 times from 3/27/03 to 4/11/03)
# The average time of doing laundry is 11:23 minutes (9 times from 3/27/03 to 4/11/03)
# The subject is a person which is quite clean and tidy.

# The average time in this case is not useful because it is not the actual time of the activity
# The subject goes out to work 12 times in 16 days
# The subject goes out for entertainment once in 16 days
# The subject goes out for shopping twice in 16 days
# The subject watches TV 3 times in 16 days
# The subject is a person which is a normal worker without lot of entertainments.

 
 