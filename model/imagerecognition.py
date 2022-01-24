import pytesseract
from PIL import Image
import os


class ImageRecognition:
    def __init__(self):
        self.path= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.checklist = ["下","免","水","些","的"]



    def checkIfCapturedSignIsCorrect(self,state,sign):
        if (state.listOfTrainingCharacters[state.currentTrainingIndex]== sign):
            return True
        return False

    def paste(self,sign):
        d = os.getcwd()
        d = d + '/model/hanzirecognition/'
        background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 255))
        if sign in self.checklist:
            index = self.checklist.index(sign)
            for i in range(5):
                if i == index:
                    img = Image.open(d + 'image.png', 'r')
                else :
                    img = Image.open(d + str(i) + ".png")
                img = img.resize((100, 100))
                background.paste(img, (i * 100, 500))
        else :
            for i in range(5):
                img = Image.open(d + str(i) + ".png")
                img = img.resize((100, 100))
                background.paste(img, (i*100, 500))
            img = Image.open(d + 'image.png', 'r')
            img = img.resize((100, 100))
            background.paste(img, (i * 100, 500))
        background.save(d + 'out.png')
    def calculate(self,sign):
        d = os.getcwd()
        d = d + '/model/hanzirecognition/'
        img = Image.open(d + 'out.png')
        text = pytesseract.image_to_string(img, lang='chi_sim')
        for i in self.checklist:
            if i != sign:
                text = text.replace(i, "")
        text=text.strip().replace(" ","")
        return text

    def recognize(self,sign):
        self.paste(sign)
        return self.calculate(sign)