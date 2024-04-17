from ultralytics import YOLO
import cv2

model_path = '../runs/classify/train/weights/best.pt'

model = YOLO(model_path)
image1 = cv2.imread('../images/teste3.png', cv2.IMREAD_GRAYSCALE)
results = model(image1)
result = results[0]