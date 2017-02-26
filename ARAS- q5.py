import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# use ggplot to make the graph looks better
plt.style.use('ggplot')

columnsName = ['Ph1','Ph2','Ir1','Fo1','Fo2','Di3','Di4','Ph3','Ph4','Ph5','Ph6','Co1','Co2','Co3','So1','So2','Di1','Di2','Te1','Fo3','R1','R2']

# 5. What are the patterns that can be studied to predict what the subject is going to do next?
for x in range(1,6):
    df = pd.read_csv('House A/DAY_'+ str(x) +'.txt', sep=" ", header=None) 
    df.columns = columnsName
    pattern = []
    unique = True
    for i in range(0, len(df)-1):
        if unique == True :
            pattern.append(df['R2'][i])
            unique = False
        if df['R2'][i] != df['R2'][i+1]:
            unique = True
    print pattern
    
# Result (R1)
# Day 1
# [12, 22, 12, 21, 15, 17, 11, 1, 12, 3, 4, 15, 17, 21, 13, 22, 13, 22, 13, 1, 19, 17, 15, 27, 2, 1, 7, 22, 7, 8, 17, 22, 12, 21, 12]
# Day 2
# [17, 10, 17, 10, 12, 13, 21, 1, 11, 12, 15, 3, 17, 3, 4, 13, 21, 15, 22, 14, 1, 13, 1, 2, 12, 5, 6, 9, 17, 15, 21, 14, 17, 27, 2, 27, 12, 17, 22, 15, 17]
# Day 3
# [10, 12, 25, 12, 17, 21, 15, 11, 1, 15, 1, 12, 3, 4, 9, 12, 17, 22, 17, 21, 12, 17, 10, 15, 14, 1, 5, 6, 9, 17, 22, 17, 18, 27, 2, 12, 27, 12, 13, 10, 15, 13, 22, 17, 22, 10, 12]
# Day 4           
# [12, 17, 22, 17, 21, 11, 15, 1, 17, 23, 3, 4, 9, 22, 15, 1, 21, 1, 12, 13, 22, 13, 5, 12, 5, 6, 9, 15, 13, 25, 13, 22, 13, 10, 12, 22, 13, 7, 8, 9, 12, 22, 12, 10, 15, 13, 17, 13, 22]
# Day 5
# [22, 12, 17, 21, 11, 25, 15, 4, 9, 1, 17, 22, 17, 21, 13, 22, 13, 12, 10, 12, 5, 6, 9, 17, 23, 16, 15, 14, 1, 13, 22, 13, 27, 2, 1, 27, 7, 8, 9, 15, 22, 17, 12, 1, 12, 22]

# Result (R2)
# Day 1
# [17, 15, 17, 11, 20, 21, 15, 27, 2, 14, 17, 12, 22, 10, 22, 12, 22, 12, 17, 15, 8, 9, 17, 21, 12]
# Day 2
# [2]
# Day 3
# [10, 17, 21, 15, 11, 20, 15, 3, 4, 21, 2, 15, 22, 17, 22, 17, 12, 22, 12]
# Day 4
# [17, 21, 11, 1, 11, 15, 20, 14, 3, 4, 21, 27, 2, 25, 15, 14, 27, 2]
# Day 5
# [2, 25, 27, 3, 4, 21, 20, 22, 2, 1, 27, 12, 22, 12, 15, 12, 17, 1, 17, 13, 22, 13, 21, 11]