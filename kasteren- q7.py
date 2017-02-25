import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#7
df = pd.read_csv('KasterenActData.txt', header=None)
df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',2).tolist(), columns=['StartTime', 'EndTime', 'ID'])
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')
df = df.drop(df.index[245])
print df




