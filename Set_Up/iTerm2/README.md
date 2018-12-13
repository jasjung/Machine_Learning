# iTerm2 Setup

## Changing key stroke behaviro 

- [https://apple.stackexchange.com/questions/154292/iterm-going-one-word-backwards-and-forwards](https://apple.stackexchange.com/questions/154292/iterm-going-one-word-backwards-and-forwards)
- [https://stackoverflow.com/questions/15733312/iterm2-delete-line](https://stackoverflow.com/questions/15733312/iterm2-delete-line)


```
Preferences > Profiles > Keys
```

### move forward one word

```
option+right
send escape
f
```

### move back one word

```
option+left
send escape
b
```

### delete to beginning of word 

```
option+delete
send hex code
0x1B 0x08
```

### delete the whole line 

```
fn+option+delete
send hex code
0x15
```