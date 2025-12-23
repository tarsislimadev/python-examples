import pyautogui, time

events = []

for _ in range(200):
  events.append(pyautogui.position())
  time.sleep(0.1)

print(f'{len(events)} mouse positions')
