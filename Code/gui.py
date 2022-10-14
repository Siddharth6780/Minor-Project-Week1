from tkinter import *
from Detection_Through_Video import start_vid
from Detection_Through_Webcam import start_cam_analyze
from preview import start_cam

root = Tk()
root.title('Bacteria Detection')
root.geometry("400x400")
def start_video_analyze():
    start_vid()

def start_webcam_analyze():
    start_cam_analyze()

def close_btn():
    root.destroy()

def start_preview():
    start_cam()

video_button = Button(root,text="Analyze Video",command=start_video_analyze)
video_button.pack(pady=20)

cam_button = Button(root,text="Start WebCam Analyze",command=start_webcam_analyze)
cam_button.pack(pady=20)

stop_button = Button(root,text="Exit",command=close_btn)
stop_button.pack(pady=20)

preview_button = Button(root,text="Preview",command=start_preview).pack(pady=20)

root.mainloop()