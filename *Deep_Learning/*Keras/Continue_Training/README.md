# Continue Training 

- https://stackoverflow.com/questions/36356004/continue-training-from-a-specific-epoch

Continue training from previous epochs

```py
model = Sequential()
model.add(...)
model.load_weights('path/to/weights.h5') # this is your previous weight
...
model.fit(...,initial_epoch='<your epoch number>') 
```
