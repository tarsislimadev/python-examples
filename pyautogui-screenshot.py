import pyautogui

img_1 = pyautogui.screenshot()
img_1.save('./data/my_screenshot1.png')
img_2 = pyautogui.screenshot('./data/my_screenshot2.png')
