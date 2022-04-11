import cv2
import pyautogui
from time import sleep

pyautogui.PAUSE = 0

template_L = cv2.imread("left.xcf")
template_R = cv2.imread("right.xcf")

# template_L_G = cv2.cvtColor(template_L, cv2.COLOR_RGB2GRAY)
# template_R_G = cv2.cvtColor(template_R, cv2.COLOR_RGB2GRAY)

# dims = (429, 515, 860-515, 460-429)
dims = (515, 429, 860-515, 460-429)

sleep(10)

pyautogui.screenshot("temp_image.png", dims)
# image = cv2.imread("temp_image.png")


