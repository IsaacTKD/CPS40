import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#7
plt.style.use('ggplot')
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

ndf['ActivityCode'] = pd.Categorical.from_array(ndf['Activity']).labels 
print ndf
plt.hist(ndf['ActivityCode'])
plt.show()

print ndf.loc[ndf['ActivityCode']== 15]


# Result
# From the activity data, 15-17 are rarely done by the subject
# Putting away dishes, Putting away groceries, Putting away laundry deviate from what is standard