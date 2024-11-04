import cv2
import os
import pandas as pd
from ultralytics import YOLO
from compression import compress_video
from utils import save_frame,log_detection

relevant_class_names = ['person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck']
model = YOLO('yolov8n.pt')
video_path = '/Users/shankarganesh/Desktop/asc/input/input_video.mp4'
output_path_relevant = '/Users/shankarganesh/Desktop/asc/output/relevant'
output_path_irrelevant = '/Users/shankarganesh/Desktop/asc/output/irrelevant'
log_path = '/Users/shankarganesh/Desktop/asc/output/logs/detections_log.csv'

os.makedirs(output_path_relevant, exist_ok=True)
os.makedirs(output_path_irrelevant, exist_ok=True)
os.makedirs('../output/logs', exist_ok=True)


cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0
relevant_count = 0
irrelevant_count = 0
log_data = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    results = model(frame)
    detected_relevant = False

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = model.names[class_id]

            if label in relevant_class_names:
                detected_relevant = True
                break

    frame_type = 'relevant' if detected_relevant else 'irrelevant'
    save_frame(frame, frame_count, relevant_count, irrelevant_count, frame_type)

    if detected_relevant:
        relevant_count += 1
    else:
        irrelevant_count += 1

    log_data.append({
        'Frame': frame_count,
        'Type': frame_type,
        'Timestamp': frame_count / fps
    })

cap.release()

# Save log data to CSV
log_df = pd.DataFrame(log_data)
log_df.to_csv(log_path, index=False)

# Compress the folders
compress_video(output_path_relevant, 'output_relevant.mp4')
compress_video(output_path_irrelevant, 'output_irrelevant.mp4')
print("Processing and compression complete.")