# https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode

# python -m pip install opencv-python ultralytics

from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model("0", stream=True)

for result in results: result.show()
