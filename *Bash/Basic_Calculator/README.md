# Basic Calculator (BC)


## Get Percent Change 

Need to use BC because normally bash does not deal with decimal points. 

```sh
old_num=114
new_num=79

perc_change=$(bc -l <<< "((($old_num-$new_num)/$old_num * 100))")
echo "percent change:" $perc_change
```

