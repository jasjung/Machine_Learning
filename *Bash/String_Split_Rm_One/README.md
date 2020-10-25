# String Split Rm one 


```sh 
#For Filename
echo "a.b.c.txt" | rev | cut -d"." -f2-  | rev
# a.b.c

#For extension
echo "a.b.c.txt" | rev | cut -d"." -f1  | rev
# txt 
 ```