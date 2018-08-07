# Datasets 

Loading difference datasets in python. 

## Iris 

```py
import numpy as np
import pandas as pd
from sklearn import datasets

# load data 
iris = datasets.load_iris()

# conver to pandas df 
df = pd.DataFrame(iris.data, columns=iris.feature_names)

labels = pd.Categorical.from_codes(iris.target, iris.target_names)
labels_tmp = pd.DataFrame(pd.Series(labels),columns=['y'])

# add labels to the dataframe 
df = pd.concat([df,labels_tmp],axis=1)

print(df.shape)
df.head()
```

## Boston House Price 

```py
from sklearn.datasets import load_boston
boston = load_boston()

print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

```

