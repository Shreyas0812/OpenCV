import numpy as np 
import cv2

i=0
j=0

img = cv2.imread('Hexagon_detect.jpg',0)

cv2.imshow('Original Image',img)

ret,thresh = cv2.threshold(img,240,255,0)

_,contours,hierchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#In the parameters first one is source image, second is contour retrieval mode, third is contour approximation method.

if contours:
    for c in contours:

       approx_corners = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c,True),True) # Both true for closed figurs
       #cv2.drawContours(img,[approx_corners],0,(0),5)    # -1 ensures that all contours are drwn and 0 for one specific
       print len(approx_corners)                         # 0 in above line is black

       if len(approx_corners) == 6: 
           # print (approx_corners)     
            
            cv2.drawContours(img,[approx_corners],0,(0),5)    # -1 ensures that all contours are drwn and 0 for one specific  
           # print (approx_corners.ravel())
             
            while i<10:
                j=i+2
                while j<12 :
                    cv2.line(img, (approx_corners.ravel()[i],approx_corners.ravel()[i+1]), (approx_corners.ravel()[j],approx_corners.ravel()[j+1]), (0),2)
                    j+=2
                i+=2


ret,thresh = cv2.threshold(img,240,255,0)
_,contours,hierchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

if contours:
    for c in contours:

       approx_corners = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c,True),True) # Both true for closed figurs

       if len(approx_corners) == 3: 
           print "Next one:"
           print (approx_corners.ravel())   

cv2.imshow('Final Image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()