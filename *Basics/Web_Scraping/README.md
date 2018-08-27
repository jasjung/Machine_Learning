# Web Scraping 

### Finding by class 

[reference](https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class)

```py {"class": "stylelistrow"}
mydivs = soup.findAll("div",)
```

### Unwrap(): Removing certain tags 

If if you wanto remove just a tag in html

[reference](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#decompose)

```py 
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a
a_tag.i.unwrap()
a_tag
```

```py
for i in soup.findAll('i'):
    i.unwrap()
# or 
for i in soup.findAll('i'):
    i.replace_with('')
```