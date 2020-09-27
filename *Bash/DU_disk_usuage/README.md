# DU disk usuage 

credit: https://www.ostechnix.com/find-size-directory-linux/

- s: summary 
- h: human 


to see a directory's disk usuage. 

```sh
# for your current directory 
du -sh 
# choose a specific directory 
du -sh <your directory> 
# 1G	<your directory>/
```

following will output all the sub directories 

```sh
du -h <your directory>
```

see sub-directories' disk usuage sorted 

```sh
du -h --max-depth=1 | sort -hr
```

