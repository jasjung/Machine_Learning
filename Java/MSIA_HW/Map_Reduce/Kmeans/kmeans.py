import os 
import random
import numpy as np
import sys

''' Setup
Folders:

1. hw3/input
1.1   hw3/input/ex1/ -> contains clustering data
1.2   hw3/input/ex2/ -> contains medicaid data
2. hw3/centroid 
3. hw3/output 
'''

#%% 
# number of clusters 
k = int(sys.argv[1])
print("*** k:" , k)
# number of kmeans iterations to run 
max_iter = int(sys.argv[2])
print("*** iteration:" , max_iter)
ex = str(sys.argv[3])

# sample initial centroids into 
print("*** sample initial centroid")
#np.savetxt("centroids.txt", init, delimiter=' ')
if ex == "ex1":
    os.system("shuf -n " + str(k) + " clustering.txt > centroids.txt")
    print("***using clustering.txt")    
if ex == "ex2":
    os.system("shuf -n " + str(k) + " medicaid_clean_final.txt > centroids.txt")
    print("***using medicaid_clean_final.txt")    
# move centroids.txt into hdfs  
print("*** move centroids.txt into hdfs")
os.system("hdfs dfs -copyFromLocal centroids.txt")
# remove centroid folder 
os.system("hdfs dfs -rm -R hw3/centroid")
# make centroid folder
os.system("hdfs dfs -mkdir hw3/centroid")
# move centroids.txt to centroid folder 
os.system("hdfs dfs -mv centroids.txt hw3/centroid")

for i in range(max_iter):
    print("*** In %dth iteration" %(i+1) )
    # delete output folder
    print("*** REMOVE OUTPUT FOLDER")
    os.system("hdfs dfs -rm -R hw3/output")
    # run the jar code
    if ex== "ex1":
        os.system("yarn jar target/mr-app-1.0-SNAPSHOT.jar Kmeans hw3/input/ex1 hw3/output")
    if ex == "ex2":
        os.system("yarn jar target/mr-app-1.0-SNAPSHOT.jar Kmeans hw3/input/ex2 hw3/output")

    # concatenate all output files into centroid folder. It should override the previous file 
    print("*** producing new centroids.txt")
    #os.system("hdfs dfs -cat hw3/output/part* > hw3/centroid/centroids.txt")
    os.system("hdfs dfs -rm hw3/centroid/centroids.txt")
    os.system("hdfs dfs -cat hw3/output/part* | hdfs dfs -put - hw3/centroid/centroids.txt")
    # delete output folder
    os.system("hdfs dfs -rm -R hw3/output")

os.system("rm centroids.txt")
os.system("hdfs dfs -copyToLocal hw3/centroid/centroids.txt")
print("JASON: Done")
# then the file code should be inside centroid folder.

