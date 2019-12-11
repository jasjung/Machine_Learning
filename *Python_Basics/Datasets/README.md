# Datasets 

Loading difference datasets in python. 

Reference: [https://keras.io/datasets/](https://keras.io/datasets/)

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


## IMDB 

```py 
from keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data(path="imdb.npz",
                                                      num_words=None,
                                                      skip_top=0,
                                                      maxlen=None,
                                                      seed=113,
                                                      start_char=1,
                                                      oov_char=2,
                                                      index_from=3)
```


## Rotten Tomatoes 

https://www.kaggle.com/c/movie-review-sentiment-analysis-kernels-only/data


## News20 

https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html

```py 
from sklearn.datasets import fetch_20newsgroups
# newsgroups_train = fetch_20newsgroups(subset='train')

newsgroups_train = fetch_20newsgroups(subset='train',
                                      remove=('headers', 'footers', 'quotes'))

# sample 
cats = ['alt.atheism', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
newsgroups_train


newsgroups_train.data
newsgroups_train.target
newsgroups_train.target_names
```

