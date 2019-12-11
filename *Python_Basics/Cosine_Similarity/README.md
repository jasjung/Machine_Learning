# Cosine Similarity 

## Quick Reference 

```py 
from sklearn.metrics.pairwise import cosine_similarity

e1 = [1,1,1,0,0,0]
e2 = [1,0,0,1,0,0]
cosine_similarity([e1,e2])

from scipy import spatial
1 - spatial.distance.cosine(e1,e2)
```

