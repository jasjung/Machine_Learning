# Table of Content 

Refererence

- gh-md-toc: https://github.com/ekalinin/github-markdown-toc

## Example 

### Table of Content 

- [Topic 1](#topic-1)
- [Topic 2](#topic-2)

### Topic 1 

[Content]

### Topic 2

[Content]

## Example Code

```md 
### Table of Content 

- [Topic 1](#topic-1)
- [Topic 2](#topic-2)

### Topic 1 

[Content]

### Topic 2

[Content]
```

## GH-MD-TOC package

Install 

```
curl https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc -o gh-md-toc
chmod a+x gh-md-toc
```

Use 

```
./gh-md-toc ~/projects/Dockerfile.vim/README.md 
```


## Complicated TOC (2021 Update)

If you have a complicated header that includes a lot of special characters or spaces, adding a simple hyphen to replace space does not work too well. 
This method of adding an `html <a> tag` can help with this and make the table of content shortcut name shorter. 


```markdown
## Table of Content 

1. [ Description. ](#desc)
2. [ Usage tips. ](#usage)

<a name="desc"></a>
## 1. Description

sometext

<a name="usage"></a>
## 2. Usage tips

```

- reference: https://community.atlassian.com/t5/Bitbucket-questions/How-to-write-a-table-of-contents-in-a-Readme-md/qaq-p/673363