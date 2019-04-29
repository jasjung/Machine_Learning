# String Split 

- https://tecadmin.net/split-a-string-on-a-delimiter-in-bash-script/
- https://www.tutorialkart.com/bash-shell-scripting/bash-split-string/

```
STR="Learn to Split a String in Bash Scripting"

#Convert string to array called NAMES
IFS=' ' read -ra NAMES <<< "$STR"    

#Print all elements from array
for i in "${NAMES[@]}"; do
    echo $i
done

# print first element
echo ${NAMES[0]}
# out: Learn
```
