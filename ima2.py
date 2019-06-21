import cv2
import numpy as np

url='download.JPG'
cap=cv2.imread(url)
while(1):
    hsv=cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    res=cv2.bitwise_and(cap,cap,mask=mask)

    cv2.imshow('cap',cap)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',res)

    k=cv2.waitKey(5)& 0xFF# for escaping the infinite loop
    if (k==27):
        break

cv2.destroyAllWindows()

