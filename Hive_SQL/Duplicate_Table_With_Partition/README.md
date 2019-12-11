# Duplicate_Table_With_Partition

https://stackoverflow.com/questions/24211372/loading-data-from-one-hive-table-to-another-with-partition

```sql 
set hive.exec.dynamic.partition.mode=nonstrict;

use your_username; 

-- copy schema 
drop table if exists your_table_new;
CREATE TABLE your_table_new
LIKE your_table_old;

-- fill table 
insert overwrite table your_table_new PARTITION (your_partition)
select * from your_table_old;  
```
