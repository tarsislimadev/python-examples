import pyautogui

x, y = 100, 100

while not x < 10 :
  x, y = pyautogui.position()
  print(f'x: {x}, y: {y}')
