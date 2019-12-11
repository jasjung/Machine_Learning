# Subprocess 

References

- https://security.openstack.org/guidelines/dg_avoid-shell-true.html

### Examples 

```py 
# getting unique value of first column in a csv file
subprocess.check_output("cut -d',' -f1 ex.csv | sort | uniq", universal_newlines=True,shell=True).split()
# or 
cmd = "cut -d',' -f1 ex.csv | sort | uniq"
subprocess.check_output(cmd, universal_newlines=True,shell=True).split()

# getting the line count 
subprocess.check_output("wc -l ex.csv".split(),universal_newlines=True).split()[0] 

# ls 
subprocess.check_output("ls".split(),universal_newlines=True)

# wc 
subprocess.check_output("wc -l ex.csv".split(),universal_newlines=True)
```
