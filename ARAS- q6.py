import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
plt.style.use('ggplot')

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2'] 
    
# 6. In terms of security of the house, what are the time that subjects not at home?

for x in range(1,2):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columnsName
    resident = "R1"        
    mdf = df.loc[df[resident]==2]
    mdf = mdf[[resident]]
    plt.scatter(mdf[resident], mdf.index)
    plt.xlabel(resident+ ' - Day ' + str(x))
    plt.xlim(1,3)
    plt.show() 
    
# Result
# Resident 1  
# did not go out on Day 4, Day 6, Day 9
# Resident 2
# go out everday