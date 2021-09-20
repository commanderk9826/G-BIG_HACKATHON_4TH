from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

case2= pd.read_csv('보행도로_통합파일_최종.csv',encoding='EUC-KR')

data_norm = case2.copy() 

case2

from sklearn.preprocessing import MinMaxScaler
minMaxScaler = MinMaxScaler()

case2_df2=case2.drop(['동','자치구','0-12세(어린이)','65-100이상(노인)','장애인수','동별보행취약계층인구수','총인구','시설개수','area/Dong'],axis=1,inplace=False)

print(minMaxScaler.fit(case2_df2))
case2_minmax2= minMaxScaler.transform(case2_df2)

case2_df2=pd.DataFrame(case2_minmax2, columns=case2_df2.columns)
case2_df2


ks = range(1,20)   
inertias = []    
for k in ks :
    model = KMeans(n_clusters = k, n_init = 5)  
    get_ipython().run_line_magic('time', "model.fit(case2_df2)   
    inertias.append(model.inertia_)    
    print('n_cluster : {}, inertia : {}'.format(k, model.inertia_))      # 적정 클러스터의 개수를 찾기위해 elbow 그래프를 그려 확인
    
plt.figure(figsize = (15, 6))   
plt.plot(ks, inertias, '-o')    
plt.xlabel('number of clusters, k')    
plt.ylabel('inertia')    
plt.xticks(ks)    
plt.show()


kmeans= KMeans(n_clusters=7)
kmeans.fit(case2_df2)
answer=kmeans.fit_predict(case2_df2)

df=pd.DataFrame(case2_df2)

cluster= pd.DataFrame(kmeans.labels_)

df_merge = pd.concat([df,cluster],axis=1)
df_merge.info()
df_merge.describe()

cluster_size = df_merge.groupby([0]).count()    
print(cluster_size)

sns.countplot(answer)  # 클러스터별 데이터 개수 시각화
print(answer)

x=case2_df2.values

# 3차원 시각화를 통해 클러스터된 군집 확인
fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[answer == 0,0],x[answer == 0,1],x[answer == 0,2], s = 40 , color = 'blue', label = "cluster 0")
ax.scatter(x[answer == 1,0],x[answer == 1,1],x[answer == 1,2], s = 40 , color = 'orange', label = "cluster 1")
ax.scatter(x[answer == 2,0],x[answer == 2,1],x[answer == 2,2], s = 40 , color = 'green', label = "cluster 2")
ax.scatter(x[answer == 3,0],x[answer == 3,1],x[answer == 3,2], s = 40 , color = '#D12B60', label = "cluster 3")
ax.scatter(x[answer == 4,0],x[answer == 4,1],x[answer == 4,2], s = 40 , color = 'purple', label = "cluster 4")
ax.scatter(x[answer == 5,0],x[answer == 5,1],x[answer == 5,2], s = 40 , color = 'black', label = "cluster 5")
ax.scatter(x[answer == 6,0],x[answer == 6,1],x[answer == 6,2], s = 40 , color = 'red', label = "cluster 6")

ax.set_xlabel('population rate-->')
ax.set_ylabel('Facility rate-->')
ax.set_zlabel('Slope rate-->')
ax.legend()
plt.show()



#히트맵을 통해 각 클러스터의 특징 식별
temp = df_merge.groupby([0]).mean()   
cluster_mean = temp.transpose()    
mean_table = cluster_mean.div(cluster_mean.max(axis=1), axis=0)    


plt.figure(figsize = (15, 15))   
sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')

sns.heatmap(mean_table,    
	annot=True,     
            fmt='.3f',   
            linewidths = 0.1,   
            cmap = 'RdYlGn_r')    
plt.title('Cluster mean table', fontsize=13)
plt.show()


# # Result print

cluster= pd.DataFrame(kmeans.labels_)

case2_df2

df_merge = pd.concat([case2_df2,cluster],axis=1)
df_merge

result_df=pd.concat([case2,cluster],axis=1)

result_df.to_csv("Clustering_Kmeans.csv",encoding="EUC-KR")


# # Dendrogram


from scipy.cluster.hierarchy import dendrogram, linkage

import scipy.cluster.hierarchy as shc

plt.figure(figsize=(10, 7))
dend = shc.dendrogram(shc.linkage(case2_df2, method='ward')) # 덴드로그램 시각화

from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit_predict(case2_df2)
answer=cluster.fit_predict(case2_df2)


cluster= pd.DataFrame(cluster.fit_predict(case2_df2))

df_merge = pd.concat([df,cluster],axis=1)
df_merge.info()
df_merge.describe()

cluster_size = df_merge.groupby([0]).count()    
print(cluster_size)
cluster_size.plot(kind = 'bar')


temp = df_merge.groupby([0]).mean()   
cluster_mean = temp.transpose()   
mean_table = cluster_mean.div(cluster_mean.max(axis=1), axis=0)    

plt.figure(figsize = (15, 20))    
sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')

sns.heatmap(mean_table,   
	annot=True,     
            fmt='.3f',    
            linewidths = 0.1,    
            cmap = 'RdYlGn_r')  
plt.title('Cluster mean table', fontsize=13)
plt.show()

x=case2_df2.values

fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[answer == 0,0],x[answer == 0,1],x[answer == 0,2], s = 40 , color = 'blue', label = "cluster 0")
ax.scatter(x[answer == 1,0],x[answer == 1,1],x[answer == 1,2], s = 40 , color = 'orange', label = "cluster 1")
ax.scatter(x[answer == 2,0],x[answer == 2,1],x[answer == 2,2], s = 40 , color = 'green', label = "cluster 2")

ax.set_xlabel('population rate-->')
ax.set_ylabel('Facility rate-->')
ax.set_zlabel('Slope rate-->')
ax.legend()
plt.show()

result_df2=pd.concat([case2,cluster],axis=1)
result_df2.to_csv("Clustering_dendrogram.csv",encoding="EUC-KR")


# # DBSCAN

from sklearn.cluster import DBSCAN
db_scan =DBSCAN(eps=0.1, min_samples=5).fit(case2_df2.values)
answer=db_scan.fit_predict(case2_df2)

df=pd.DataFrame(case2_df2)

cluster= pd.DataFrame(db_scan.labels_)

df_merge = pd.concat([df,cluster],axis=1)
df_merge.info()
df_merge.describe()

cluster_size = df_merge.groupby([0]).count()    
print(cluster_size)
cluster_size.plot(kind = 'bar')

x=case2_df2.values

fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[answer == 0,0],x[answer == 0,1],x[answer == 0,2], s = 40 , color = 'blue', label = "cluster 0")
ax.scatter(x[answer == 1,0],x[answer == 1,1],x[answer == 1,2], s = 40 , color = 'orange', label = "cluster 1")
ax.scatter(x[answer == 2,0],x[answer == 2,1],x[answer == 2,2], s = 40 , color = 'green', label = "cluster 2")
ax.scatter(x[answer == 3,0],x[answer == 3,1],x[answer == 3,2], s = 40 , color = '#D12B60', label = "cluster 3")
ax.scatter(x[answer == 4,0],x[answer == 4,1],x[answer == 4,2], s = 40 , color = 'purple', label = "cluster 4")
ax.scatter(x[answer == 5,0],x[answer == 5,1],x[answer == 5,2], s = 40 , color = 'black', label = "cluster 5")
ax.scatter(x[answer == 6,0],x[answer == 6,1],x[answer == 6,2], s = 40 , color = 'red', label = "cluster 6")

ax.set_xlabel('population rate-->')
ax.set_ylabel('Facility rate-->')
ax.set_zlabel('Slope rate-->')
ax.legend()
plt.show()

temp = df_merge.groupby([0]).mean()   
cluster_mean = temp.transpose()    
mean_table = cluster_mean.div(cluster_mean.max(axis=1), axis=0)    

plt.figure(figsize = (15, 10))    
sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
sns.heatmap(mean_table,    
	annot=True,    
            fmt='.3f',     
            linewidths = 0.1,     
            cmap = 'RdYlGn_r')   
plt.title('Cluster mean table', fontsize=13)
plt.show()


result_df3=pd.concat([case2,cluster],axis=1)
result_df3.to_csv("Clustering_DBSCAN.csv",encoding="EUC-KR")

# # GMM


from sklearn.mixture import GaussianMixture

cluster = GaussianMixture(n_components=5, random_state=42)
answer=cluster.fit_predict(case2_df2)

cluster= pd.DataFrame(cluster.fit_predict(case2_df2))

df_merge = pd.concat([df,cluster],axis=1)
df_merge.info()
df_merge.describe()

cluster_size = df_merge.groupby([0]).count()   
print(cluster_size)
cluster_size.plot(kind = 'bar')

x=case2_df2.values

fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[answer == 0,0],x[answer == 0,1],x[answer == 0,2], s = 40 , color = 'blue', label = "cluster 0")
ax.scatter(x[answer == 1,0],x[answer == 1,1],x[answer == 1,2], s = 40 , color = 'orange', label = "cluster 1")
ax.scatter(x[answer == 2,0],x[answer == 2,1],x[answer == 2,2], s = 40 , color = 'green', label = "cluster 2")
ax.scatter(x[answer == 3,0],x[answer == 3,1],x[answer == 3,2], s = 40 , color = '#D12B60', label = "cluster 3")
ax.scatter(x[answer == 4,0],x[answer == 4,1],x[answer == 4,2], s = 40 , color = 'purple', label = "cluster 4")

ax.set_xlabel('population rate-->')
ax.set_ylabel('Facility rate-->')
ax.set_zlabel('Slope rate-->')
ax.legend()
plt.show()

temp = df_merge.groupby([0]).mean()    
cluster_mean = temp.transpose()    
mean_table = cluster_mean.div(cluster_mean.max(axis=1), axis=0)   

plt.figure(figsize = (15, 10)) 
sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
sns.heatmap(mean_table,     
	annot=True,     
            fmt='.3f',  
            linewidths = 0.1,  
            cmap = 'RdYlGn_r')  
plt.title('Cluster mean table', fontsize=13)
plt.show()

result_df4=pd.concat([case2,cluster],axis=1)
result_df4.to_csv("Clustering_GMM.csv",encoding="EUC-KR")


