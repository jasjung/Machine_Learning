# TTY (TeleTYpewriter)

- https://www.quora.com/What-does-the-t-or-tty-do-in-Docker
- https://askubuntu.com/questions/481906/what-does-tty-stand-for/481915#481915


### Crontab 

When running docker command from crontab, I had the following issue: 

```
cannot enable tty mode on non tty input
```

This was fixed by removing `-t` tag. 

```sh
docker run -i -v `pwd`:/ext [name of your docker img] python /ext/your_python_file.py 
``` 

- https://stackoverflow.com/questions/29380344/docker-exec-it-returns-cannot-enable-tty-mode-on-non-tty-input