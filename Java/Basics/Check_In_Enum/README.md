# check if value is in enum 

https://stackoverflow.com/questions/4936819/java-check-if-enum-contains-a-given-string/4936895

```java 
enum Choices{A1, A2, B1, B2};

List choices = Arrays.asList(Choices.values());

//compare with enum value 
if(choices.contains(Choices.A1)){
   //do something
}

//compare with String value
if(choices.contains(Choices.valueOf("A1"))){
   //do something
}
```