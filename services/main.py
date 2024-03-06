from pytesseractocr import PytesseractOCR
from paddleocrtes import PaddleOCRTES
import cv2

ocrtesser = PytesseractOCR()
image = cv2.imread("D:/Python/formated/resources/images/license7.jpg")
result = ocrtesser.text_detection(image)
print(result)

ocrpaddle = PaddleOCRTES()
image =  "D:/Python/formated/resources/images/license7.jpg"
paddleres = ocrpaddle.text_detection(image)
print (paddleres)