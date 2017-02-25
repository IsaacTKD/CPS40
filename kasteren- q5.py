import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#-----------------------------------------------------------------------------
#5
df = pd.read_csv('KasterenActData.txt', header=None)
df.drop(df.index[[0,1,2,3,4,5,6,7,8,9,10,11,12]], inplace=True)
df = pd.DataFrame(df[0].str.split('\t',2).tolist(), columns=['StartTime', 'EndTime', 'ID'])

newdf = pd.DataFrame(df.StartTime.str.split(' ',expand=True))
df = newdf[[0]].join(df)
df.columns = ['Date','StartTime','EndTime', 'ID']
unique = df.Date.unique()
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')
df= df.drop(df.index[245])


#for i in unique :
#    idList = []  
#    x = 1
#    day = []
#    print i
#    for index, row in df.iterrows():    
#        if(i == row['Date']) :
#            day.append(x)
#            x = x + 1
#            idList.append(row['ID'])
#    plt.scatter(day, idList)
#    plt.xlabel(str(i) + ' - Activity Pattern')
#    plt.show()        

# Result  
#activity id list:
#1: 'leave house'
#4: 'use toilet'
#5: 'take shower'
#10:'go to bed'
#13:'prepare Breakfast'
#15:'prepare Dinner'
#17:'get drink'

# Activity pattern :  
#25-Feb-2008
#['10', '4', '13', '5', '1', '4', '17', '4', '15', '17', '4', '10', '4']
#26-Feb-2008
#['4', '4', '4', '4', '13', '5', '1', '4', '17', '4', '10']
#27-Feb-2008
#['4', '13', '4', '5', '1', '15', '17', '4']
#28-Feb-2008
#['4', '10', '4', '4', '13', '4', '5', '1', '4', '1', '4', '4', '10']
#29-Feb-2008
#['4', '13', '4', '5', '1', '1', '4', '15', '1']
#02-Mar-2008
#['4', '15', '4', '10']
#03-Mar-2008
#['4', '13', '5', '1']
#04-Mar-2008
#['4', '1', '4', '1', '4', '17']
#05-Mar-2008
#['4', '4', '10', '4', '4', '13', '5', '1', '15', '4', '4', '4', '10']
#06-Mar-2008
#['4', '4', '13', '4', '5', '1', '17', '4', '15', '17', '17', '4', '4', '10']
#07-Mar-2008
#['4', '4', '17', '13', '5', '1']
#08-Mar-2008
#['17', '4', '10', '4', '17', '4', '4', '10', '13', '4', '5', '1']
#10-Mar-2008
#['10', '4', '4', '13', '5', '1', '4', '15', '17', '4', '17', '4', '10']
#11-Mar-2008
#['4', '4', '4', '5', '1', '15', '17', '4', '1', '17', '17', '4', '10']
#12-Mar-2008
#['4', '4', '13', '17', '4', '1', '5', '1']
#13-Mar-2008
#['4', '10', '4', '4', '13', '5', '1', '4', '4', '1']
#14-Mar-2008
#['4', '10', '4', '4', '13', '4', '5', '1', '4', '1', '4', '4', '10']
#15-Mar-2008
#['4', '4', '4', '13', '4', '4', '4', '5', '15', '17', '4', '1']
#16-Mar-2008
#['4', '10', '4', '4', '13', '5', '1', '4', '10', '4']
#17-Mar-2008
#['4', '4', '13', '5', '4', '1', '4', '15', '4', '17', '17', '4']
#18-Mar-2008
#['4', '10', '4', '4', '13', '5', '1', '4', '4', '1']
#19-Mar-2008
#['4', '10', '4', '13', '4', '5', '1', '5', '1', '4', '4', '10']
#20-Mar-2008
#['4', '4', '4', '13', '5', '1', '4', '4', '4', '10']
#21-Mar-2008
#['4', '4', '4', '5', '1', '4', '10', '4', '1']
