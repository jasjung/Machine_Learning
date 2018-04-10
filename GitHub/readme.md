
# Github_Tricks 

## Tricks 

### Most Common 
```
# to pull
git pull origin master 

# to push 
git add . 
git commit -m 'update' 
git push origin master 
```

### Undo `git add .`

`git reset`


## Removing github commit history:
Source: 

- https://gist.github.com/stephenhardy/5470814
- https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository/13102849#13102849

```
git checkout --orphan newBranch
git add -A  # Add all files and commit them
git commit -m 'remove history'
git branch -D master  # Deletes the master branch
git branch -m master  # Rename the current branch to master
git push -f origin master  # Force push master branch to github
git gc --aggressive --prune=all     # remove the old files
```

## Useful links: 

- Markdown tricks: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
- https://help.github.com/articles/ignoring-files/

