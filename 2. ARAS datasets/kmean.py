import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
# use ggplot to make the graph looks better
plt.style.use('ggplot')

#-----------------------------------------------------------------------------
# from 9 - 10
columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']
fig = plt.figure()
ax = fig.add_subplot(111)

indexes = []
r1_activities = []

ndf = pd.DataFrame(columns=columnsName)

frames = []

for x in range(1, 31):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None)
    df.columns = columnsName
    df = df.loc[(df.index >= 32400) & (df.index < 36000)]
    frames.append(df)
    
ndf = pd.concat(frames)

ndf['time'] = ndf.index

ax.scatter(ndf.index, ndf.R1, marker='.', alpha=0.3)
kmeans = KMeans(n_clusters = 6)
ndf = ndf[['time','R1']]
kmeans.fit(ndf)
labels = kmeans.predict(ndf)
centroids = kmeans.cluster_centers_
ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
plt.show()



