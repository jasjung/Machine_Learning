# OpenAI 

- Get Started: https://gym.openai.com/docs/

```
# or pip 
pip3 install gym

# test
import time

import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
	env.render()
	time.sleep(0.1)
	env.step(env.action_space.sample()) # take a random action

pip3 install pyglet==1.2.4
```

### Other Resources: 

- http://mckinziebrandon.me/TensorflowNotebooks/2016/12/21/openai.html
- http://nbviewer.jupyter.org/github/patrickmineault/xcorr-notebooks/blob/master/Render%20OpenAI%20gym%20as%20GIF.ipynb  
- http://gforsyth.github.io/instructions,/reference/2014/03/01/installing-jsanimation.html