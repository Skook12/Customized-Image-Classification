from ultralytics import YOLO

model_path = "src/runs/classify/train/weights/best.pt"

model = YOLO(model_path)
results = model("src/images/teste3.png")
result = results[0]
result.show()
