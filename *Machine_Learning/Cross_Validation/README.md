# Cross Validation 

Reference

- https://www.kaggle.com/kanncaa1/roc-curve-with-k-fold-cv
- https://stats.stackexchange.com/questions/52274/how-to-choose-a-predictive-model-after-k-fold-cross-validation 

Example of using semi-custom cross-validation to measure ROC AUC and PR AUC with random frest classifer 

```py 
from sklearn.model_selection import StratifiedKFold

clf = RandomForestClassifier(random_state=0)
cv = StratifiedKFold(n_splits=5,shuffle=False)

x = 'your input features' 
y = 'your target variable' 

cv_roc_auc=[]
cv_pr_auc=[]

count = 0 

for train,test in cv.split(x,y):
    print(count)
    
    prediction = clf.fit(x.iloc[train],y.iloc[train]).predict_proba(x.iloc[test])[:,1]

    cv_roc_auc.append(roc_auc_score(y.iloc[test], prediction))
    cv_pr_auc.append(average_precision_score(y.iloc[test], prediction))
    
    count += 1 

print('Average ROC AUC Score:',np.mean(cv_roc_auc))
print('Average PR AUC Score: ',np.mean(cv_pr_auc))

```
