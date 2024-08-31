

from ultralytics import YOLO

class Detector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
    
    def detect(self, frame):
        results = self.model(frame)[0]
        detections = []
        threshold = 100 # check
        for box in results.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if cls in [0]:  
                x1, y1, x2, y2 = box.xyxy[0]
                width = x2 - x1
                height = y2 - y1
                area = width * height
                label = 'child' if area < threshold else 'therapist'  # needs to change according to the video
                detections.append({
                    'bbox': [int(x1), int(y1), int(x2), int(y2)],
                    'confidence': conf,
                    'class': label
                })
        return detections

