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
ndf['StartTime'] = pd.to_datetime(ndf['StartTime'],errors='coerce')
ndf['EndTime'] = pd.to_datetime(ndf['EndTime'], errors='coerce')
ndf = ndf.sort(['Date','StartTime'])
ndf.index = range(0,len(ndf))

ndf = ndf.loc[(ndf['Activity']=='Going out to work') | (ndf['Activity']=='Going out for shopping') | (ndf['Activity']=='Going out for entertainment')]

Duration = []
for index, row in ndf.iterrows():
   Duration.append(row['EndTime'] - row['StartTime'])

ndf['Duration'] = Duration
ndf['StartTime'] = pd.to_datetime(ndf['StartTime'],errors='coerce').dt.time
ndf['EndTime'] = pd.to_datetime(ndf['EndTime'], errors='coerce').dt.time

print ndf

# Result
# Subject goes out to work 12 times in 16 days
# leaving time (7:51,12:32,13:42,10:18,7:02,12:15,8:30,12:14,9:34,14:05,9:50,7:32)
# Thur(27) -> Fri(28) -> Sat (29) -> Sun (30) -> Mon (31) -> Tue (1)
# Subject goes out for shopping twice in 16 days
# Leaving time (18:48,9:56)
# Subject goes out for entertainment once in 16 days
# Leaving time (18:54) 
