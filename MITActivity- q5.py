import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#5
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

unique = ndf['Date'].unique()
for x in unique:
    print 'Activities on ' + str(x) + ':'
    for i in range(0,len(ndf)):
        if (ndf.loc[i]['Date'] == x):
            print ndf.loc[i]['Activity'] 
    print ' '
    print '----------------------------------------------------------'


# Result
# Pattern is generated in text. There is a reason why it is not shown on a graph.
# Converting text into Integers is easy but looking up what number refers to what activity takes time
# Result is on the console.