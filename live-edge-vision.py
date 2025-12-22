import cv2, time

cap = cv2.VideoCapture(0)
t0 =time.time()
frames = 0

while True:
  ret, frame = cap.read()
  if not ret: break
  edges = cv2.Canny(frame, 120, 240)
  frames += 1
  elapsed = time.time() - t0
  fps = frames / elapsed
  cv2.putText(edges, f'FPS: {fps:.1f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
  cv2.imshow('Live', edges)
  if cv2.waitKey(1) == 27: break # ESC gets out

cap.release()
cv2.destroyAllWindows()
