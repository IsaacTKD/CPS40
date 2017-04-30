import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# use ggplot to make the graph looks better
plt.style.use('ggplot')

#-----------------------------------------------------------------------------
#1 

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

for x in range (1,31):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    
    print df