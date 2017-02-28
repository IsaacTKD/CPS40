import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#3
df = pd.read_csv('subject1/activities_data.csv',header=None)
activities = []
for i in range(0, len(df),5):
    activity = [df[0][i],df[1][i],df[2][i],df[3][i]]
    activities.append(activity) 
   
ndf = pd.DataFrame(activities, columns=['Activity','Date','StartTime', 'EndTime'])
ndf['StartTime'] = pd.to_datetime(ndf['StartTime'],errors='coerce').dt.time
ndf['EndTime'] = pd.to_datetime(ndf['EndTime'], errors='coerce').dt.time
ndf = ndf.sort(['Date','StartTime'])
ndf.index = range(0,len(ndf))

oneSubject = True
for i in range(0, len(ndf)-1) :
    
    if (ndf.loc[i]['Date'] == ndf.loc[i+1]['Date']) & (ndf.loc[i]['EndTime'] > ndf.loc[i+1]['StartTime']) :
        print ndf.index[i]
        oneSubject = False

print ndf
print oneSubject

# Result
# Most of the end time from one activity is less than the start time from the second activity
# only one subject is at home.
# There are few cases where the subjects dress before turn off the shower faucet, Groom and do other things.
