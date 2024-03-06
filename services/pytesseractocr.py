from baseocr import BASEOCR
import pytesseract 
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

class PytesseractOCR(BASEOCR):
    def text_detection(self, image):
        text =pytesseract.image_to_string(image)
        return text