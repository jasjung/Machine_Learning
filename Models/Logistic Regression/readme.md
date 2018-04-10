# Logistic Regression 
Useful codes 

## Sources: 
- https://elitedatascience.com/imbalanced-classes
- http://scikit-learn.org/stable/modules/cross_validation.html
- https://towardsdatascience.com/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a
- https://www.kaggle.com/hadend/tuning-random-forest-parameters
- https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74
- http://blog.datadive.net/selecting-good-features-part-iii-random-forests/
- xgboost: https://jessesw.com/XG-Boost/
- RF: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
- logistic: https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8


## Examples 

### Packages 
```python
# Import packages 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

from sklearn.utils import resample

### LOGISTIC 
from sklearn import model_selection 
from sklearn.model_selection import cross_val_score 

from sklearn import preprocessing
#plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

import statsmodels.api as sm
#from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

### RANDOM FOREST 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
```

### Null Analysis
```python
df.apply(lambda x: sum(x.isnull()))
```

### Correlations 
```python
corr_matrix = df.corr().abs()
# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
# Find index of feature columns with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
to_drop

plt.close()
sns.heatmap(df[di_cols_new].corr())
plt.show()
```

### Variance 
```python
variance = df[di_cols_new].var()
to_drop_var = list(variance[variance==0].index.values)
to_drop_var
```

### Examine Variables 
```python
plt.close()
for i in features:
    print(i)
    df[i].hist()
    plt.show()
```

### Confusion Matrix
```python
def confusion(y,y_hat): 
    '''
    function that creates confusion matrix 
    y = original dependent variable 
    y_hat = predicted dependent variable 
    '''
    # confusion matrix 
    table = pd.crosstab(y, y_hat, margins=True)

    print(table)
    print()

    if table.shape == (3,3): 
        # accuracy =(TP + TN ) / All 
        accuracy = (table.iloc[0,0] + table.iloc[1,1])/(table.iloc[2,2])
        print('accuracy  ' + str(accuracy))
        # precision = true positive / true positive + false positive 
        precision = table.iloc[1,1]/(table.iloc[2,1])
        print('precision ' + str(precision))
        # recall = true positive / true positive + false negative
        recall = table.iloc[1,1]/(table.iloc[1,2])
        print('recall    ' + str(recall))
        # f1-score = 2*Precision*Recall/(Precision+Recall)
        fscore = 2*precision*recall/(precision+recall)
        print('f1-score  ' + str(fscore))        
    else: 
        print(table.shape)
        print('table shape is not full')
```

### Split Dataframe
```python
def split_df(df,x,y):
    #print('\n*** Start of Split_Df function ***') 
    '''
    df = df you want to split 
    x = list of feature column names 
    y = name of dependent variable as a list 
    '''
    x_train, x_test, y_train, y_test = train_test_split(df[x], df[y], test_size=0.20, random_state=0)
    return x_train, x_test, np.ravel(y_train), np.ravel(y_test)
```

### Balance Dataset 
```python
def balance(df):
    print('\n*** Start of Balance function ***')

    # Separate majority (0) and minority (1) classes
    df_majority = df[df.y==0]
    df_minority = df[df.y==1]

    # Upsample minority class
    df_minority_upsampled = resample(df_minority, 
                                     replace=True,     # sample with replacement
                                     n_samples=len(df_majority),    # to match majority class
                                     random_state=0) # reproducible results

    # Combine majority class with upsampled minority class
    df = pd.concat([df_majority, df_minority_upsampled])

    # Display new class counts
    print(df.y.value_counts())

    return df 
```

### Logistic Model
```python
def jj_model(df, df_hold, model): 
    
    # split test/train 
    x_train, x_test, y_train, y_test = split_df(df, features, ['y'])
    x_hold, y_hold = df_hold[features], df_hold['y']
    
    if model == 'logistic': 
        print('logistic regression result\n')
    
        # instance of the model 
        model = LogisticRegression(random_state = 0, penalty='l1')
        model.fit(x_train, y_train)
        y_hat = model.predict(x_test)
        print('intercept' + str(model.intercept_))

        # train on entire train data before split_df
        model_all = LogisticRegression(random_state = 0, penalty='l1')
        model_all.fit(df[features], df['y'])
        y_hat_all = model_all.predict(x_hold)
        print('intercept' + str(model_all.intercept_))

        # Model Summary 
        logit_model=sm.Logit(df.y, df[features])
        result=logit_model.fit()

        
    elif model == 'rf':
        print('random forest result\n')
        model = RandomForestClassifier(random_state = 0,n_estimators=100)
        model.fit(x_train, y_train)
        y_hat = model.predict(x_test)
        '''
        {'bootstrap': False,
         'max_depth': 35,
         'max_features': 'sqrt',
         'min_samples_leaf': 1,
         'min_samples_split': 5,
         'n_estimators': 500}
        '''
    else: 
        print('error') 
        return 
    
    print('#'*100)
    print('confusion matrix of training data')
    confusion(y=y_test,y_hat=y_hat)
    print()
    print('#'*100)
    
    print('confusion matrix of 0107 data agaist 0108') 
    confusion(y=y_hold, y_hat=y_hat_all)
    print()
    print('#'*100)

    auc = roc_auc_score(y_test, y_hat)
    auc_hold = roc_auc_score(y_hold, y_hat_all)
    #results = model_selection.cross_val_score(model, df[features], df['y'],cv=10, scoring='accuracy')    

    print('AUC Test Set     ' + str(auc))
    print('AUC Holdout Se dt  ' + str(auc_hold))

    print('#'*100)
    print('Model Summary')
    print(result.summary())
    
jj_model(df_upsampled,df_hold_out,model='logistic')
```

