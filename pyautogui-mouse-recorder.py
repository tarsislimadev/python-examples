import pyautogui

arr = []

for _ in range(200):
  pos = pyautogui.position()
  arr.append(pos)
  print(f'x: {pos.x}, y: {pos.y}')

print('PyAutoGUI')
print(f'{len(arr)} items')
