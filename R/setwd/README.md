# Setwd to the location of the file 

Reference/Credit: https://eranraviv.com/r-tips-and-tricks-working-directory/


```
# install.packages("rstudioapi") # run this if it's your first time using it to install
library(rstudioapi) # load it
```

```
# the following line is for getting the path of your current open file
current_path <- getActiveDocumentContext()$path 
# The next line set the working directory to the relevant one:
setwd(dirname(current_path))
# you can make sure you are in the right directory
print(getwd())

```

```
set_wd <- function() {
	library(rstudioapi) # make sure you have it installed
	current_path <- getActiveDocumentContext()$path 
	setwd(dirname(current_path))
	print(getwd())
}

set_wd()
```