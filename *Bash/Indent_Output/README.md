# indent output 

For whatever reason, say you want to format your bash output. I wanted to `head` some files but wanted to indent them for easy of readability. 

`| nl -bn` -> this did the trick. 

Example 


```sh 
head test_file.txt | nl -bn
```

output 
```
        aidfh ias ajsoid jaishd
        asdkjnaosd aoshd
        asdiasdh  adhaods 
```


```sh 
head test_file.txt 
```

output 
```
aidfh ias ajsoid jaishd
asdkjnaosd aoshd
asdiasdh  adhaods
```


reference: https://unix.stackexchange.com/questions/148109/shifting-command-output-to-the-right