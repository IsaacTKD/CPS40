import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
plt.style.use('ggplot')

# 1.Can the data show the gender of the subject/resident?

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

for x in range(1, 5):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    df.columns = columnsName
        
#   Histogram 
    mdf = df[['R1','R2']]
    s = "Day " + str(x)
    data = np.vstack([mdf.R1,mdf.R2]).T
    plt.hist(mdf.R1,alpha=0.5, color='green',bins = 30, label='R1')
    plt.hist(mdf.R2,alpha=0.5, color='red',bins = 30, label='R2')
    plt.xlabel("Day " + str(x))
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.show()
    
# Result
# activity 20 indicates shaving 
# Resident 1 never shaves (Likely to be a Woman)
# Resident 2 shaves everyday (Likely to be a Man)