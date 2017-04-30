import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
# use ggplot to make the graph looks better
plt.style.use('ggplot')

#-----------------------------------------------------------------------------
house = 'B'
df= pd.read_csv('House ' + house +'/processed_ARAS_R1.txt', names = ["avgDuration","numOfoccurrences","numOfsensors"],sep="\t", header=None)
    
# Data visualization
fig = plt.gcf()
fig.set_size_inches(8.5, 4.5)
plt.bar(df.index, df['numOfoccurrences'], alpha = 0.5, color ='blue')
plt.title('30 Days of Activities in House ' + house)
patch = mpatches.Patch(color='blue', alpha= 0.5, label='Resident 1')
patch1 = mpatches.Patch(color='red', alpha= 0.5, label='Resident 2')
plt.legend(handles=[patch,patch1]) 
plt.xticks(df.index)
plt.xlabel('Activity ID')
plt.ylabel('NumOfoccurrences')
df= pd.read_csv('House ' + house +'/processed_ARAS_R2.txt', names = ["avgDuration","numOfoccurrences","numOfsensors"],sep="\t", header=None)
plt.bar(df.index, df['numOfoccurrences'], alpha= 0.5, color ='red')
plt.show()

df= pd.read_csv('House ' + house + '/processed_ARAS_R1.txt', names = ["avgDuration","numOfoccurrences","numOfsensors"],sep="\t", header=None)
   
fig = plt.gcf()
fig.set_size_inches(8.5, 4.5)
plt.bar(df.index, df['avgDuration'], alpha = 0.5, color ='blue')
plt.title('30 Days of Activities in House ' + house)
patch = mpatches.Patch(color='blue', alpha= 0.5, label='Resident 1')
patch1 = mpatches.Patch(color='red', alpha= 0.5, label='Resident 2')
plt.legend(handles=[patch,patch1]) 
plt.xticks(df.index)
plt.xlabel('Activity ID')
plt.ylabel('AvgDuration')
df= pd.read_csv('House ' + house + '/processed_ARAS_R2.txt', names = ["avgDuration","numOfoccurrences","numOfsensors"],sep="\t", header=None)
plt.bar(df.index, df['avgDuration'], alpha= 0.5, color ='red')
plt.show()


#df= pd.read_csv('House B/processed_ARAS_R1.txt', names = ["avgDuration","numOfoccurrences","numOfsensors"],sep="\t", header=None)
##K-mean clustering 
#X = np.column_stack((df['avgDuration'], df['numOfoccurrences']))
#
#kmeans = KMeans(n_clusters=3)
#kmeans.fit(X)
#
#centroids = kmeans.cluster_centers_
#labels = kmeans.labels_
#predictions =kmeans.predict([
#        [12.0,30],[6.0,30],[6.0,90]])
#
#colors = ["g.","r.","b."]
#
#for i in range(len(X)):
#    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
#
#
#patch = mpatches.Patch(color='green', label='Cluster 0')
#patch1 = mpatches.Patch(color='red', label='Cluster 1')
#patch2 = mpatches.Patch(color='blue', label='Cluster 2')
#plt.legend(handles=[patch,patch1,patch2]) 
#plt.title('30 Days of Activities in House B - Resident 1')
#plt.xlabel('avgDuration')
#plt.ylabel('numOfoccurrences')
#plt.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=150, zorder=10)
#plt.show()
#df = []


