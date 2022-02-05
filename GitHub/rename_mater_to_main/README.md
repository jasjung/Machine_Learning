# rename master to main

to keep up with the trend, lets rename the master branch to main.

https://www.git-tower.com/learn/git/faq/git-rename-master-to-main

```sh
# Switch to the "master" branch:
git checkout master

# Rename it to "main":
git branch -m master main

git push -u origin main

# go to settings in the web to make default branch as main

# delete master branch
git push origin :master
```
