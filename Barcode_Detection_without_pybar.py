import numpy as np 
import cv2

video = cv2.VideoCapture(0)

while (1):

    r,frame = video.read()

    if r == True:

        blur_img = cv2.GaussianBlur(frame,(21,21),0)
        #Parameters: image_name , width and height of kernel which should be positive and odd , standard deviation in X and Y direction, 
        #sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as same as sigmaX. If both are given as zeros, 
        #they are calculated from kernel size.
        
        ret,thresh = cv2.threshold(blur_img,127,255,0)
        _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            for c in contours:

                approx_corners = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c,True),True) # Both true for closed figurs
                #cv2.drawContours(img,[approx_corners],0,(0),5)    # -1 ensures that all contours are drwn and 0 for one specific
                print len(approx_corners)                         # 0 in above line is black

                if len(approx_corners) == 4: 
                    # print (approx_corners)     
            
                    cv2.drawContours(blur_img,[approx_corners],0,(0),5)    # -1 ensures that all contours are drwn and 0 for one specific  
                    # print (approx_corners.ravel())
                
        cv2.imshow ("Original",frame)
        cv2.imshow("nalejbfv",Mask)
        cv2.imshow ("Blur",blur_img)
        

    else:
        print ("Oops, frames not coming in properly")

    
    if cv2.waitKey(1) & 0xFF == ord ('`'):
        break

video.release()
cv2.destroyAllWindows()