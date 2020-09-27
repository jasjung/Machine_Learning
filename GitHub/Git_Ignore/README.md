# Git Ignore

- https://help.github.com/articles/ignoring-files/
- https://gist.github.com/subfuzion/db7f57fff2fb6998a16c


## Global 

Run the following command to create .gitignore_global file 

```sh 
# past 
# git config --global core.excludesfile ~/.gitignore_global
# vi ~/.gitignore_global

# new 
git config --global core.excludesfile ~/.gitignore
vi ~/.gitignore
```

add the following into the .gitignore_global or .gitignore: 


### Examples 

```sh 
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
.ipynb_checkpoints 
spark-warehouse*
.Rapp.history
.Rhistory
__pycache__
*.pyc
*.RData
```

## Local 

```sh 
touch .gitignore
vi .gitignore
```

## Git Ignore Caches 

- https://stackoverflow.com/questions/1139762/ignore-files-that-have-already-been-committed-to-a-git-repository

```
git rm -r --cached .
git add .
git commit -m ".gitignore is now working"
```

# Deleting hidden files recrusively

Source: https://jonbellah.com/articles/recursively-remove-ds-store/

- cd to/your/directory
- To View the names file 
	- find . -name '.DS_Store' 
- To Delete them: 
	- find . -name '.DS_Store' -type f -delete
- To Delete hidden directories: 
	- find . -name '.ipynb_checkpoints'
		- to see which folders have checkpoints
	- rm -r `find . -name '.ipynb_checkpoints'`
		- (there is ` character in the command above. Copy from the raw file)
	- Make sure there are no spaces in the sub folders 



