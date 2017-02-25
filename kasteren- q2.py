import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#2 
df = pd.read_csv('KasterenActData.txt', header=None)
df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',2).tolist(), columns=['StartTime', 'EndTime', 'ID'])
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')

df = df.loc[(df['ID']== '1') | (df['ID']== '5') | (df['ID']== '10')]

Duration = []
for index, row in df.iterrows():
   Duration.append(row['EndTime'] - row['StartTime'])

df['Duration'] = Duration

ndf = df.loc[df['ID'] == '1']
ndf['ID'] = pd.to_numeric(ndf['ID'], errors="coerce")
plt.scatter(ndf['ID'], ndf.index)
plt.xlabel('Living Style')
plt.ylim(0,250)
plt.show()

print ndf['Duration'].mean

ndf = df.loc[df['ID'] == '5']
ndf['ID'] = pd.to_numeric(ndf['ID'], errors="coerce")
plt.scatter(ndf['ID'], ndf.index)
plt.xlabel('Living Style')
plt.ylim(0,250)
plt.show()

print ndf['Duration'].mean

ndf = df.loc[df['ID'] == '10']
ndf['ID'] = pd.to_numeric(ndf['ID'], errors="coerce")
plt.scatter(ndf['ID'], ndf.index)
plt.xlabel('Living Style')
plt.ylim(0,250)
plt.show()

print ndf['Duration'].mean


# Result
# Analyzing the activity (Leave house, Take shower, Go to bed)
# The mean of the three : 06:36:32, 00:10:14, 09:11:26
# 1/4 of a day is used to go out -> not too outgoing
# 9/24 of a day is used to sleep -> healthy person 
# 0.10/24 of a day is used to shower -> normal

