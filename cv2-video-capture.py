import cv2

def display(frame):
  cv2.imshow('Video Capture', frame)

cap = cv2.VideoCapture(0)

try:
  while True:
    ret, frame = cap.read()
    if not ret: break
    display(frame)
    if cv2.waitKey(1) == 27: break
except:
  cap.release()

cv2.destroyAllWindows()
