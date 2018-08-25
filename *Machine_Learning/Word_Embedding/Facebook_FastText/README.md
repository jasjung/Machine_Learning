# FastText

Reference: 

- Official Website: https://fasttext.cc
- FastText: https://medium.com/@ageitgey/text-classification-is-your-new-secret-weapon-7ca4fad15788
- Word2Vec_vs_FastText: https://towardsdatascience.com/word-embedding-with-word2vec-and-fasttext-a209c1d3e12c
- Sent2Vec: https://github.com/epfml/sent2vec

Using the Gensim Wrapper, you can use fasttext quite easily. 

```py 
from gensim.models import FastText
model_ted = FastText(sentences_ted, size=100, window=5, min_count=5, workers=4,sg=1)

model_ted.wv.most_similar("Gastroenteritis")
```