# get current year 


Often people put something like © 2015-2019 Commpany Name in the footer. Having to manually update the current year seemed extremely annoying. 

https://stackoverflow.com/questions/4562587/shortest-way-to-print-current-year-in-a-website


The link provides solution to this: 

```html
<script>document.write(/\d{4}/.exec(Date())[0])</script>
<!-- or -->
<script>document.write(new Date().getFullYear())</script>
```