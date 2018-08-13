# Jekyll 


Build your own website using `Github Pages` and blog with `Jekyll`. 
 
## Tutorial 
- https://evanwill.github.io/go-go-ghpages/
- https://www.youtube.com/watch?v=SWVjQsvQocA
- https://www.youtube.com/watch?v=iWowJBRMtpc
- https://github.com/evanwill/evanwill.github.io/blob/master/index.html
- Other Ref: https://jekyllrb.com/docs/posts/

## Steps

There are a few ways to do this, but this is how I did it. 

1. Create Repo on Github. Then go to `Settings` --> `GitHub Pages`--> Choose `Source` (I used master branch) --> `Save`. Then your repo should be live under `[username].github.io/[repo-name]` but there will be no content. 
2. Download your repo locally and type the following in your terminal. 

   ```
# may need sudo
gem install jekyll 
jekyll new new_site 
cd new_site
sudo jekyll serve --watch 
# or 
sudo bundle exec jekyll serve --watch
```

3. Push your repo and visit `[username].github.io/[repo-name]`. You can start blogging in the _posts folder using markdown. 

## Trouble Shooting 

```
gem cleanup lumberjack
gem list lumberjack
bundle clean --force
```



## Insert Image 
```
![image-title-here](/path/to/image.jpg){:class="img-responsive"}
```
Ref: 

- https://dev-notes.eu/2016/01/images-in-kramdown-jekyll/
- http://talk.jekyllrb.com/t/i-cannot-get-an-image-to-display/850/5
- https://flinhong.com/2016/09/22/figure-caption-for-images-on-jekyll-sites/


or 

```
![My helpful screenshot]({{ "/assets/screenshot.jpg" | absolute_url }})
```


## Add Comments Tool 

### [DISQUS.com](https://www.DISQUS.com)

https://medium.com/@balogic/adding-comments-part-to-your-jekyll-blog-6a8fccb7e634

### Other options 

- https://dc25.github.io/myBlog/2017/06/24/using-github-comments-in-a-jekyll-blog.html
- https://savaslabs.com/2016/04/20/squabble-comments.html
- https://utteranc.es
- http://ivanzuzak.info/2011/02/18/github-hosted-comments-for-github-hosted-blogs.html


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

