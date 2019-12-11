# Matplotlib

### Stlye 

```py 
import matplotlib.style as style
# style.available
style.use('fivethirtyeight')
```

### FigSize

```py
plt.figure(figsize=(20,5))
```

```py
plt.close()
plt.figure(figsize=(20,5))
plt.hist(tmp,bins=300)
plt.title('histogram')
plt.ylabel('count')
plt.xlabel('number of words')
plt.show()
```

### Xticks 

```py 
plt.xticks(rotation='vertical')
```

### Legends 

```py 
plt.plot(x,y,label='hi')
plt.legend()
```
