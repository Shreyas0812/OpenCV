import numpy as np 
import cv2

i=0
j=0

img = cv2.imread('Hexagon_detect.jpg',0)

ret,thresh = cv2.threshold(img,240,255,0)

_,contours,hierchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

if contours:
    for c in contours:
       approx_corners = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c,True),True) # Both true for closed figurs
       #cv2.drawContours(img,[approx_corners],0,(0),5)    # -1 ensures that all contours are drwn and 0 for one specific
       print len(approx_corners)                         # 0 in above line is black

       if len(approx_corners) == 6: 
            print (approx_corners)     
            
            cv2.drawContours(img,[approx_corners],0,(0),5)    # -1 ensures that all contours are drwn and 0 for one specific  
            
            print "------------------First---------------------"
            while (i < 6):
                while (j < 6):
                    print approx_corners[i] 
                    print approx_corners[j]
                    print "-------------------NEXT---------------"
                    j+=1
                i+=1
                j=0
               


cv2.imshow('Final Image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
