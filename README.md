VisionTrack-ASD
Overview
VisionTrack-ASD is an AI-powered system for detecting and tracking children and therapists in videos. It assigns unique IDs, handles re-entries and occlusions, and overlays tracking data for behavioral analysis and engagement monitoring.

Features
Person Detection: Identifies and labels children and therapists in video frames.
Unique ID Assignment: Provides and maintains unique IDs for each person.
Tracking: Monitors movement across frames, managing re-entries and occlusions.
Output Video: Generates a video with bounding boxes and IDs.
Installation
Prerequisites
Ensure Python 3.11 or later is installed. Download it from python.org.

Setting Up a Virtual Environment
Create a Virtual Environment:

bash
Copy code
python -m venv venv
Activate the Virtual Environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Installing Dependencies
Clone the Repository (if applicable):

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt
Requirements File
Create a requirements.txt file with the following content:

plaintext
Copy code
# Core Libraries
numpy>=1.23.0,<2.0.0
opencv-python
torch
torchvision
ultralytics
scipy
matplotlib

# Optional for video handling
ffmpeg-python
Usage
Prepare Your Video: Ensure your test video is ready and update the path in the configuration file.

Run the Inference Script:

bash
Copy code
python main.py
This processes the video, applies detection and tracking, and saves the annotated output.

Review Output: Check the output video for bounding boxes and unique IDs.

Configuration
Input Video Path: Update in the script or configuration file.
Detection Threshold: Adjust parameters as needed.
Troubleshooting
Import Errors: Ensure all dependencies are correctly installed.
Installation Issues: Verify Python and package versions, and check the virtual environment setup.
For further assistance, consult NumPy Troubleshooting.
