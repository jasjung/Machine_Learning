
# Auto Push & Pull 

## Version 1
It became very repetitive that I had to pull and push github folders very often. I didn't want to keep typing the same commands such as 

```
git add . 
git commit -m 'sth'
git push origin master 
```

Thus, I created this simple script file. Also, I created a shortcut from `iterm2` so that it will automatically run these scripts. For example, I can type Command+A and it will run `git_push.sh` script. 

## Version 2 
But what if I want to change the commit message? We will solve that by creating a python file that takes in command line argument and runs a git command. 

coming soon. 