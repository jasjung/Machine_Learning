# Utils 

## Binary Classification

```py
from sklearn.metrics import roc_auc_score,accuracy_score,f1_score
from sklearn.metrics import confusion_matrix, precision_score,recall_score

print('Accuracy :', round(accuracy_score(y_test, y_pred>.5),3))
print('ROC AUC  :', round(roc_auc_score(y_test, y_pred),3))
print('PR AUC   :', round(average_precision_score(y_test, y_pred),3))
print('F1 Score :', round(f1_score(y_test, y_pred>0.5),3))
print('Precision:', round(precision_score(y_test, y_pred>0.5),3))
print('Recall   :', round(recall_score(y_test, y_pred>0.5),3))
```


```py
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def jj_binary_score(y_test, y_pred, threshold=0.5):
    '''
    Computes various performance evaluation metric for binary classification 
    y_test: list of 1s and 0s 
    y_pred: list of predictions between 0 and 1 
    '''
    # convert prob to class
    y_pred_class = y_pred > threshold
    print(f'Scoring {len(y_test):,d} observations.')
    print('---------------------------')
    print('Accuracy :', round(accuracy_score(y_test, y_pred_class), 3))
    print('ROC AUC  :', round(roc_auc_score(y_test, y_pred), 3))
    print('PR AUC   :', round(average_precision_score(y_test, y_pred), 3))
    print('F1 Score :', round(f1_score(y_test, y_pred_class), 3))
    print('Precision:', round(precision_score(y_test, y_pred_class), 3))
    print('Recall   :', round(recall_score(y_test, y_pred_class), 3))

jj_binary_score(y_test,y_pred)
```