# Pickle 

Refernce: https://www.datacamp.com/community/tutorials/pickle-python-tutorial

## Save 
```
import pickle 

with open('test.pickle','wb') as f: 
    pickle.dump(savethisfile,f)

```
## Load 
```
with open('test.pickle','rb') as f: 
    var = pickle.load(f)
```