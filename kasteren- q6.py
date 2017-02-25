import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#6
df = pd.read_csv('KasterenActData.txt', header=None)
df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',2).tolist(), columns=['StartTime', 'EndTime', 'ID'])
df = df.loc[df['ID']== '1']
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')

Duration = []
for index, row in df.iterrows():
   Duration.append(row['EndTime'] - row['StartTime'])

df['NotHome_Duration'] = Duration

#print df
#print df['NotHome_Duration'].mean

# Result
# On March 2, March 10 and March 23, the subject left home for a day and more
# The mean of the duration is 0 days 06:36:32  
