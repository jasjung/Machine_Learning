# Bash Tricks 

Reference

- Cheatsheet: [https://devhints.io/bash](https://devhints.io/bash)

## Accessing Files 
- Source: http://bconnelly.net/working-with-csvs-on-the-command-line/
- `head input.csv`: view first 10 lines of the file 
- `head -n 7 input.csv`: specify number of lines to view 
- `head -n 100 input.csv > output.csv`: save first 100 lines to outout.csv. If you rerun, the existing file is replaced. 
- `head -n 100 input.csv >> output.csv`: appends to existing file.
- `wc -l input.csv`: count number of lines.
- `less log.log`: fast way to view-only file. 
- `tail -f log.log`: view live update of the log file. 
- `ls -l --block-size=G`: view file size 


## Server Trikcs 
- `hostname`: to see the current server host name 

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

# MacOS 
## Clear History 

```
# Remove current histry
history -c

# Clear all bash history
rm ~/.bash_history # or rm ~/.zsh_history

# Open the history file
open ~/.bash_history
```

## ETC 

```
ps -ef | grep <pattern>
ps -aux | grep <pattern>
netstat -an 
```

## Find Files Certain Size 

```
find . -size +100M
```