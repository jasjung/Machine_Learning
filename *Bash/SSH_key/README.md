# SSH KEY

Reference: 

- https://adamdehaven.com/blog/how-to-generate-an-ssh-key-and-add-your-public-key-to-the-server-for-authentication/


See the list of current keys 

```sh
ls -al ~/.ssh
```

```sh
ssh-keygen
```

```
cat ~/.ssh/id_rsa.pub
```

```
ssh-add ~/.ssh/digitalocean
```

IP: `ssh root@[ip-address]`
