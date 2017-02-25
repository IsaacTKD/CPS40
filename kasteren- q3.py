import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#3
df = pd.read_csv('KasterenSenseData.txt', header=None)

df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',3).tolist(), columns=['StartTime', 'EndTime', 'ID', 'Val'])
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')
df = df.drop(df.index[1319])

oneSubject = True
for i in range(0, len(df)-1) :
    if df.iloc[i]['EndTime'] > df.loc[i+1]['StartTime'] :
        oneSubject = False

print oneSubject

# Result
# The end time from one sensor is less than the start time from the second sensor
# only one subject is at home because the sensor is only activated one at a time.
