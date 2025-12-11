import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random
import os

commands = [

    ("sin(x)", 0, 2*np.pi),                               # index 0
    ("cos(x)", 0, 2*np.pi),                               # index 1
    ("x**2", -3, 3),                                      # index 2
    ("exp(-x**2)", -3, 3),                                # index 3
    ("sqrt(x)", 0, 10),                                   # index 4

    ("x", -5, 5),                                          # index 5

    ("sqrt(1 - x**2)", -1, 1),                            # index 6

    ("((x**2 + sin(x))*(log(x+10)+exp(-x)))/(1+cos(x))", -10, 10),  # index 7

    ("sin(x) + log(x + e)", -1, 5),                       # index 8

    ("(x**2 + 1)/(sin(x) + 2)", -10, 10),                 # index 9  ← ← ← **ده اللي ظهر عندك**

]



def preprocess_input_image(path):

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:

        raise FileNotFoundError("⚠️ تعذّر قراءة الصورة")



    # استخلاص المنحنى فقط (من غير grid)

    edges = cv2.Canny(img, 50, 150)



    # Normalize

    edges = edges.astype(np.float32) / 255.0



    # Resize مثل التدريب

    edges = cv2.resize(edges, (84, 84))



    # (84,84,1)

    edges = edges.reshape(84, 84, 1)



    return edges

class FastCurveEnv(gym.Env):

    def __init__(self, dataset):

        super().__init__()

        self.dataset = dataset

        self.num_classes = len(dataset)



        self.action_space = spaces.Discrete(self.num_classes)

        self.observation_space = spaces.Box(0, 255, shape=(84,84,1), dtype=np.uint8)



    def reset(self, seed=None, options=None):

        super().reset(seed=seed)



        self.correct_index = np.random.randint(0, self.num_classes)

        img = random.choice(self.dataset[self.correct_index])

        img = (img * 255).astype(np.uint8)

        self.current_obs = img



        return img, {"correct_index": self.correct_index}



    def step(self, action):

        reward = 1 if action == self.correct_index else 0

        return self.current_obs, reward, True, False, {"correct_index": self.correct_index}





# تحميل dataset (لازم تكون نفس اللي استخدمته في التدريب)

dataset = np.load(r"E:\compiler construction\Lab 1-20251009T140633Z-1-001\Lab 1\Math Plotting Language\curve_dataset_v2.npy", allow_pickle=True)



# تحميل الموديل

model = PPO.load(r"C:\Users\mmwmn\Downloads\ppo_curve_intelligent_v2.zip")



# ابدأ بيئة الاختبار

env = FastCurveEnv(dataset)



obs, info = env.reset()

action, _ = model.predict(obs)



print("Predicted function:", commands[action][0])



plt.imshow(obs.squeeze(), cmap="gray")

plt.show()

import cv2

from tkinter import Tk, filedialog

file_path = filedialog.askopenfilename(

    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]

)

root = Tk()
root.withdraw()
img = preprocess_input_image(file_path)
action, _ = model.predict(img)
#print("Predicted class index =", action)

print("Predicted function:", commands[action][0])