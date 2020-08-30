import numpy as np 
import cv2

img1 = cv2.imread("colours.jpg",1)

bgr = [234,39,59]
threshold = 50

minBGR = np.array[bgr[0] - threshold, bgr[1] - threshold, bgr[2] - threshold]
maxBGR = np.array[bgr[0] + threshold, bgr[1] + threshold, bgr[2] + threshold]

maskBGR = cv2.inRange(img1,minBGR,maxBGR) 

resultBGR = cv2.bitwise_and(img1,img1,mask = maskBGR)

cv2.imshow("Final Result : ", resultBGR) 

cv2.witkey(0)
cv2.destroyAllWindows()
