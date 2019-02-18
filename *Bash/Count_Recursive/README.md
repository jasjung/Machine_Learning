# Count all PDFs in a folder

https://stackoverflow.com/questions/9157138/recursively-counting-files-in-a-linux-directory

```
find [path] -name '*.pdf' | wc -l 
# ex
find . -name '*.pdf' | wc -l 
```
