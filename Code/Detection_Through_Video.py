import cv2
import numpy as np
import sys
import glob
import os

sys.path.insert(0, './Helper')
from Helper.Motion_Detection import MotionDetection
isclosed = 0

def main():
    while True:
    
        list_of_files = glob.glob('/home/pi/*.mkv') # * means all if need specific format then *.csv
        print(list_of_files)
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)


        # Capturing video
        video = cv2.VideoCapture('../pebrin database/Video-7_2019-08-14.wmv')

        if MotionDetection(video) == False:
            break

    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()
