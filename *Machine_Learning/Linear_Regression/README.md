# Linear Regression

reference: 

- regression: [https://becominghuman.ai/stats-models-vs-sklearn-for-linear-regression-f19df95ad99b](https://becominghuman.ai/stats-models-vs-sklearn-for-linear-regression-f19df95ad99b)
- r_squared: [https://stackoverflow.com/questions/42033720/python-sklearn-multiple-linear-regression-display-r-squared](https://stackoverflow.com/questions/42033720/python-sklearn-multiple-linear-regression-display-r-squared)

```py 
from sklearn import datasets
from sklearn import linear_model 
from sklearn.metrics import r2_score
import statsmodels.api as sm

x = iris['petal length (cm)'].values.reshape(-1,1)
y = iris['petal width (cm)'].values.reshape(-1,1)

# SKLEARN 
model = linear_model.LinearRegression()
model.fit(x,y)

# STATSMODELS
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
```

Logistic Regression in STATSMODELS

```py 
model = sm.Logit(y, x).fit()
```