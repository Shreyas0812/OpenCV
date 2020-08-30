import numpy as np 
import cv2

print ('Blue +-')
BThresh = input()     #40

print ('Green +-') #100
GThresh = input()

print ('Red +-')      #50
RThresh = input()

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('Blue','image',0 + BThresh,255 - BThresh,nothing)
cv2.createTrackbar('Green','image',0 + GThresh,255 - GThresh,nothing)
cv2.createTrackbar('Red','image',0 + RThresh,255 - RThresh,nothing)

video = cv2.VideoCapture(0)


while(True):
    
    B = cv2.getTrackbarPos('Blue','image')
    G = cv2.getTrackbarPos('Green','image')
    R = cv2.getTrackbarPos('Red','image')

    r, frame = video.read()

    #frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    
    if r == True:
                                                                                       
        minBGR = np.array([B - BThresh,G - GThresh,R - RThresh])                  
        maxBGR = np.array([B + BThresh,G + GThresh,R + RThresh])                  
                         
        Mask = cv2.inRange(frame,minBGR,maxBGR) 
        
        ret, thresh = cv2.threshold(Mask, 127, 255, 0)   # 0 => THRESH_BINARY
        
        _,contours, hierarchy = cv2.findContours(Mask,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            cnt = contours[0] 
            for c in contours:
                area = cv2.contourArea(c)
                if (area>800):
                    x,y,w,h = cv2.boundingRect(c)      # (x,y) top left, w = width, h=height
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (10,250,250), 3)
                    #cv2.rectangle(frame1, (x,y), (x+w,y+h), (10,250,250), 3)

        cv2.imshow("Original image", frame)           
        #cv2.imshow("Hsv image", frame)
        cv2.imshow("Final Result", Mask)
               
    else:
        print "Camera Problem"    
    if cv2.waitKey(1) & 0xFF == ord ('`'):
        break

video.release()
cv2.destroyAllWindows()    