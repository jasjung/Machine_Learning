# Split Train Test Val 

https://datascience.stackexchange.com/questions/15135/train-test-validation-set-splitting-in-sklearn

```py
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)
```