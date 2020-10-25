# SSH and Github

Sometimes you have to use SSH instead of HTTPS for your git remote setup. 


### Change setting from HTTPS to SSH 

https://stackoverflow.com/questions/14762034/push-to-github-without-a-password-using-ssh-key

```sh
git remote set-url origin git@github.com:<Username>/<Project>.git
```

### Generate new ssh key for Mac 

- https://docs.github.com/en/enterprise-server@2.21/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key
- https://docs.github.com/en/enterprise-server@2.21/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval "$(ssh-agent -s)"
open ~/.ssh/config
# add the following 
# Host *
#   AddKeysToAgent yes
#   UseKeychain yes
#   IdentityFile ~/.ssh/id_rsa
ssh-add -K ~/.ssh/id_rsa

# Add the ssh key to github account 
pbcopy < ~/.ssh/id_rsa.pub
# then paste to the corresponding section 
```
