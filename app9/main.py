import cv2 as c
import time as t
from email_sender import send_email
import glob
import os
from threading import Thread
#import streamlit as s


def clean_folder():
    all_images = glob.glob("images/*.png")
    for image in all_images:
        os.remove(image)


video = c.VideoCapture(0)
t.sleep(1)

first_frame = None

status_list=[]
count =1
while True:
    
    status=0
    check , frame = video.read()

    

    gray_frame = c.cvtColor(frame,c.COLOR_BGR2GRAY)
    gray_frame_gau = c.GaussianBlur(gray_frame,(21,21),0)
    

    if first_frame is None:
        first_frame=gray_frame_gau

    delta_frame = c.absdiff(first_frame,gray_frame_gau)
   

    #if the pixel is more that 30 assign it as 255 to make the whihte as object
    thresh_frame = c.threshold(delta_frame,30,255,c.THRESH_BINARY)[1]
   
    dil_frame =c.dilate(thresh_frame,None,iterations=2)
    
    
    #to count the objects in web cam
    counters , check =c.findContours(dil_frame,c.RETR_EXTERNAL,c.CHAIN_APPROX_SIMPLE)

    for counter in counters:
        if c.contourArea(counter)<5000:
            continue
        x,y,w,h = c.boundingRect(counter)
        rectangle =c.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        if rectangle.any():
            status =1
            #to save a image
            c.imwrite(f"images/{count}.png",frame)
            count = count+1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images)/2)
            image_with_object = all_images[index]
            
    
    status_list.append(status)
    status_list=status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email,args=(image_with_object, ))
        email_thread.daemon=True

        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon=True

        email_thread.start()
        


    c.imshow("my video", frame)
    key = c.waitKey(1)
    #to exit from the web cam  
    if key == ord("q"):
        break



video.release()
clean_thread.start()

print(check)
print(frame)