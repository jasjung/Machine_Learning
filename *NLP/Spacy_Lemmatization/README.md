# Spacy

[spacy.io](https://spacy.io)


## Set up 

```sh 
pip install spacy 

python -m spacy download en 
```

## Lemmatization 

```py 
import spacy
spacy_lemma = spacy.load('en', disable=['parser', 'ner'])

t = spacy_lemma('how are you jason? There are many birds here.')

for i in t:
    print(i.lemma_)
    
#out how,be,-PRON-,jason,?,there,be,many,bird,here,.
```
