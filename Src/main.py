
import numpy as np
import cv2
from detector import Detector
from tracker import Tracker

def main(video_path, output_path):
    
    detector = Detector()
    tracker = Tracker()
    
    
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        
        detections = detector.detect(frame)
        
        
        tracked_objects = tracker.update(detections, frame)
        
        
        for obj in tracked_objects:
            x1, y1, x2, y2, track_id = obj
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        
        out.write(frame)
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "D:\AI&DS Student\Projects\Cogniable\Data\ABA Therapy_ Daniel - Communication.mp4"
    output_path = "D:\AI&DS Student\Projects\Cogniable\Outputs"
    main(video_path, output_path)
