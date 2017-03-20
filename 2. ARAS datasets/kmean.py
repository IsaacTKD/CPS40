import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.cluster import KMeans
# use ggplot to make the graph looks better
plt.style.use('ggplot')

#-----------------------------------------------------------------------------
# Data cleansing, transformation

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']
sensorsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3']

# Manipulating and transforming the data
# Grouping number of occurrence per Day
# Grouping activities by time required to complete activity
# Grouping sensors
# Data : 30 days of ARAS data

# read input file and clean up the data
df = pd.read_csv('House A/ARAS_Dataset.txt', sep=" ", header=None)
df.columns = columnsName
# select only 10 days because it takes too long to load 30 days of data
#df = df.loc[df.index < 86401]

# declare variables 
activitiesPerDay = []
uniqueActivities = []
Duration = []
numOccurrences = []
avgDuration = []
numSensors = []

# assign value to lists
activitiesPerDay.append(df.R1[0])
uniqueActivities = df.R1.unique()

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
    
for activity in uniqueActivities:
    ndf = df.loc[df.R1==activity]
    ndf = ndf.reset_index(drop=True)
    ndf = ndf.loc[(ndf['Ph1'] == 1)| (ndf['Ph2'] == 1) | (ndf['Ir1'] == 1) |
                 (ndf['Fo1'] == 1) | (ndf['Fo2'] == 1) | (ndf['Di3'] == 1) |
                 (ndf['Di4'] == 1) | (ndf['Ph3'] == 1) | (ndf['Ph4'] == 1) |
                 (ndf['Ph5'] == 1) | (ndf['Ph6'] == 1) | (ndf['Co1'] == 1) |
                 (ndf['Co2'] == 1) | (ndf['Co3'] == 1) | (ndf['So1'] == 1) |
                 (ndf['So2'] == 1) | (ndf['Di1'] == 1) | (ndf['Di2'] == 1) |
                 (ndf['Te1'] == 1) | (ndf['Fo3'] == 1) ]
    ndf = ndf.reset_index(drop=True)
    temp=[]
    for x in sensorsName :
        if(1 in list(ndf[x])):
            temp.append(x)
            
    numSensors.append(len(temp))

for index in range (0, len(uniqueActivities)):
    avgDuration.append(round(Duration[index] / numOccurrences[index],2))
    
# create new dataframe that stores desirable data
ndf = pd.DataFrame()
ndf['activitiesID'] = uniqueActivities
ndf['avgDuration'] = avgDuration
ndf['numOfoccurrences'] = numOccurrences
ndf['numOfsensors'] = numSensors
ndf = ndf.sort_values(['activitiesID','avgDuration','numOfoccurrences','numOfsensors'])
ndf = ndf.reset_index(drop=True)

#-----------------------------------------------------------------------------
# Data modeling 
X = np.column_stack((ndf['avgDuration'], ndf['numOfoccurrences']))
kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ["g.","r.","b."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

patch = mpatches.Patch(color='green', label='Cluster 0')
patch1 = mpatches.Patch(color='red', label='Cluster 1')
patch2 = mpatches.Patch(color='blue', label='Cluster 2')
plt.legend(handles=[patch,patch1,patch2]) 
plt.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=150, zorder=10)

plt.show()


X = np.column_stack((ndf['avgDuration'], ndf['numOfsensors']))
kmeans = KMeans(n_clusters = 3, random_state=0, max_iter=300)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ["g.","r.","b."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

patch = mpatches.Patch(color='green', label='Cluster 0')
patch1 = mpatches.Patch(color='red', label='Cluster 1')
patch2 = mpatches.Patch(color='blue', label='Cluster 2')
plt.legend(handles=[patch,patch1,patch2]) 
plt.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=150, zorder=10)
plt.show()

X = np.column_stack((ndf['numOfoccurrences'], ndf['numOfsensors']))
kmeans = KMeans(n_clusters = 3, random_state=0, max_iter=300)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ["g.","r.","b."]

patch = mpatches.Patch(color='green', label='Cluster 0')
patch1 = mpatches.Patch(color='red', label='Cluster 1')
patch2 = mpatches.Patch(color='blue', label='Cluster 2')
plt.legend(handles=[patch,patch1,patch2]) 
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
    
plt.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=150, zorder=10)
plt.show()


