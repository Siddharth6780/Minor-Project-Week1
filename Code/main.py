import cv2
import numpy as np
import sys
import os

from Code.Detection_Through_Video import start_vid
from Code.Detection_Through_Webcam import start_cam_analyze
sys.path.insert(0, './Helper')
import streamlit as st
from Helper.Motion_Detection import MotionDetection
st.title("Bacteria Detection")
c1, c2 , c3= st.columns(3)

with c1:
    if st.button("Detection By Video"):

        start_vid()


with c2:
    if st.button("Detection By Live Camera"):

        start_cam_analyze()


with c3:
    if st.button("exit"):
        os._exit(0)
