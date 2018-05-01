# timeit

```
import timeit 
np.mean(timeit.repeat(lambda: "-".join(str(n) for n in range(100)), repeat=100,number=100))
```

`number`: how many times you want to repeat the lambda function 
`repeat`: how many times you want to repeat the lambda function after applying the number parameter. 

