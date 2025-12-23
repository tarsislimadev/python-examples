import pyautogui

for _ in range(20):
  x, y = pyautogui.position()
  print(f'x: {x}, y: {y}')
