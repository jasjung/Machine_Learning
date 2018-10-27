# Kmeans 

This is my attempt to visualize kmeans clusters. 

```py 
# capping the std to deal with outliers 
feature_scaled.applymap(lambda x: min(x,10))
```

```py
# kmeans = cluster.KMeans(n_clusters=3)
# # scale data 
# kmeans.fit(preprocessing.scale(features))
# var = features.columns

def kmeans_plot(kmeans, variables, figsize=(10,5)): 

    # centroids 
    center = kmeans.cluster_centers_
    # number of clusters 
    k = kmeans.n_clusters
    # cluster size 
    cluster_size = (pd.Series(kmeans.labels_)).value_counts().sort_index()
    # for categorical plotting 
    xn = range(len(variables))
    # init plots 
    fig, axes = plt.subplots(1,k, sharey=True, sharex=True,figsize=(figsize))
    # number of plots = number of clusters 

    for i in range(k):
        # scatter plot 
        axes[i].scatter(center[i],xn,s=50)
        # Title 
        axes[i].set_title('Cluster %d' % (i+1), fontweight='bold',bbox={'facecolor':'gold', 'alpha':0.5, 'pad':2.9})
        # 
#         print((cluster_size[i]))
        axes[i].set_xlabel('Size:' + str(int(cluster_size[i])))
        # Grid 
        axes[i].grid(True)
        axes[i].set_facecolor('whitesmoke')
    # change y-axis name 
    plt.yticks(xn,variables)
    # remove space between subplots 
    plt.subplots_adjust(wspace=0, hspace=0)
    # set common xlabel     
    fig.text(0.5, -0.05, 'Cluster Means', fontsize=12, ha='center')
    #fig.set_facecolor("black")
    plt.show()
    plt.close()
    
kmeans_plot(km,dfkm.columns,figsize=(10,5))

# kmeans_plot(kmeans = kmeans, variables = var)
```
