# Drop Table or Purge 


## SQL Command 

```sql
-- move data to trash 
DROP TABLE IF EXISTS table_name; 
-- even removes from trash 
DROP TABLE IF EXISTS table_name PURGE; 
```


## From hadoop 

Delete from trash 

```sh 
hadoop fs -rm -r -f .Trash/*
```

See your hadoop usuage 

```sh
hadoop fs -du -h /user/<username>/
```

