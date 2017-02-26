import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
plt.style.use('ggplot')

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2'] 
    
# 7. How can anomaly activities be recognized in this dataset? (eg. outlier on a 2D/3D graph?)
for x in range(1,8):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columnsName
    plt.hist(df['R1'], bins = 30)
    plt.xlabel("R1")
    plt.xlim(0,28)
    plt.show()
    
for x in range(1,8):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columnsName
    plt.hist(df['R2'], color="Green", bins = 30)
    plt.xlabel("R2")
    plt.xlim(0,28)
    plt.show()

# Result (for one week)
# R1 Outlier : 27
# R2 Outlier : 1