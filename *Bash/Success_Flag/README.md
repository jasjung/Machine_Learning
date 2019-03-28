# Success Flag and Error Handling 

## Exit Status 

- [http://linuxcommand.org/lc3_wss0140.php](http://linuxcommand.org/lc3_wss0140.php) -> good!

`$?` will contain the exit status of the last command executed. If a program finishes successfully, the exit status will be zero.

```sh 
[me] $ true; echo $?
0
[me] $ false; echo $?
1
```
↓

```
# Check the exit status

cd $some_directory
if [ "$?" = "0" ]; then
	rm *
else
	echo "Cannot change directory!" 1>&2
	exit 1
fi
```
↓

```
# A better way

if cd $some_directory; then
	rm *
else
	echo "Could not change directory! Aborting." 1>&2
	exit 1
fi
```


## Error Exit Function 

```
# An error exit function

error_exit()
{
	echo "$1" 1>&2
	exit 1
}

# Using error_exit

if cd $some_directory; then
	rm *
else
	error_exit "Cannot change directory!  Aborting."
fi
```


## AND OR 

command2 is executed if, and only if, command1 returns an exit status of zero.

```
command1 && command2
```

command2 is executed if, and only if, command1 returns a non-zero exit status.

```
command1 || command2
```
