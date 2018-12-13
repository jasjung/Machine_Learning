# Remove Punctuation 

```py 
# get punctuatiosn from string package 
import string 
print(string.punctuation)
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# remove punctuation 
translation = str.maketrans('','',string.punctuation)

s = "hello! what is your name?"
print(s.translate(translation))
# hello what is your name
```
