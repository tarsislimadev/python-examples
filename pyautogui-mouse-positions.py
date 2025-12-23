import pyautogui, time

SLEEP = 10

cur_time = lambda: int(time.time())

start_time = cur_time()
end_time = start_time + SLEEP
print(f'start: {start_time}; end: {end_time}')

while cur_time() < end_time:
  x, y = pyautogui.position()
  print(f'x: {x}; y: {y}')
