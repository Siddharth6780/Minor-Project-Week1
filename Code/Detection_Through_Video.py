import cv2
import numpy as np
import sys

sys.path.insert(0, './Helper')
from Motion_Detection import MotionDetection

def main():
    while True:
        # Capturing video
        video = cv2.VideoCapture('../pebrin database/Video-7_2019-08-14.wmv')
        isclosed = 0

        MotionDetection(video)

        if isclosed:
            break

    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()
