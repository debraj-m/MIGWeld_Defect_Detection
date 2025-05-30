from ultralytics import YOLO

# Load the YOLOv8 model (nano version here; you can change to s/m/l/x if needed)
model = YOLO('yolov8n.pt')

# Train the model using your custom dataset
model.train(
    data=r'C:\Users\debra\Desktop\Dataset\Drive link Dataset\driveLink.yaml',
    epochs=10,
    imgsz=640,
    batch=16
)
