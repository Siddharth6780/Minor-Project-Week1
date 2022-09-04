import cv2
import numpy as np
import sys
import os
sys.path.insert(0, './Helper')
import streamlit as st
from Helper.Motion_Detection import MotionDetection
st.title("Bacteria Detection")
c1, c2 , c3= st.columns(3)

with c1:
    if st.button("Detection By Video"):

        # Capturing video
        video = cv2.VideoCapture('../pebrin database/Video-7_2019-08-14.wmv')
        isclosed = 0

        MotionDetection(video)



        video.release()

        # Destroying all the windows
        cv2.destroyAllWindows()


with c2:
    if st.button("Detection By Live Camera"):

        video = cv2.VideoCapture(0)
        isclosed = 0

        MotionDetection(video)




        video.release()

        # Destroying all the windows
        cv2.destroyAllWindows()


with c3:
    if st.button("exit"):
        os._exit(0)
