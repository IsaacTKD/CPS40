import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
# use ggplot to make the graph looks better
plt.style.use('ggplot')

#-----------------------------------------------------------------------------
columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']
#fig = plt.figure(figsize=(10,7))
#ax = fig.add_subplot(111)

# Manipulating and transforming the data
# Grouping number of occurrence per Day
# Grouping activities by time required to complete activity
# Grouping sensors
# Data : 30 days of ARAS data

#df = pd.read_csv('House A/ARAS_Dataset.txt', sep=" ", header=None)
df = pd.read_csv('House A/Day_1.txt', sep=" ", header=None)
df.columns = columnsName
# select only 10 days because it takes too long to load 30 days of data
#df = df.loc[df.index < 864001]
activitiesPerDay = []
activitiesPerDay.append(df.R1[0])
uniqueActivities = []
uniqueActivities = df.R1.unique()
Duration = []
numOccurrences = []
avgDuration = []
numberOfsensors = []
for i in range (0, len(df)-1):       
    if(df.R1[i] != df.R1[i+1]) :
        activitiesPerDay.append(df.R1[i+1])
        

for activity in uniqueActivities:
    count = 0
    for t in activitiesPerDay :
        if(activity==t) :
            count = count + 1
    numOccurrences.append(count)

    
for activity in uniqueActivities:
    ndf = df.loc[df.R1==activity]
    ndf = ndf.reset_index(drop=True)
    Duration.append(round(((len(ndf)-1) /3600.0),2))

#for activity in uniqueActivities:
#    ndf = df.loc[df.R1==activity]
#    ndf = ndf.reset_index(drop=True)
#    ndf = ndf.loc[(ndf['Ph1'] == 1)| (ndf['Ph2'] == 1) | (ndf['Ir1'] == 1) |
#                 (ndf['Fo1'] == 1) | (ndf['Fo2'] == 1) | (ndf['Di3'] == 1) |
#                 (ndf['Di4'] == 1) | (ndf['Ph3'] == 1) | (ndf['Ph4'] == 1) |
#                 (ndf['Ph5'] == 1) | (ndf['Ph6'] == 1) | (ndf['Co1'] == 1) |
#                 (ndf['Co2'] == 1) | (ndf['Co3'] == 1) | (ndf['So1'] == 1) |
#                 (ndf['So2'] == 1) | (ndf['Di1'] == 1) | (ndf['Di2'] == 1) |
#                 (ndf['Te1'] == 1) | (ndf['Fo3'] == 1) ]
#    ndf = ndf.reset_index(drop=True)
#    for x in range (0, len(ndf)):
#        temp = []
#        for y in range(0, 20):
#            if(ndf.iloc[x][y] == 1):
#                temp.append(ndf.columns[y])
#    numberOfsensors.append(len(list(set(temp))))
#    
#
print numberOfsensors
for index in range (0, len(uniqueActivities)):
    avgDuration.append(round(Duration[index] / numOccurrences[index],2))
    
#ndf = pd.DataFrame()
#ndf['ActivitiesID'] = uniqueActivities
#ndf['avgDuration'] = avgDuration
#ndf['numOfoccurrences'] = numOccurrences
#ndf = ndf.sort_values(['ActivitiesID','avgDuration','numOfoccurrences'])
#ndf = ndf.reset_index(drop=True)
#print ndf


#ax.scatter()
#kmeans = KMeans(n_clusters = 2, random_state=0)
#kmeans.fit(ndf)
#centroids = kmeans.cluster_centers_
#ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
#plt.show()


