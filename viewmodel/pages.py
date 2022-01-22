from viewmodel.testmode import TestMode
from viewmodel.learnmode import LearnMode
from viewmodel.browsemode import BrowseMode
from model.programstate import ProgramState

from PIL import ImageGrab
import os


class Pages:
    def __init__(self,window,frame):
        self.window = window
        self.frame = frame
        self.currentWidgetList = []
        self.alwaysOnWidgetList = []
        self.browseWidgetList = []
        self.testWidgetList = []
        self.learnWidgetList = []
        self.state = ProgramState()

    def initializeModes(self):
        self.placeAlwaysOnWidgets()
        self.browseMode = BrowseMode(self.browseWidgetList,self.state)
        self.testMode = TestMode(self.testWidgetList,self.state)
        self.learnMode = LearnMode(self.learnWidgetList,self.state)

    def placeAlwaysOnWidgets(self):
        self.alwaysOnWidgetList[0].place(x=30, y=17)
        self.alwaysOnWidgetList[1].place(x=186.0, y=103.0, width=158.0, height=46.0)
        self.alwaysOnWidgetList[2].place(x=355.0, y=103.0, width=158.0, height=46.0)
        self.alwaysOnWidgetList[3].place(x=524.0, y=104.0, width=158.0, height=46.0)

    def createList(self,listVar,*args):
        for arg in args:
            listVar.append(arg)
    def removeWidgets(self,listVar):
        for element in listVar:
            element.place_forget()

    def clearPage(self):
        self.removeWidgets(self.currentWidgetList)

    def clearCanvas(self):
        if self.currentWidgetList == self.testWidgetList or self.currentWidgetList == self.learnWidgetList:
            self.currentWidgetList[0].create_rectangle(0, 0, 520, 500, fill='white')

    def paintOnCanvas(self,event):
        if self.currentWidgetList == self.testWidgetList or self.currentWidgetList == self.learnWidgetList:
            x1, y1, x2, y2 = (event.x - 9), (event.y - 9), (event.x + 9), (event.y + 9)
            self.currentWidgetList[0].create_oval(x1, y1, x2, y2, fill="Black")

    def enterBrowseMode(self):
        self.clearPage()
        self.currentWidgetList = self.browseWidgetList
        self.browseMode.place()
    
    def enterTestMode(self):
        self.clearPage()
        self.currentWidgetList = self.testWidgetList
        self.clearCanvas()
        self.testMode.place()

    def enterLearnMode(self):
        self.clearPage()
        self.currentWidgetList = self.learnWidgetList
        self.clearCanvas()
        self.learnMode.place()

    def addButton(self):
        if self.currentWidgetList == self.learnWidgetList:
            self.learnMode.addCharacter()
        if self.currentWidgetList == self.browseWidgetList:
            self.browseMode.addCharacter()
    
    def nextButton(self):
        if self.currentWidgetList == self.learnWidgetList:
            self.learnMode.nextCharacter()
        if self.currentWidgetList == self.testWidgetList:
            self.testMode.nextCharacter()
    
    def previousButton(self):
        if self.currentWidgetList == self.learnWidgetList:
            self.learnMode.previousCharacter()
        if self.currentWidgetList == self.testWidgetList:
            self.testMode.previousCharacter()
    
    def checkButton(self):
        self.getter(self.currentWidgetList[0])
        if self.currentWidgetList == self.learnWidgetList:
            self.learnMode.checkCanvas()
        if self.currentWidgetList == self.testWidgetList:
            self.testMode.checkCanvas()
        self.clearCanvas()

    def getter(self, widget):
        x = self.window.winfo_rootx() + self.frame.winfo_x() + widget.winfo_x()
        y = self.window.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        d = os.getcwd()
        d = d + '/model/hanzirecognition/image.png'
        ImageGrab.grab().crop((x, y, x1, y1)).save(d)

    def printRessultsButton(self):
        self.state.printResults()

    def keyHandler(self,event):
        pass

    def selectResultsButton(self):
        self.browseMode.selectResults(self.state)
