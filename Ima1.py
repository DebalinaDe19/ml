import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#for opening the video camera of the lappy, u can also put url or any video links
while(1):
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#COLOR_BGR2HSV is used for masking the background in greyscale
    lower_green=np.array([192,255,0])
    upper_green=np.array([0,255,64])

    mask=cv2.inRange(hsv,lower_green,upper_green)

    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',res)

    k=cv2.waitKey(5)& 0xFF# for escaping the infinite loop
    if (k==27):
        break

cv2.destroyAllWindows()


    
