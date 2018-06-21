# AUC 

```
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score

accuracy = accuracy_score(y_test, y_pred)
pr_auc = average_precision_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)
```

Another method of computing pr-auc score 

```
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc

precision, recall, thresholds = precision_recall_curve(y_test, y_pred)

# same as average_precision_score
pr_auc = auc(recall, precision)
```
## ROC-AUC 
Refernece: 

- http://www.dataschool.io/roc-curves-and-auc-explained/

## PR-AUC 

References: 

- http://pages.cs.wisc.edu/~jdavis/davisgoadrichcamera2.pdf
- https://andybeger.com/2015/03/16/precision-recall-curves/
- http://www.chioka.in/differences-between-roc-auc-and-pr-auc/
- https://classeval.wordpress.com/introduction/introduction-to-the-precision-recall-plot/
- https://www.kaggle.com/general/7517#post41179

### Plotting PR-AUC 

```
import matplotlib.pyplot as plt
precision, recall, thresholds = precision_recall_curve(y_test, y_pred)

plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2,
                 color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))

```