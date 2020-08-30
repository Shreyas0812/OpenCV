from pyzbar import pyzbar
import cv2

img = cv2.imread("Barcode128.jpg",0)

cv2.imshow("Original Image",img)

barcodes = pyzbar.decode(img)

"""
UTF-8 is a method for encoding these code points. A character in UTF-8 can be made up of one or more bytes. 
The encoding of the first 128 code points is equivalent to their ASCII counterpart. 
Further code points are represented using more than one byte. 
Each further byte in a single character starts with a special bit sequence to signal that it's still the same character.
"""

for b in barcodes:
    (x,y,w,h) = b.rect
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255), 2)

    barcodeData = b.data.decode("utf-8")
    barcodeType = b.type

    text = "{},({})".format(barcodeData, barcodeType)
    cv2.putText(img, text, (x-30, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) #image, text, position, font,font size, colour,thickness of font
    print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))

cv2.imwrite("new_img.jpg", img)

cv2.imshow("Final Image", img)
    
cv2.waitKey(0)
 
cv2.destroyAllWindows()
