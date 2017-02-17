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

# 1.Can the data show the gender of the subject/resident?

columesName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

for x in range(1, 1):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    df.columns = columesName
        
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
    
# Result for checking gender
# activity 20 indicates shaving 
# Resident 1 never shaves (Likely to be a Woman)
# Resident 2 shaves everyday (Likely to be a Man)

#General Questions
# 2. Can a living style tell the personality of the person?

for x in range(1,1):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columesName
        
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
    
# Result for finding the personality of the person
#  Resident 1 sleep time is very consistent
#  Resident 1 goes out less and uses internet a lot 
#  Resident 1 could be not a outgoing person and have a good life balance at home
#  Resident 2 is always not home and doesn't clean his place
#  Resident 2 could be a outgoing and untidy person
#  More activities could be used to analyze a person's personalities

# 3. How many subjects are at home? 
# This can be answered by looking at column 20 and columne 21

# 4. How do we know if the subjects are sleeping or they are just lying on the bed? (Assume all smart home should have beds)
mean =0
for x in range(1,30):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columesName
    
    mdf = df.loc[df["R2"]==11]
    mdf = mdf[["R2"]]
    #Begin Time
    if mdf.index.size > 1:
        begin = mdf.index[0]
        #End Time    
        end = mdf.index[mdf.index.size-1]
        #Difference
        diff = end - begin
        #Average
        mean += diff
        #Convert to hours
        if diff > 3600:
            hours = diff / 3600
            temp = diff / 3600.0
            minutes = round(temp % int(temp), 2) * 60
            print 'Day ' + str(x) + ' : ' + str(hours) + 'hrs : ' + str(minutes) + 'mins'
    

# Result for subjects ar sleeping or doing something else
# Without a light switch sensor, time is the only thing to look at.
# Resident 1
# Day 5 
# Resident 2
# Day 2, Day 29, Day 30 are not home.   


 

    

