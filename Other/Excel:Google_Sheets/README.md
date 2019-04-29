# Excel

### Convert Date to Day of the Week 
```
=TEXT(WEEKDAY(A1), "ddd")

=CHOOSE(weekday(H1), "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
```

### Convert Month 1 -> 01. 

```
=text(a1,"00"). --> 01 
where a1 = 1
```
