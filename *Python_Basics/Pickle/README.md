# Pickle 

Refernce: https://www.datacamp.com/community/tutorials/pickle-python-tutorial

### Save 
```
import pickle 

with open('test.pickle','wb') as f: 
    pickle.dump(savethisfile,f)
    
# or 
pickle.dump(model, open(filename, 'wb'))

```
### Load 
```
with open('test.pickle','rb') as f: 
    var = pickle.load(f)
    
# or 
loaded_model = pickle.load(open(filename, 'rb'))
```

## Pandas Way 

```py 
import pandas as pd 
# save
pd.Series(your_list).to_pickle('your_list.pickle')
# load 
pd.read_pickle('your_list.pickle')
```