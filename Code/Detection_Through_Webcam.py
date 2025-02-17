import cv2
import numpy as np
import sys

sys.path.insert(0, './Helper')
from Motion_Detection import MotionDetection

def start_cam_analyze():
    # Capturing video
    video = cv2.VideoCapture(0)

    MotionDetection(video)

    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

# if __name__== "__main__":
#     main()
