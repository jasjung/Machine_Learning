# Hive Parameters 


### for faster running time 

This runs parallel jobs if your query has multiple stages that are not dependent upon each other. 

```sql 
SET hive.exec.parallel = true;
```
