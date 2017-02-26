import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#7

#Activities
plt.style.use('ggplot')
df = pd.read_csv('KasterenActData.txt', header=None)
df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',2).tolist(), columns=['StartTime', 'EndTime', 'ID'])
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')
df = df.drop(df.index[245])

df['ID'] = pd.to_numeric(df['ID'], errors='coerce')
plt.hist(df['ID'], bins =30)
plt.show()

#Sensors
df = pd.read_csv('KasterenSenseData.txt', header=None)
df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',3).tolist(), columns=['StartTime', 'EndTime', 'ID', ' Val'])
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')
df = df.drop(df.index[1319])

df['ID'] = pd.to_numeric(df['ID'], errors='coerce')
plt.hist(df['ID'], bins = 30)
plt.show()

# Result 
# From the activity data, preparing dinner is rarely done by the subject
# From the sensor data, subject rarely washes dishes 





