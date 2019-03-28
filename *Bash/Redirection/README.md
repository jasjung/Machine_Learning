# Redirection 

Credit: [https://www.brianstorti.com/understanding-shell-script-idiom-redirect/](https://www.brianstorti.com/understanding-shell-script-idiom-redirect/)

## stdout - standard output

```
foo.txt > output.txt
```

```
cat foo.txt 1> output.txt
```

`command > output` is just a shortcut for `command 1> output`. 

## stderr - standard error

```
# this will print error 
cat nop.txt > output.txt
```

```
# error not printed
cat nop.txt 2> error.txt
```

## File Descriptors 

There are file descriptors for the Standard Output (stdout) and Standard Error (stderr). `1` for stdout and `2` for stderr.


## 2>&1

- = Redirect the stderr to the same place we are redirecting the stdout. 
- Using `2>&1` will redirect stderr to whatever value is set to stdout (and `1>&2` will do the opposite).
- You can use `&[FILE_DESCRIPTOR]` to reference a file descriptor value

```
cat nop.txt > output.txt 2>&1
```
