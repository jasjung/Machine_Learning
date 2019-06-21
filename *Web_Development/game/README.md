# Javascript Game 

- [Reference](https://pastebin.com/Z3zhb7cY)
- [YouTube-Snake Coding Fast Demo](https://youtu.be/xGmXxpIj6vs)
- https://www.w3schools.com/graphics/game_controllers.asp


## Disable Array Key Scrolling 

https://stackoverflow.com/questions/8916620/disable-arrow-key-scrolling-in-users-browser

```javascript
var keys = {};
window.addEventListener("keydown",
    function(e){
        keys[e.keyCode] = true;
        switch(e.keyCode){
            case 37: case 39: case 38:  case 40: // Arrow keys
            case 32: e.preventDefault(); break; // Space
            default: break; // do not block other keys
        }
    },
false);
window.addEventListener('keyup',
    function(e){
        keys[e.keyCode] = false;
    },
false);
``` 
