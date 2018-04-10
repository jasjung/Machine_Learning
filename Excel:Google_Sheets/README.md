# Excel

### Convert Date to Day of the Week 
```
=TEXT(WEEKDAY(A1), "ddd")

=CHOOSE(weekday(H1), "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
```