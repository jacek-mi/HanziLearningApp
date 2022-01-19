import pytesseract
from PIL import Image
from PIL import ImageGrab
import cv2
class ImageRecognition:
    def __init__(self):
        self.path= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    @staticmethod
    def checkIfMatch(label1, label2):
        if (label1["text"] == label2["text"]):
            return True
        return False
    def checkIfCapturedSignIsCorrect(self,state,sign):
        if (state.listOfTrainingCharacters[state.currentTrainingIndex]== sign):
            return True
        return False

    def getter(self,widget,window,frame):
        x = window.winfo_rootx() + frame.winfo_x() + widget.winfo_x()
        y = window.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save('hanzirecognition/image.png')
    def paste(self):
        img1 = Image.open('hanzirecognition/first.png')
        img1 = img1.resize((100, 100))
        img2 = Image.open('hanzirecognition/second.png')
        img2 = img2.resize((100, 100))
        img3 = Image.open('hanzirecognition/third.png')
        img3 = img3.resize((100, 100))
        img = Image.open('hanzirecognition/image.png', 'r')
        img = img.resize((100, 100))
        background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 255))
        background.paste(img1, (100, 500))
        background.paste(img2, (200, 500))
        background.paste(img3, (300, 500))
        background.paste(img, (400, 500))
        background.save('hanzirecognition/out.png')
    def calculate(self):
        img = cv2.imread('hanzirecognition/out.png')
        text = pytesseract.image_to_string(img, lang='chi_sim')
        return  text[len(text) - 2]

    def recognize(self,canvas,window,frame):
        self.getter(canvas, window, frame)
        self.paste()
        return self.calculate()