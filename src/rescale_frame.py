import torch
import cv2 as cv
import numpy as np



# Function to frame the video
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Reading videos
video = cv.VideoCapture('videos\squat_exercises\squat_exercises_00_.mp4')

while True:
    isTrue, frame = video.read()
    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()