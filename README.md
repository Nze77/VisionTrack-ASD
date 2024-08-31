VisionTrack-ASD
Analyzing Model Predictions
Detection
The system utilizes a pre-trained object detection model, which scans each video frame to identify persons (children and therapists). The model outputs bounding boxes around detected individuals, accompanied by confidence scores indicating the reliability of each detection. These bounding boxes are the foundation for further analysis.

Unique ID Assignment
Each detected person is assigned a unique ID, ensuring consistent identification across frames. The assignment leverages a tracking algorithm that maintains these IDs as individuals move within the video. The tracking system analyzes movement patterns and appearance features to distinguish between different persons and ensure the IDs remain accurate.

Tracking and Re-entries
As individuals move, leave, or re-enter the frame, the tracking algorithm updates or reassigns their unique IDs. The system is designed to recognize the same individual upon re-entry and reassign the original ID if possible. This is crucial for maintaining continuous tracking throughout the video.

Handling Occlusions
When a person is partially or fully obscured (occluded) by objects or other individuals, the tracking system employs advanced techniques to re-identify them once they become visible again. This process ensures that the correct ID is reassigned, minimizing errors in tracking and maintaining the continuity of the person’s movement trajectory.

Output
The final output is an annotated video where each person is enclosed in a bounding box, labeled with their unique ID. This visualization allows for easy interpretation of the tracking results, facilitating behavior analysis and engagement monitoring.
