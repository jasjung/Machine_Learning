# Chicago Crime 

Part of MSIA HW Assignment in Hadoop Class. 

## Assignment: 

1. By using SparkSQL generate a histogram of average crime events by month. Find an explanation of results. (10 pts)
2. By using plain Spark (no Spark SQL): (1) find the top 10 blocks in crime events in the last 3 years; (2) find the two beats that are adjacent with the highest correlation in the number of crime events (this will require you looking at the map to determine if the correlated beats are adjacent to each other) over the last 5 years (3) establish if the number of crime events is different between Majors Daly and Emanuel at a granularity of your choice (not only at the city level). Find an explanation of results. (20 pts)
3. Predict the number of crime events in the next week at the beat level. The higher the IUCR is, the more severe the crime is. Violent crime events are more important and thus it is desirable that they are forecasted more accurately. (45 pts) You are encouraged to bring in additional data sets. (extra 50 pts if you mix the existing data with an exogenous data set) Report the accuracy of your models.
4. Find patterns of crimes with arrest with respect to time of the day, day of the week, and month. (25 pts)