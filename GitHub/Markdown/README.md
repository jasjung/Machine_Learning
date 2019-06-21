# Markdown (MD)

It's not fun trying to format image perfectly in github markdown because of different rendering rules. But here is an example that I liked and worked. 

Reference: 

- https://coderwall.com/p/iftc1q/centered-text-and-images-in-github-markdown

## Center Image with Border and Caption 

### EX1

<p align="center">
 <kbd><img src="images/img.png" width="300"></kbd>
 <br>
 <b><u>Figure 1</u>: Hello, I am a caption</b> 
</p>

```html
<p align="center">
 <kbd><img src="images/img.png" width="300"></kbd>
 <br>
 <b><u>Figure 1</u>: Hello, I am a caption</b> 
</p>
```

### EX2

<center>
<img src="images/sample.png" border="1" style="width:200px;">
</center>

```html
<center>
<img src="images/sample.png" border="1" style="width:200px;">
</center>
```

### EX3

<p align="center">
	<img src="images/sample.png" border="1" width="200">
</p>

```
<p align="center">
	<img src="images/sample.png" border="1" width="200">
</p>
```


## Add Caption 

<caption><center> <u> **Figure 1** </u>: **Definition of a box**<br> </center></caption>

```html
<caption>
	<center> <u> **Figure 1** </u>: **Definition of a box**<br> </center>
</caption>
```

## Video 

```html
<video width="400" height="200" src="images/demo.mov" type="video/mov" controls>
</video>
```

## Reference 

```html 
<p align="center">
  <b>Some Links:</b><br>
  <a href="#">Link 1</a> |
  <a href="#">Link 2</a> |
  <a href="#">Link 3</a>
  <br><br>
  <img src="http://s.4cdn.org/image/title/105.gif">
</p>
```


## Bullet Points 

https://stackoverflow.com/questions/47344571/how-to-draw-checkbox-or-tick-mark-in-github-markdown-table

- [x] one 
- [ ] two 

or 

- checked: `&#9744;` &#9744;  
- unchecked `&#9745;` &#9745;

or the actual character 

- ☐
- ☑


