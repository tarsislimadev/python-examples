import pyautogui
import matplotlib.pyplot as plt
import time

SLEEP = 10

x_coords = []
y_coords = []

cur_time = lambda: int(time.time())
start_time = cur_time()
end_time = start_time + SLEEP
print(f'start: {start_time}; end: {end_time}')

print('Move the mouse to record positions. Wait for 10 seconds to stop.')

while cur_time() < end_time:
  x, y = pyautogui.position()
  x_coords.append(x)
  y_coords.append(y)
  print(f'x: {x}, y: {y}')

plt.plot(x_coords, y_coords)
plt.title('Mouse Positions')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()
