import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#4
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

lt = ndf['Activity'].unique()

print "List all activities :"
for i in lt:
    print i

# Result
# Unfortunately, there is no sleeping activities in this dataset 
