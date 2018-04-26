# Average 

### Quick Code 
```
rdd = sc.parallelize([['key1',1],['key1',2],['key1',5],['key2',4],['key2',9]])

# step 3 - average 
rdd.mapValues(lambda x: (x,1))\
    .reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1]))\
    .mapValues(lambda v: v[0]/v[1]).collect()
```