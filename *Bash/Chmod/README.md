# chmod 

ref: 

- http://www.december.com/unix/ref/chmod.html
- https://support.rackspace.com/how-to/checking-linux-file-permissions-with-ls/

```
# to view the files 
ls -la 

# to change permission 
chmod <permission> <filename>

# eg 
# for user access only 
chmod 700 myfile.txt 

# gives access to everyone 
chmod 777 myfile.txt 
```

### Recursive 

```
chmod -R 755 /path/to/directory 
```

## Info 

```
Owner (you)
Group (a group of other users that you set up)
World (anyone else browsing around on the file system)

0 = no permissions whatsoever; this person cannot read, write, or execute the file
1 = execute only
2 = write only
3 = write and execute (1+2)
4 = read only
5 = read and execute (4+1)
6 = read and write (4+2)
7 = read and write and execute (4+2+1)
```


initial '-' signifies the type of file