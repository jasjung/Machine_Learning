# Extended Attribute 

- https://apple.stackexchange.com/questions/104712/what-causes-os-x-to-mark-a-folder-as-quarantined
- http://scottlab.ucsc.edu/xtal/wiki/index.php/Extended_Attributes

```sh
xattr -d com.apple.quarantine my_jar.jar
xattr -dr com.apple.quarantine my_jar.jar
```
