
from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)
    
    def update_tracks(self, detections, frame):
        bbox_xywh = []
        confidences = []
        class_ids = []
        
        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            bbox = [(x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1]  
            bbox_xywh.append(bbox)
            confidences.append(det['confidence'])
            class_ids.append(det['class'])
        
        tracks = self.tracker.update_tracks(bbox_xywh, confidences, class_ids, frame=frame)
        
        tracked_objects = []
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()
            cls = track.get_det_class()
            tracked_objects.append({
                'id': track_id,
                'bbox': [int(ltrb[0]), int(ltrb[1]), int(ltrb[2]), int(ltrb[3])],
                'class': cls
            })
        return tracked_objects
