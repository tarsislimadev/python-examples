import cv2

face_cascade_name = './data/haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)): exit(0)

def detect(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    return face_cascade.detectMultiScale(frame_gray)

def display(frame, faces):
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

    cv2.imshow('Face detection', frame)

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if frame is None: break
        detected = detect(frame)
        display(frame, detected)
        if cv2.waitKey(1) == 27: break
except:
    cap.release()

cv2.destroyAllWindows()
