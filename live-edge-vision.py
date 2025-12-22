import cv2

cap = cv2.VideoCapture(0)

try:
  while True:
    ret, frame = cap.read()
    cv2.imshow('Live', cv2.Canny(frame, 120, 240))
    if cv2.waitKey(1) == 27: break # ESC gets out
finally:
  cap.release()

cv2.destroyAllWindows()
