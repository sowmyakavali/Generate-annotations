import argparse
import cv2
import os

from generate_annotations import writeXml

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, help="path to input video file")
ap.add_argument("-l", "--label", help="which class you want to annotate")
args = vars(ap.parse_args())

# Create the folder to save images and annotations
if not os.path.exists(args["label"]):
    os.makedirs(args["label"])

# Access the video
vs = cv2.VideoCapture(args["video"])

# Important variables
(W, H) = (None, None)
frameCount = -1
totalElapsed = 0  

# Lets dive
try:
    while True:
        # Read frame
        (grabbed, frame) = vs.read()

        # Break if grabbed is false
        if not grabbed:
            break

        # Update frame count
        frameCount += 1

        # Store frame dimensions
        if W is None or H is None:
            (H, W) = frame.shape[:2]

        # List to store all bounding boxes in a frame
        boxes = []

        # Resize the image size to display
        image = cv2.resize(frame, (1080, 780))

        # Show the image
        # cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF

        # Start annotation
        if key == ord("s"):
            # Select the ROIs
            box = cv2.selectROIs("Frame", image, fromCenter=False, showCrosshair=True)
            # If u selected multiple ROIs append them
            if len(box)>1:
                for b in box:
                    boxes.append(box)
            # If only one region is selected        
            else:
                boxes.append(box)  
        # Key to quit
        elif key == ord("q"):
            break  
        
        # If You have objects in frame save that frame and bounding boxes in a xml file
        if len(boxes) > 1:
            print(boxes)
            img_name = str(frameCount) + '.jpg'
            cv2.imwrite(os.path.join(args["label"], img_name), image)
            writeXml(img_name, W, H, boxes, args["label"])

except KeyboardInterrupt:
    print("")
    print("[EXCP] Keyboard interrupt")
    print("[INFO] Cleanup initialized")

# Destroy all windows
vs.release()
cv2.destroyAllWindows()