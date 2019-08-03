# Regression

When target is a continuous variable

- https://www.pyimagesearch.com/2019/01/21/regression-with-keras/
- https://machinelearningmastery.com/custom-metrics-deep-learning-keras-python/

quick code 

```py
model.add(Dense(1, activation="linear"))

model.compile(loss='mean_squared_error', optimizer='adam')

model.compile(loss='mean_squared_error', optimizer='adam',metrics=['mse', 'mae', 'mape'])

metrics=['mean_squared_error', 'mean_absolute_error', 'mean_absolute_percentage_error']

for i in metrics:
    plt.plot(history.history[i])
    plt.plot(history.history['val_'+i])
    plt.title(i)
    plt.ylabel(i)
    plt.xlabel('epoch')
    plt.legend([i,'val_'+i], loc='upper left')
	# plt.savefig('yo.png')
    plt.show()
    plt.close()
```

