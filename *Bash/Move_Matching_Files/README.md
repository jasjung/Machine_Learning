# Move Matching Files 

- https://unix.stackexchange.com/questions/30693/how-can-you-move-or-copy-all-files-of-a-certain-type-to-a-directory-in-unix

```sh
# show all files with l in its name
find . -name '*l*.txt'
# ./testdir/dir2/l4.txt
# ./testdir/dir1/l1.txt
# ./testdir/dir1/l3.txt
# ./testdir/dir1/l2.txt

# show all files with r in its name
find . -name '*r*.txt'
# copy all files matching the pattern to a new directory
find . -name '*l*.txt' -exec sh -c 'cp -i "$@" "$0"' ./testdir/l_only {} +
```

## Usuage - Tesla 

I wanted to view all tesla left camera footages. The following code will move the files to a directory you choose. 


```sh
# ran inside `TeslaCam/`
find . -name '*left*.mp4' -exec sh -c 'mv -i "$@" "$0"' ./t {} +
```