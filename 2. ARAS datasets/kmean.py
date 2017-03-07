import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
# use ggplot to make the graph looks better
plt.style.use('ggplot')

#-----------------------------------------------------------------------------
#columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']
#fig = plt.figure(figsize=(10,7))
#ax = fig.add_subplot(111)
#
## 1
## Number of occurrence per Day
## Data : 30 days of ARAS data
#
#df = pd.read_csv('House A/ARAS_Datasets.txt', sep=" ", header=None)
#df.columns = columnsName
## select only 10 days because it takes too long to load 30 days of data
#df = df.loc[df.index < 864001]
#activitiesPerDay = []
#activitiesPerDay.append(df.R1[0])
#unique = []
#unique = df.R1.unique()
#d = {}
#for i in range (0, len(df)-1):
#    if(df.R1[i] != df.R1[i+1]) :
#        activitiesPerDay.append(df.R1[i+1])
#for i in unique:
#    count = 0
#    for t in activitiesPerDay :
#        if(i==t) :
#            count = count + 1
#    d.update({i:count})
##keys are the activities ID
##values are the number of occurences 
#ax.scatter(list(d.keys()),list(d.values()))
#    
#
#ndf = pd.DataFrame()
#ndf['activities'] = list(d.keys())
#ndf['occurences'] = list(d.values())
#kmeans = KMeans(n_clusters = 2, random_state=0)
#kmeans.fit_transform(ndf)
#centroids = kmeans.cluster_centers_
#ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
#plt.show()

# Result
# Two clusters 
# 1: number of occurrences from 0 to 20
# 2: number of occurrences from 30 to 70

##2 
## Grouping activities by time required to complete activity
## Data : 30 days of ARAS data
df = pd.read_csv('House A/ARAS_Datasets.txt', sep=" ", header=None)
df.columns = columnsName
# select only 10 days because it takes too long to load 30 days of data
df = df.loc[df.index < 864001]
duration = []

activitiesId = [1]
activitiesPerDay = []
activitiesPerDay.append(df.R1[0])
unique = []
unique = df.R1.unique()
d = {}
for activity in activitiesId:
    ndf = df.loc[df.R1==activity]
    ndf = ndf.reset_index(drop=True)
    totalTime = round(((len(ndf)-1) /3600.0),2)
    for i in range (0, len(df)-1):
        if(df.R1[i] != df.R1[i+1]) :
            activitiesPerDay.append(df.R1[i+1]) 
    count = 0
    for t in activitiesPerDay :
        if(t == activity) :
            count = count + 1
    avg = round (totalTime / count,2)
    d.update({activity:avg})
    
print d
                

#3 
# Grouping sensors
# Data : 30 days of ARAS data


