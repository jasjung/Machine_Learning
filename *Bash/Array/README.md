# Array

Dealing with arrays in bash 

- https://www.cyberciti.biz/faq/finding-bash-shell-array-length-elements/
- https://stackoverflow.com/questions/8880603/loop-through-an-array-of-strings-in-bash


## Convert string to array 

Note: `($string)` does not work on macos 

```sh 
string="element1  element2  element3"
echo $string
array=($string)
echo ${array[1]}

array_length=${#array[@]}
echo "array lengh:" $array_length
echo ${array[1]}

# for loop directly 
for i in $string; do 
	echo $i;
done
```


```sh
# if given an array 
array=("element1" "element2")
echo ${array[1]}
```