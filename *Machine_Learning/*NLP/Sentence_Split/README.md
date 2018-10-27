# Split Sentences 

```py 
inputstring = ' This is an example sent. The sentence splitter will split on sent markers. Ohh really !!'
from nltk.tokenize import sent_tokenize
all_sent = sent_tokenize(inputstring)
print (all_sent)
# [' This is an example sent', 'The sentence splitter will split on markers.','Ohh really !!']
```

or use 

```py 
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tokenizer.tokenize(inputstring)
```