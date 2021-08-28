# Environment Variable


https://phoenixnap.com/kb/set-environment-variable-mac


In MacOS, you can type `env` to see the environment variable. How can we access them in python? 

First set the variable by updating `~/.zshrc`. 

```sh
open ~/.zshrc # for zsh 
source ~/.zshrc
```

Access the variable in python. 

```py
import os 
import sys 

YOUR_ENV_VAR = os.getenv('YOUR_ENV_VAR')
# the following is just an example why I was using the env variable. 
sys.path.append(YOUR_ENV_VAR) 
```
