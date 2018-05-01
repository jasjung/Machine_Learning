# Bash Tricks 

## Accessing Files 
- Source: http://bconnelly.net/working-with-csvs-on-the-command-line/
- `head input.csv`: view first 10 lines of the file 
- `head -n 7 input.csv`: specify number of lines to view 
- `head -n 100 input.csv > output.csv`: save first 100 lines to outout.csv. If you rerun, the existing file is replaced. 
- `head -n 100 input.csv >> output.csv`: appends to existing file.
- `wc -l input.csv`: count number of lines.
- `less log.log`: fast way to view-only file. 
- `tail -f log.log`: view live update of the log file. 


## Screen Function 
- Source: https://linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions/
- type `screen` to start persistent terminal sessions 
- to exit, press `cntrl + a + d`
- to return to the latest screen session, type `screen -r`
- type `screen -ls` to see list of screen sessions
- press `control + a ` then type `:quit` to quit the screen session while you are in the session. 
- `killall SCREEN` to kill all screens 

## Server Trikcs 
- `hostname`: to see the current server host name 

## Rsync 
- `rsync -azh localfile.csv servername:/home/username/..`
- `rsync -azh servername:/home/username/file.csv /Users/username/folder`
- Run `bash rync.sh` to sync your folder 

```
# sync.sh
#!/usr/bin/env bash

directory=`pwd`
#echo $directory
base=`basename $directory`
echo "updating prod:projects/$base"

rsync -azh $directory prod:/home/username/projects/
```

## SCP 
- `scp file_to_trasnfer.txt servername:/home/username/location_to_transfer` 

## Hadoop 
- `hadoop fs -du -h`: folder size in human readable format 
- `hdfs dfs -du -s -h /user/[user_name]`: find out how much data in the user's folder
- `yarn application -kill [application_id]`: to kill your spark job

## Print 
```
# Python's print() equivalent in shell scripting is echo 
echo 'hello world' 
# prints hello world
```

## Other Links 
- https://unix.stackexchange.com/questions/159489/is-there-a-difference-between-and-and

## Command Line Argument 

- [credit](https://unix.stackexchange.com/questions/31414/how-can-i-pass-a-command-line-argument-into-a-shell-script?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

```
$ cat myscript
#!/bin/bash
echo "First arg: $1"
echo "Second arg: $2"
$ ./myscript hello world
First arg: hello
Second arg: world
```