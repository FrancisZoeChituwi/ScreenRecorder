from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime
#Geometry to Dynamic
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
file_name=f"{time_stamp}.mp4"

#Saving code
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

#added webcam capture code
webcam = cv2.VideoCapture(0)

while True:
     img = ImageGrab.grab(bbox=(0, 0, width, height))
     img_np = np.array(img) 
     img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
     _, frame = webcam.read()
     cv2.imshow("Nzeru Capture", img_final)
     
     cv2.imshow("webcam", frame)
     
     captured_video.write(img_final)
     if cv2.waitKey(10) ==ord("q"):
         break
     