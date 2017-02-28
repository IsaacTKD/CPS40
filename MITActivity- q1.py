import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

#-----------------------------------------------------------------------------
#1 


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

ndf = ndf.loc[ndf['Activity']=='Bathing']

print ndf['Duration'].mean()

 # Result
 # Not 100% sure because there's no activities are female related.
 # Average Bathing time is about 23:49 minutes
 # The subject might be a Female
 # But by looking at the sensor data, a jewelry box is used before going out to work
 # It proves that the subject should be a female
 
 
 
 
 