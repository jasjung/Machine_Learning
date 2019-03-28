# Removing Duplicates From a Table

https://stackoverflow.com/questions/43280052/how-to-delete-duplicate-records-from-hive-table

```sql
insert overwrite table table.mine select distinct * from table.mine;
```
