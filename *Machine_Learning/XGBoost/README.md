# XGBOOST - Extreme Gradient Boosting 

- https://www.kaggle.com/dansbecker/xgboost
- https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d
- https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/
- https://www.analyticsvidhya.com/blog/2018/09/an-end-to-end-guide-to-understand-the-math-behind-xgboost/
- https://xgboost.ai/about
- https://www.youtube.com/watch?v=OtD8wVaFm6E


XGBoost is an implementation of the Gradient Boosted Decision Trees algorithm (scikit-learn has another version of this algorithm, but XGBoost has some technical advantages.) What is Gradient Boosted Decision Trees? We'll walk through a diagram.

We go through cycles that repeatedly builds new models and combines them into an ensemble model. We start the cycle by calculating the errors for each observation in the dataset. We then build a new model to predict those. We add predictions from this error-predicting model to the "ensemble of models."

https://xgboost.readthedocs.io/en/latest/build.html

```sh 
# in mac 
brew install libomp
pip3 install xgboost
```

```py 
import xgboost as xgb
# read in data
dtrain = xgb.DMatrix('demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('demo/data/agaricus.txt.test')
# specify parameters via map
param = {'max_depth':2, 'eta':1, 'objective':'binary:logistic' }
num_round = 2
bst = xgb.train(param, dtrain, num_round)
# make prediction
preds = bst.predict(dtest)
``` 

## Parameters 

- learning_rate: step size shrinkage used to prevent overfitting. Range is [0,1]
max_depth: determines how deeply each tree is allowed to grow during any boosting round.
- subsample: percentage of samples used per tree. Low value can lead to underfitting.
- colsample_bytree: percentage of features used per tree. High value can lead to overfitting.
- n_estimators: number of trees you want to build.
- objective: determines the loss function to be used like reg:linear for regression problems, reg:logistic for classification problems with only decision, binary:logistic for classification problems with probability.
- gamma: controls whether a given node will split based on the expected reduction in loss after the split. A higher value leads to fewer splits. Supported only for tree-based learners.
- alpha: L1 regularization on leaf weights. A large value leads to more regularization.
- lambda: L2 regularization on leaf weights and is smoother than L1 regularization.


## Fit (Sklearn) vs Train (Xgboost Native)

- https://www.kaggle.com/questions-and-answers/65417
- xgboost.XGBRegressor.fit and xgboost.Classifier.fit is the scikit-compatible api. It accepts pandas df or numpy arrays as input and works with the scikit objects such as RandomizedSearchCV. 
- xgboost.train and xgboost.cv are the xgboost specific training and cross validation methods. 

### Train 

```py 
import xgboost as xgb

dtrain = xgb.DMatrix(data=X_train.values,
                     feature_names=X_train.columns,
                     label=y_train.values)
dvalid = xgb.DMatrix(data=X_valid.values,
                     feature_names=X_valid.columns,
                     label=y_valid.values)

mod = xgb.train(params=params,
                dtrain=dtrain,
                num_boost_round=10000,
                early_stopping_rounds=100,
                evals=[(dvalid,'valid'), (dtrain,'train')],
                verbose_eval=20)
```

### Fit 

```py
import xgboost as xgb
from sklearn.model_selection import RandomizedSearchCV

xgb_scikit = xgb.XGBClassifier(verbose=0,
                               objective='binary:logistic',
                               n_jobs=-2)

xgb_grid = RandomizedSearchCV(xgb_scikit, 
                              params,
                              cv=5,
                              n_jobs=-2,
                              verbose=1,
                              n_iter=20)
xgb_grid.fit(X, y)
```

## Plot Tree 

Install dependency 

```sh 
conda install python-graphviz
```

```py
import matplotlib.pyplot as plt

xgb.plot_tree(model,num_trees=0)
# plt.rcParams['figure.figsize'] = [50, 10]
plt.show()
```

## Feature Importance 

```py
xgb.plot_importance(model)
plt.rcParams['figure.figsize'] = [5, 5]
plt.show()
```