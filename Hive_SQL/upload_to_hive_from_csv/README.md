# How to upload to Hive from CSV file 


### Create Schema 

```sql 
use jason; 
drop table if exists jason.table;
create table jason.table (
	c1 string, 
	c2 string,
	c3 double
)
row format delimited fields terminated by ',' 
tblproperties("skip.header.line.count"="1"); 
```

may need 

```sql 
set hive.exec.dynamic.partition.mode=nonstrict;
```

### Load from CSV 

```sql 
LOAD DATA LOCAL INPATH 'your_file_path' OVERWRITE INTO TABLE jason.table;
```


### With Partition 

- https://stackoverflow.com/questions/45214291/loading-in-path-file-to-a-partitioned-table
- http://bigdataprogrammers.com/load-files-into-hive-partitioned-table/

```sql 
LOAD DATA LOCAL INPATH [your_file.csv] OVERWRITE INTO TABLE your.table PARTITION([partition_name]=[partition_value]);
```