# Levenshtein

https://www.datacamp.com/community/tutorials/fuzzy-string-python

```sh 
pip install python-levenshtein
```

```py 
import Levenshtein as lev

Str1 = "Apple Inc."
Str2 = "apple Inc"
Distance = lev.distance(Str1.lower(),Str2.lower()),
print(Distance)
Ratio = lev.ratio(Str1.lower(),Str2.lower())
print(Ratio)
```