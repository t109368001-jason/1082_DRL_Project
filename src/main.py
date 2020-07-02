# %% import
import random

import numpy as np
from PIL import Image

# %%
map_filepath = '../image/map.png'


# %%
class MyAction:
    def __init__(self, n):
        self.n = n

    def sample(self):
        return random.randint(0, self.n - 1)


class MyObservation:
    def __init__(self, n):
        self.n = n


class MyEnv:
    def __init__(self):
        self.action_spec = MyAction(4)
        self.observation_space = MyObservation(50 * 50)
        self.reset()

    def reset(self):
        self.current_step = 0
        self.current_state = 0

    def step(self, action):
        self.current_step += 1
        # TODO
        next_state = None
        reward = None
        done = None
        info = None
        return next_state, reward, done, info


map = Image.open(map_filepath).convert('L')
print(np.array(map))
env = MyEnv()

print(env.action_spec.n)
print(env.observation_space.n)
