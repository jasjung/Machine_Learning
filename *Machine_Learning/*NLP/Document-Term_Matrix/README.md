# Document Term Matrix  

```py
from sklearn.feature_extraction.text import CountVectorizer

docs = ['why hello there', 'omg hello pony', 'she went there? omg']
vec = CountVectorizer()
X = vec.fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
print(df)
```



Ref: https://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk