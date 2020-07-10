# theme

## minimal mistakes 

- https://github.com/mmistakes/minimal-mistakes
- https://github.com/mmistakes/mm-github-pages-starter
- https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/
- https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/


```sh 
sudo jekyll new new_site 
cd new_site

# add: 
gem "minimal-mistakes-jekyll"
# run 
bundle
# add 
theme: minimal-mistakes-jekyll
# run 
sudo bundle update

# replace index.md with index.html

# Change layout: post in _posts/0000-00-00-welcome-to-jekyll.markdown to layout: single

# Remove about.md, or at the very least change layout: page to layout: single
```

Locally serve 

```sh 
bundle exec jekyll serve 
```


