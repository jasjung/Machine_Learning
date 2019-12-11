# English Dictionary 

Trying to see if a string is a word. 

- https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
- http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python
- https://github.com/dwyl/english-words
- https://wordnet.princeton.edu

```py 
with open("words_alpha.txt") as f:
    words = set(i.strip() for i in f)
print(len(words))

def is_english_word(word):
    return word in english_words

print (is_english_word("ham"))  
```

