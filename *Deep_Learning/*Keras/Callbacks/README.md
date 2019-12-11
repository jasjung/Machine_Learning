# Callbacks 

## CSVLogger 

- https://keras.io/callbacks/#csvlogger
- https://stackoverflow.com/questions/38445982/how-to-log-keras-loss-output-to-a-file

```py
from keras.callbacks import CSVLogger
csv_logger = CSVLogger('training.log')
model.fit(X_train, Y_train, callbacks=[csv_logger])
or 
from keras.callbacks import CSVLogger
csv_logger = CSVLogger('log.csv', append=True, separator=';')
model.fit(X_train, Y_train, callbacks=[csv_logger])
```

