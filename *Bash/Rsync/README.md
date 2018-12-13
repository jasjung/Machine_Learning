# Rsync

---
*Public Repo*

---

References 

- [https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)

## Note

- `rsync -azh localfile.csv servername:/home/username/..`
- `rsync -azh servername:/home/username/file.csv /Users/username/folder`
- Run `bash rync.sh` to sync your folder 

## sync.sh

```
#!/usr/bin/env bash

directory=`pwd`
#echo $directory
base=`basename $directory`
echo "updating prod:projects/$base"

rsync -avzh --progress $directory prod:/home/username/projects/
```

To run 

```
bash sync.sh
```
