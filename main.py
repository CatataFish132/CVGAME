import cv2
import pyautogui
from time import sleep
from matplotlib import pyplot as plt
import os

pyautogui.PAUSE = 0

template_L = cv2.imread("left.png")
template_R = cv2.imread("right.png")
test = cv2.imread("test.png")

template_L_G = cv2.cvtColor(template_L, cv2.COLOR_RGB2GRAY)
template_R_G = cv2.cvtColor(template_R, cv2.COLOR_RGB2GRAY)
test_g = cv2.cvtColor(test, cv2.COLOR_RGB2GRAY)

# dims = (429, 515, 860-515, 460-429)
# dims = (515, 429, 860-515, 460-429)

# template matching with test image
sleep(3)

while True:
    pyautogui.screenshot("temp_image.png")
    temp_img = cv2.imread("temp_image.png")
    os.remove("temp_image.png")
    temp_img_g = cv2.cvtColor(temp_img, cv2.COLOR_RGB2GRAY)

    result_L = cv2.matchTemplate(temp_img_g, template_L_G, cv2.TM_CCOEFF_NORMED)
    result_R = cv2.matchTemplate(temp_img_g, template_R_G, cv2.TM_CCOEFF_NORMED)

    # plt.imshow(result_L, 'gray')
    # plt.show()
    min_val, max_val_l, min_loc, max_loc_l = cv2.minMaxLoc(result_L)
    min_val, max_val_r, min_loc, max_loc_r = cv2.minMaxLoc(result_R)

    if max_val_l > 0.8:
        print(max_loc_l)
        if max_loc_l[1] > 600 and max_loc_l[0] < 780:
            pyautogui.click(1000, 600)
            print("left")
    if max_val_r > 0.8:
        if max_loc_r[1] > 600 and max_loc_r[0] > 780:
            pyautogui.click(600, 600)
            print("right")

    # plt.show()
    sleep(1)

# sleep(10)

# pyautogui.screenshot("temp_image.png", dims)
# image = cv2.imread("temp_image.png")


