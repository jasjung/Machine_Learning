# ZSH

https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/

"ZSH, also called the Z shell, is an extended version of the Bourne Shell (sh), with plenty of new features, and support for plugins and themes. Since it’s based on the same shell as Bash, ZSH has many of the same features, and switching over is a breeze."

## Oh My ZSH 

https://ohmyz.sh/#install


## Switching shells 

to return to default shell (more [here](https://unix.stackexchange.com/questions/137183/how-do-you-disable-oh-my-zsh-and-zsh-without-uninstalling-it))

```sh 
chsh -s /bin/bash
```

[Switch to ZSH](https://askubuntu.com/questions/131823/how-to-make-zsh-the-default-shell)

```sh 
chsh -s $(which zsh)
```


ZSH profile 

```sh 
vi ~/.zshrc
```

## Jupyter notebook 

- https://medium.com/@sumitmenon/how-to-get-anaconda-to-work-with-oh-my-zsh-on-mac-os-x-7c1c7247d896
- https://medium.com/@kuanhoong/setting-up-anaconda3-to-work-with-macos-catalina-zsh-shell-99898522ece1

When I swtiched to zsh, it had trouble accessing jupyter notebook. FYI, my jupyter was installed via conda. This is what I did the fix: 


1. copy some files from bash_profile 

	```sh 
	cat ~/.bash_profile
	```

	Where you see something like the following 

	```sh 
	alias jp='jupyter notebook'
	# added by Anaconda3 5.0.1 installer
	# old 
	# export PATH="/Users/<your_user_name>/anaconda3/bin:$PATH"
	# new
	export PATH="/Users/<your_user_name>/opt/anaconda3/bin:$PATH"
	```

2. Copy them and them at the end of `vi ~/.zshrc` file. 
3. Run `source ~/.zshrc` command. 
4. It worked! 

https://www.reddit.com/r/zsh/comments/9koj2v/help_im_not_sure_why_my_prompt_says_base/

It base show `base` in your terminal. to hide: 
```conda config --set changeps1 False```



## Plugins 

- https://medium.com/@ivanaugustobd/your-terminal-can-be-much-much-more-productive-5256424658e8

