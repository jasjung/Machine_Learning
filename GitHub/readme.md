
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
git commit -m 'second update' # 'remove history'
git branch -D master  # Deletes the master branch
git branch -m master  # Rename the current branch to master
git push -f origin master  # Force push master branch to github
git gc --aggressive --prune=all     # remove the old files
```

## Useful links: 

- Markdown tricks: 
	- https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
	- https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
- https://help.github.com/articles/ignoring-files/

## Make Your Website 
```
https://pages.github.com
```

## Removing Large File Cache from Commit History 

When you try to upload a large file, you will fail to push. Even after you delete those files, you will still not be able to push because those large files are cached in history. The following is a way to remove them. 

[Reference 1](https://stackoverflow.com/questions/2100907/how-to-remove-delete-a-large-file-from-commit-history-in-git-repository)

```
git filter-branch --tree-filter 'rm -f file/location' HEAD
```

[Reference 2](https://stackoverflow.com/questions/19573031/cant-push-to-github-because-of-large-file-which-i-already-deleted?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)


```
git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch <file/dir>' HEAD

# if you have more than one, you need to force it with -f
git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch <file/dir>' -f HEAD

# replace <file/dir> with your file's location 
```

[Reference 3](https://stackoverflow.com/questions/19573031/cant-push-to-github-because-of-large-file-which-i-already-deleted/23657759#23657759)

```
git rm --cached giant_file
    # Stage our giant file for removal, but leave it on disk
git commit --amend -CHEAD
    # Amend the previous commit with your change
    # Simply making a new commit won't work, as you need
    # to remove the file from the unpushed history as well
git push
    # Push our rewritten, smaller commit
```

## Branching
```
git clheckout -b my_branch # -b if the new branch does not exist
# do your dev work
git add .
git commit -m 'yo'
git push origin my_branch
# review pull requests on github.com
```

### Merge branch from terminal 

coming soon 

```

```






