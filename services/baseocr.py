class BASEOCR:
    def _init_(self,language:str ='en'):
        self.language = language
        
    def text_detection(self,image: str)->str:
        raise NotImplementedError