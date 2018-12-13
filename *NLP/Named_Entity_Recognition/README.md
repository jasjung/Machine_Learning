# NER 


Reference: 

- https://nlp.stanford.edu/software/CRF-NER.shtml#Download
- https://stackoverflow.com/questions/20290870/improving-the-extraction-of-human-names-with-nltk
- download: https://nlp.stanford.edu/software/stanford-ner-2018-02-27.zip

To run the file, first unzip the file you just downloaded and put it in the same working directory as your py file. 

1. `english.all.3class.distsim.crf.ser.gz`: 3 class model for recognizing locations, persons, and organizations
2. `stanford-ner.jar` is needed since the classifier is written in java. 

```py 
from nltk.tag.stanford import StanfordNERTagger

# loads up the model 
st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')

st.tag(['hi','jason'])
# [('hi', 'O'), ('jason', 'PERSON')]
```

```py
for sent in nltk.sent_tokenize(text):
    tokens = nltk.tokenize.word_tokenize(sent)
    tags = st.tag(tokens)
    for tag in tags:
        if tag[1]=='PERSON': print (tag)
```