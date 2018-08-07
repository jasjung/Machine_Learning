# Jekyll 

## Add Comments Tool 

### [DISQUS.com](https://www.DISQUS.com)

https://medium.com/@balogic/adding-comments-part-to-your-jekyll-blog-6a8fccb7e634

### Other options 

- https://dc25.github.io/myBlog/2017/06/24/using-github-comments-in-a-jekyll-blog.html
- https://savaslabs.com/2016/04/20/squabble-comments.html
- https://utteranc.es
- http://ivanzuzak.info/2011/02/18/github-hosted-comments-for-github-hosted-blogs.html


```
```

## Local Dev 

ref: 

- https://github.com/jekyll/jekyll/issues/3103
- https://jekyllrb.com/docs/quickstart/

When `jekylle serve` does not work, do the following instead: 
 
```
bundle exec jekyll serve --watch 
```

## Images 

When I inserted images and videos into the jekyll posts, they were broken when I built the site. You need to do the following to fix it. 

1. In `config.yml` update your `baseurl` and `url`. 

    ```
baseurl: "/Blog"
url: "http://usrname.github.io" 
```

2. In your `markdown` file, add `{{site.url}}{{site.baseurl}}` to the file path. 

ref: https://github.com/hemangsk/Gravity/issues/1

