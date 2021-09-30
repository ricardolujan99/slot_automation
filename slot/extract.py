import pytesseract 
import cv2
from re import sub
import numpy as np





pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def extractnum(): 
    img = cv2.imread("screenshot.png")
    kernel = np.ones((1,5),np.uint8)
    ret,img1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
    erosion = cv2.erode(img1,kernel,iterations = 3)
  

    valor_string = (pytesseract.image_to_string(erosion, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
    valor_filter = sub("\D", "", valor_string)
    cv2.imshow("hola",erosion)
    cv2.waitKey(100)
    return (valor_filter)


def showimg(titulo):
    img = cv2.imread("screenshot.png")
    cv2.imshow(titulo,img)
    cv2.waitKey(100)
