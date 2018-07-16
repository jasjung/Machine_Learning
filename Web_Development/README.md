# Website 

Build your own website using `Github Pages` and blog with `Jekyll`. 
 
## Jekyll 

### Tutorial 
- https://evanwill.github.io/go-go-ghpages/
- https://www.youtube.com/watch?v=SWVjQsvQocA
- https://www.youtube.com/watch?v=iWowJBRMtpc
- https://github.com/evanwill/evanwill.github.io/blob/master/index.html

Other Reference 

- https://jekyllrb.com/docs/posts/


### Steps

There are a few ways to do this, but this is how I did it. 

1. Create Repo on Github. Then go to `Settings` --> `GitHub Pages`--> Choose `Source` (I used master branch) --> `Save`. Then your repo should be live under `[username].github.io/[repo-name]` but there will be no content. 
2. Download your repo locally and type the following in your terminal. 

   ```
# may need sudo
gem install jekyll 
jekyll new new_site 
cd new_site
sudo jekyll serve --watch 
```

3. Push your repo and visit `[username].github.io/[repo-name]`. You can start blogging in the _posts folder using markdown. 

### Insert Image 
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





## HTML & CSS 

### Tutorial 
- https://www.youtube.com/watch?v=nN6QuNqmAwk
- https://www.youtube.com/watch?v=IWU6ysZwCbE

## Github Pages 
- https://pages.github.com 


## Google Analytics 
Reference: https://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages


## Adding Advertisement 

### Google AdSense 

https://mycyberuniverse.com/web/add-googe-adsense-to-a-jekyll-website.html


