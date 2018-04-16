# RegEx 

cheat_cheat: https://www.debuggex.com/cheatsheet/regex/python

## Guid 
- https://www.guidgenerator.com/online-guid-generator.aspx

```py
import re 

# randomly generated guid 
guid_ex = 'hi fb10a18b-063b-4efe-9d66-02b812f51ec0 there'

# works if there is space surrounding guid 
# pattern = r'^([0-9A-Fa-f]{8}[-][0-9A-Fa-f]{4}[-][0-9A-Fa-f]{4}[-][0-9A-Fa-f]{4}[-][0-9A-Fa-f]{12})$'

# works even if there is no space surrounding guid. 
pattern = r'([0-9A-Fa-f]{8}[-][0-9A-Fa-f]{4}[-][0-9A-Fa-f]{4}[-][0-9A-Fa-f]{4}[-][0-9A-Fa-f]{12})'

m = re.search(pattern , guid_ex) 

# returns all patterns that matched 
m.groups()
# Out: ('fb10a18b-063b-4efe-9d66-02b812f51ec0',)

# returns the first pattern that matched 
m.group(0)
# Out: 'fb10a18b-063b-4efe-9d66-02b812f51ec0'
```

## Website Pattern 
```py 
ex = ['www.hello.com', 'google.com', 'account.gmail.com', 'settings', 'profile']

# pattern for websites
pattern = r'[0-9A-Za-z]*\.{1}.*'

web = [i for i in ex if  re.search(pattern,i)]
web 

# Out[2]: ['www.hello.com', 'google.com', 'account.gmail.com']
```