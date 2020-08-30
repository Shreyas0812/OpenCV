from pyzbar import pyzbar
import cv2

img = cv2.imread("QRcode3.jpg",0)

cv2.imshow("Original Image",img)

QRcode = pyzbar.decode(img)

for b in QRcode:
    (x,y,w,h) = b.rect
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255), 2)

    QRData = b.data
    QRType = b.type

   # text = "{},({})".format(QRData, QRType)
   # cv2.putText(img, text, (x-30, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) #image, text, position, font,font size, colour,thickness of font
    print("found {} meaning {}".format(QRType, QRData))

#cv2.imwrite("new_img.jpg", img)    
cv2.waitKey(0)
 
cv2.destroyAllWindows()
