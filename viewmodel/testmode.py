import tkinter as tk
from model.testmodeutil import  TestModeUtil
class TestMode:
    def __init__(self, widgets,state):
        self.widgets = widgets
        self.util = TestModeUtil(state)
    def place(self):
        self.widgets[0].place(x=370.0, y=191.0)
        self.widgets[1].place(x=900.0, y=350.0, width=90.0, height=51.0)
        self.widgets[2].place(x=1000.0, y=350.0, width=90.0, height=51.0)
        self.widgets[3].place(x=819.0, y=708.0, width=158.0, height=46.0)
        self.widgets[4].place(x=1006.0, y=708.0, width=158.0, height=46.0)
        self.widgets[5].place(x=880.0, y=191.0)
        self.widgets[6].place(x=1000.0, y=240.0)
        self.widgets[7].place(x=0.0, y=191.0)
        self.widgets[8].place(x=0.0, y=236)
        self.widgets[9].place(x=345, y=237, height=282)
        self.openPage()
    
    
    def openPage(self):
        pageData = self.util.generateTestingPageDataAfterStart()
        self.setPageData(pageData)
        
    def nextCharacter(self):
        pageData = self.util.generateTestingPageDataAfterNext()
        self.setPageData(pageData)

    def previousCharacter(self):
        pageData = self.util.generateTestingPageDataAfterPrevious()
        self.setPageData(pageData)
    def checkCanvas(self):
        pageData = self.util.generateTestingPageDataAfterCheck()
        self.setPageData(pageData)

    def setPageData(self,pageData):
        self.widgets[6]["text"] = pageData["capturedSign"]
        self.widgets[8].configure(state='normal')
        self.widgets[8].delete(1.0, tk.END)
        self.widgets[8].insert('end', pageData['translation'])
        self.widgets[8].configure(state='disabled')
    