
# Hive/SQL Tricks 

## Hive Specific 
### Duplicate Column Name Issue
- https://community.hortonworks.com/articles/43510/excluding-duplicate-key-columns-from-hive-using-re.html

```
set hive.support.quoted.identifiers=none;
select t1.*, t2.`(shopper_id)?+.+` from t1,t2 ;
```

## Basics 
### Create table 
```
# use orc or parquet 

use user_name;
drop table if exists user_name.table_name;
create table user_name.table_name stored as orc as 
```

### Change table name 
```
ALTER TABLE user.old_name RENAME TO user.new_name;
```

### Saving Hive Table from Command Line 
```
# use -f to run hive file 
hive -e "select * from table;" > output.txt
```

### Show Column Names in Hive Command Line 
```
set hive.cli.print.header=true;
-- hide col name
set hive.cli.print.header=false;
```

### RAND() Function 
```sql 
-- randomly sample 100 rows 
select * 
from table 
order by RAND()
limit 100;

-- add rand with seed so that you can random sample your large table for training the model 

create table as 
(select *, RAND(1) as rand 
from table);

select * from table 
where rand < 0.03 

```

### Remove Table Name From Column Header 
- Source: https://issues.apache.org/jira/browse/HIVE-14387

```
set hive.resultset.use.unique.column.names=false;
```

### Split Row Into N Chunks 
```
-- N = 10
select score, ntile(10) over (order by score) AS tile_10 from data;
-- Then you can group by tile_10 to get insights on tile specific information 
```

### How to Score using Logistic Regression Output from R/Python
```sql
-- given coef1, coef2, var1, var2, intercept

WITH t1 AS (
SELECT 
	*
	, (intercept + coef1*var1 + coef2*var2) AS logit
FROM table 
) 
SELECT 
	* 
	, 1/(1+exp(-logit)) AS score
FROM t1;
```

### Percentile / Median 
```
-- median 
PERCENTILE_APPROX(column_name, 0.5)
```

### Day of the Week 
```
-- Shortened Name 
from_unixtime(unix_timestamp('2017-02-23','yy-MM-dd'),'EEE')
-- Full Name 
from_unixtime(unix_timestamp('2017-02-23','yy-MM-dd'),'EEEE')
```

### Convert Array to String 
```
-- convert an array ['a','b','c'] to 'a,b,c'
select concat_ws(',',array_col)
from table;  
```

### Explode table 
```
-- coming soon
```

### Other 
```
concat_ws() 
collect_list() 
```

### Change Column Name 
- [Reference](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-ChangeColumnName/Type/Position/Comment)

```
CREATE TABLE test_change (a int, b int, c int);
 
// First change column a's name to a1.
ALTER TABLE test_change CHANGE a a1 INT;
```