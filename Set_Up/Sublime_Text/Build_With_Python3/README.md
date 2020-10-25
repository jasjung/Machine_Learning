# Build with Python Three 

https://medium.com/@hariyanto.tan95/set-up-sublime-text-3-to-use-python-3-c845b742c720

When you try to build py files, the default is 2. lets update that. 

Run this to check the version in your sublime text. (cmd+b)

```py
import sys
print(sys.version)
```

Run this to get the path to your python source 

```sh
which python3
# /usr/local/bin/python3
```

Add the new build environment by going to `Tools -> Build System -> New Build System` and adding the following 

```sh 
{
 "cmd": ["/usr/local/bin/python3", "-u", "$file"],
 "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
 "selector": "source.python"
}
```

And save it as `newPython3.sublime-build` or whatever you want. Then choose this build env to use. 


