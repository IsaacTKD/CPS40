import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
plt.style.use('ggplot')

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

# 2. Can a living style tell the personality of the person?

for x in range(1,1):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columnsName
        
#   2D Scatter plot  
#   X-axis : activity of resident R1 or R2
#   Y-axis : Every second

    mdf = df[['R1']]
    plt.scatter(mdf['R1'], mdf.index)
    plt.xlabel('R1 - Day ' + str(x))
    plt.show()  
    
    mdf = df[['R2']]
    plt.scatter(mdf['R2'], mdf.index)
    plt.xlabel('R2 - Day ' + str(x))
    plt.show()  
    
# Result
#  Resident 1 sleep time is very consistent
#  Resident 1 goes out less and uses internet a lot 
#  Resident 1 could be not a outgoing person and have a good life balance at home
#  Resident 2 is always not home and doesn't clean his place
#  Resident 2 could be a outgoing and untidy person
#  More activities could be used to analyze a person's personalities