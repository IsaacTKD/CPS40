import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
matplotlib.style.use('ggplot')

#General Questions

# Purpose : to see activities pattern
# DataSet : ARAS
# Day 1 - Day 30

#General Questions
# 1.Can the data show the gender of the subject/resident?

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

for x in range(1, 1):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    df.columns = columnsName
        
#   Histogram 
    mdf = df[['R1','R2']]
    s = "Day " + str(x)
    data = np.vstack([mdf.R1,mdf.R2]).T
    plt.hist(mdf.R1,alpha=0.5, color='green',bins = 50, label='R1')
    plt.hist(mdf.R2,alpha=0.5, color='red',bins = 50, label='R2')
    plt.xlabel("Day " + str(x))
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.show()
    
# Result
# activity 20 indicates shaving 
# Resident 1 never shaves (Likely to be a Woman)
# Resident 2 shaves everyday (Likely to be a Man)

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

# 3. How many subjects are at home? 
# This can be answered by looking at column 20 and columne 21

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

# 5. What are the patterns that can be studied to predict what the subject is going to do next?
for x in range(1,10):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    df.columns = columnsName
        
    
# 6. In terms of security of the house, what are the time that subjects not at home?

for x in range(1,1):
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


# 7. How can anomaly activities be recognized in this dataset? (eg. outlier on a 2D/3D graph?)

