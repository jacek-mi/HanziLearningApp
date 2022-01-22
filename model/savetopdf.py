from fpdf import FPDF
import requests
import warnings
import os
class pdfSaver:
    def __init__(self):
        self.pdf = FPDF()
    def saveLearningResults(self,state):
        if state.listOfLearnedCharacters:
            from fpdf import FPDF
            self.pdf.add_page()
            d = os.getcwd()
            d = d + '/model/font/font.ttf'
            self.pdf.add_font('font','',d,uni=True)
            self.pdf.set_font('Arial', '', 25)
            self.pdf.write(8,"After this session you have learned:\n")
            self.pdf.ln(2)
            self.pdf.set_font('font', '', 15)

            def createSignLink(link):
                return lambda sign :  link + requests.utils.quote(sign) ;
            hanzidbLink = createSignLink("http://hanzidb.org/character/")

            for sign in state.listOfLearnedCharacters:
                self.pdf.write(10,sign + " ", hanzidbLink(sign))
                
            warnings.filterwarnings("ignore")
            self.pdf.output("result.pdf", 'F')
            warnings.filterwarnings("always")