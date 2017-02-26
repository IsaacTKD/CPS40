import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
plt.style.use('ggplot')

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

# 4. How do we know if the subjects are sleeping or they are just lying on the bed? (Assume all smart home should have beds)
for x in range(1,1):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columnsName
    resident = "R1"        
    mdf = df.loc[df[resident]==11]
    mdf = mdf[[resident]]
    plt.scatter(mdf[resident], mdf.index)
    plt.xlabel(resident+ ' - Day ' + str(x))
    plt.xlim(10,12)
    plt.show()  
    
# Result
# Without a light switch sensor, time is the only thing to look at.
# Resident 1
# Sleeping schedule is pretty normal.
# Resident 2
# Day 2 and Day 29 are not home.   
# Day 5 is a mistake definitely to say that person is sleeping for about 2 minutes