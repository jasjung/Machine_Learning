# Find Majority in a list 

https://stackoverflow.com/questions/33511259/finding-majority-votes-on-1s-1s-and-0s-in-list-python/33511352


```py 
from collections import Counter

def find_majority(votes):
    vote_count = Counter(votes)
    top_two = vote_count.most_common(2)
    if len(top_two)>1 and top_two[0][1] == top_two[1][1]:
        # It is a tie
        return 0
    return top_two[0][0]
```

my version 


```py 
from collections import Counter

def find_majority(votes):
    vote_count = Counter(votes)
    top_one = vote_count.most_common(1)
    return top_one[0][0]
```

