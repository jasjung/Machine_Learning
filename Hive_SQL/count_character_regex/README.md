# count characters regex 

Reference: 

- https://stackoverflow.com/questions/37576308/how-to-check-if-a-string-cotains-only-number-in-sql-server
- https://stackoverflow.com/questions/11380329/finding-the-count-of-characters-and-numbers-in-a-string

## Count digits in a string 

```sql
LENGTH(regexp_replace(col,'[^0-9]+','' )) as num_count
```

## Count characters in a string 

```sql
LENGTH(regexp_replace(col,'[^a-zA-Z]+','' )) as char_count
```
