# Dates 

## CURRENT_DATE 

You can get today's date using CURRENT_DATE variable in hive. It's very useful since you do not have to manually type it. Learn more about hidden variables. 

```sql
SELECT CURRENT_DATE;
SELECT DATE_SUB(CURRENT_DATE,1);
```


## Double Digit MONTH 

You can get month like this: 

```sql
SELECT MONTH(CURRENT_DATE); 
-- for double digit 
SELECT LPAD(MONTH(CURRENT_DATE),2,0);
```


