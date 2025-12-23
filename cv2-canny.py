# https://www.instagram.com/p/DSjTYDsipnN/

import cv2

def display(frame): cv2.imshow('OpenCV Canny', cv2.Canny(frame, 120, 240))

cap = cv2.VideoCapture(0)

try:
  while True:
    ret, frame = cap.read()
    display(frame)
    if cv2.waitKey(1) == 27: break
finally:
  cap.release()

cv2.destroyAllWindows()
