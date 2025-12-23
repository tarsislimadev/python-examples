import pyautogui
import matplotlib.pyplot as plt

x_coords = []
y_coords = []

x, y = 100, 100

print("Move the mouse to record positions. Move to the top-left corner (x < 10) to stop.")

while not x < 10 :
  x, y = pyautogui.position()
  x_coords.append(x)
  y_coords.append(y)
  print(f'x: {x}, y: {y}')

plt.plot(x_coords, y_coords)
plt.title('Mouse Positions')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()
