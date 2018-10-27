# FastText

Reference: 

- Official Website: [https://fasttext.cc](https://fasttext.cc)
- FastText: [https://medium.com/@ageitgey/text-classification-is-your-new-secret-weapon-7ca4fad15788](https://medium.com/@ageitgey/text-classification-is-your-new-secret-weapon-7ca4fad15788)
- Word2Vec_vs_FastText: [https://towardsdatascience.com/word-embedding-with-word2vec-and-fasttext-a209c1d3e12c](https://towardsdatascience.com/word-embedding-with-word2vec-and-fasttext-a209c1d3e12c)
- Sent2Vec: [https://github.com/epfml/sent2vec](https://github.com/epfml/sent2vec)
- Gensim\_Wrapper_Documentation: [https://radimrehurek.com/gensim/models/fasttext.html#module-gensim.models.fasttext](https://radimrehurek.com/gensim/models/fasttext.html#module-gensim.models.fasttext)
- Gensim\_Notebok_Tutorial: [https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/FastText_Tutorial.ipynb](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/FastText_Tutorial.ipynb)
- Tranfer_Learning: [https://blog.manash.me/how-to-use-pre-trained-word-vectors-from-facebooks-fasttext-a71e6d55f27](https://blog.manash.me/how-to-use-pre-trained-word-vectors-from-facebooks-fasttext-a71e6d55f27)
- FastText\_Trained_Models: [https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md)
- Precision Recall: [https://stackoverflow.com/questions/46129903/precision-and-recall-in-fasttext](https://stackoverflow.com/questions/46129903/precision-and-recall-in-fasttext)
- FastText\_Official\_Python_Wrapper: [https://github.com/facebookresearch/fastText/tree/master/python](https://github.com/facebookresearch/fastText/tree/master/python)

## OG Method 

```

```

## Gensim Wrapper

Using the Gensim Wrapper, you can use fasttext quite easily. 

```py 
from gensim.models import FastText
model = FastText(input_df, size=100, window=5, min_count=5, workers=4, sg=1)

model.wv.most_similar("Gastroenteritis")

model.wv.get_vector('hello')
```

```py 
print('night' in model_wrapper.wv.vocab)
print('nights' in model_wrapper.wv.vocab)
print(model_wrapper['night'])
print(model_wrapper['nights'])

model.wv.__contains__('hi')
```

### Reading Pretrained Embedding 

```py
from gensim.models import KeyedVectors
# Creating the model
en_model = KeyedVectors.load_word2vec_format('wiki.en/wiki.en.vec')
```

## Pypi 
ref: https://pypi.org/project/fasttext/

```sh 
pip install fasttext 
```

```py 
import fasttext

# Skipgram model
model = fasttext.skipgram('data.txt', 'model')
print model.words # list of words in dictionary

# CBOW model
model = fasttext.cbow('data.txt', 'model')
print model.words # list of words in dictionary
```
