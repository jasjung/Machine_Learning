# Keeping Only Alpha Numeric Characters

```py
import re, string
pattern = re.compile('[\W_]+')
pattern.sub('', string.printable)
```

