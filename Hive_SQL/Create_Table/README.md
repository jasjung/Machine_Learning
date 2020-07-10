# Create Table 

### Drop or Create table 

```sql 
# use orc or parquet 
USE user_name;
DROP TABLE IF EXISTS user_name.table_name;
CREATE TABLE user_name.table_name stored AS orc AS 
```

### Change table name 

```sql
ALTER TABLE user.old_name RENAME TO user.new_name;
```