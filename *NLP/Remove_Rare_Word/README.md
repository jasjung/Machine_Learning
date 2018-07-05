# Frequent or Rare Words

```py
# compute the frequency of each tokens or words 
freq = nltk.FreqDist(tokens) 

# show top 10 most frequent words 
sorted(freq.items(), key=lambda x: x[1],reverse=True)[:10]

# show top 10 least frequent words 
sorted(freq.items(), key=lambda x: x[1],reverse=True)[-10:]
```
