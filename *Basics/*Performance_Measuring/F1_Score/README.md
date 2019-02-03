# F1 Score 

Reference: 

- f1score: [https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)

```
F1 = 2 * (precision * recall) / (precision + recall)
```

```py
from sklearn.metrics import f1_score
y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
f1_score(y_true, y_pred, average='macro')  
# 0.26
f1_score(y_true, y_pred, average='micro')  
# 0.33
f1_score(y_true, y_pred, average='weighted')  
# 0.26
f1_score(y_true, y_pred, average=None)
# array([0.8, 0. , 0. ])
```
