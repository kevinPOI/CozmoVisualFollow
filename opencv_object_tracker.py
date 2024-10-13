import cv2
from time import sleep
import numpy as np
# Create a video capture object to read from the webcam
# cap = cv2.VideoCapture(0)  # '0' is usually the default ID for the built-in webcam

# # Read the first frame from the webcam
# ret, frame = cap.read()


def cv_init(img):
    tracker = cv2.TrackerMIL_create()
    img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2RGB) 
    print(type(img))
    print(img.shape)
    cv2.imshow('Frame', img)
    initBB = cv2.selectROI("Frame", img, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Frame")

    # Create tracker object
    

    # Initialize the tracker with the first frame and the bounding box
    tracker.init(img, initBB)
    return tracker

def cv_detect(img, tracker):
# Define the initial bounding box, typically you would select this manually
    img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2RGB) 
    
    success, box = tracker.update(img)

        # Draw the tracked object
    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        print("failed")
    # Display the resulting frame
    cv2.imshow('Tracking', img)
    cv2.waitKey(1)
    turn = (x - 160)/160
    return turn
    # Exit loop when 'q' is pressed
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# When everything done, release the capture

