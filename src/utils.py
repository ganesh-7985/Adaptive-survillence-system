import cv2
import os

def save_frame(frame, frame_count, relevant_count, irrelevant_count, frame_type):
    folder = 'relevant' if frame_type == 'relevant' else 'irrelevant'
    filename = f"{folder}/frame_{relevant_count if frame_type == 'relevant' else irrelevant_count}.jpg"
    cv2.imwrite(f'../output/{filename}', frame)
    print(f"Frame {frame_count}: {frame_type.capitalize()} - Saved to {filename}")


def log_detection(log_data, frame_count, frame_type, timestamp):
    log_data.append({
        'Frame': frame_count,
        'Type': frame_type,
        'Timestamp': timestamp
    })
