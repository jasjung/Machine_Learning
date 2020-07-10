# Upstream 

https://www.atlassian.com/git/tutorials/git-forks-and-upstreams

```sh
# to see if you have upstream 
git remote -v
# add upstream 
git remote add upstream git@<your git>.git
# check it's added 
git remote -v
# fetch from upstream 
git fetch upstream 
# pull ? 
git merge upstream/master 
```