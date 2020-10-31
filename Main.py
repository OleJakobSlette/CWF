import gym
import matplotlib.pyplot as plt
import os
from gym import wrappers
from IPython import display
from PIL import Image

print("Saving gameplay of random decisions.")

env = gym.make('SpaceInvaders-v0')
env = wrappers.Monitor(env, "./gym-results", force=True)
env.reset()
plt.figure(figsize=(9, 9))
img = plt.imshow(env.render(mode='rgb_array'))
count = 1
cwd = os.getcwd()
if 'spaceInvader' in os.listdir(cwd):
    os.mkdir('spaceInvader')
for _ in range(80):
    env.env.ale.saveScreenPNG(b'test_image.png')
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        break

env.close()

print("Saved!")
