# Screen

- Source: https://linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions/


- type `screen` to start persistent terminal sessions 
- to exit, press `ctrl + a + d`
- to return to the latest screen session, type `screen -r`
- type `screen -ls` to see list of screen sessions
- press `control + a ` then type `:quit` to quit the screen session while you are in the session. 
- `killall SCREEN` to kill all screens 
- reattach: `screen -r <session_id>`
