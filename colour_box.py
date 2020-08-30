import numpy as np 
import cv2

img1 = cv2.imread("colours.jpg",1)

#bgr = [36,27,237]

minBGR = np.array([0,200,200])
maxBGR = np.array([170,255,255])

maskBGR = cv2.inRange(img1,minBGR,maxBGR) 

resultBGR = cv2.bitwise_and(img1,img1,mask = maskBGR)

cv2.imshow("Original image", img1)
cv2.imshow("Final Result", resultBGR) 

cv2.waitKey(4000)
cv2.destroyAllWindows()