# Batch Read Large File 

```py 
import pandas as pd 
for chunk in pd.read_csv(filename, chunksize=chunksize):
    process(chunk)
```