import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
from time import sleep
for i in range(100):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    img = image[130:875, 649:1295]
    cv2.imwrite("image" + str(i) + ".png", img)
    sleep(1)
plt.show()