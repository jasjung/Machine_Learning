# Delete Files with Certain Pattern

----

Reference: 

- https://askubuntu.com/questions/43709/how-do-i-remove-all-files-that-match-a-pattern
- https://stackoverflow.com/questions/20895290/count-number-of-files-within-a-directory-in-linux

----

I had duplicate files like these: 

- img.png
- img 1.png
- ... 

So I wanted to remove all the files with " 1". 

```
# to find the files with pattern
find . -name '* 1*'

# to count the number of these files 
find . -name '* 1*' | wc -l  

# to count the number of all files 
ls -1 | wc -l

# delete these files 
find . -name '* 1*' -delete
```
