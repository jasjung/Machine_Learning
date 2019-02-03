# Find Hive Table File Path 

https://stackoverflow.com/questions/13178182/i-have-created-a-table-in-hive-i-would-like-to-know-which-directory-my-table-is/30168534

```sql
show create table table_name;
```

You will find the location under `location`.  