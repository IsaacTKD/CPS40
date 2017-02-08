import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')
# Extracting the last two columns of the dataset
# Purpose : to see activities pattern
# Expected result : there is at least some pattern appearing in 30 days
# Day 1

columesName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

for x in range(1, 6):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    df.columns = columesName
    
#   2D Scatter plot
    
    mdf = df[['R2']]
    plt.scatter(mdf['R2'], mdf.index)
    plt.show()  
    
#    Histogram 
#    mdf = df[['R2']] #R1
#    s = "Day " + str(x)
#    ax = mdf.plot.hist(alpha=0.8,bins = 80)
#    ax.set_xlabel(s)


# Result for checking gender
# activity 20 indicates shaving 
# Resident 1 never shaves (Probably a Woman)
# Resident 2 shaves everyday (Probably a Man)

# Result for checking anomaly activity
# Resident 2 are not at home in Day 2 and Day 29
# Resident 2 never has lunch at home
# Resident 2 occasionally has dinner at home
# Resident 2 is not home most of the time



