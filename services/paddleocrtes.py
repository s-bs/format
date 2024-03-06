from baseocr import BASEOCR
from paddleocr import PaddleOCR

class PaddleOCRTES(BASEOCR):
    def text_detection(self,image):
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        result = ocr.ocr(image, cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                return print(line)