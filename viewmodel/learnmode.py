import tkinter as tk
from model.learnmodeutil import LearnModeUtil
class LearnMode:
    def __init__(self, widgets,state):
        self.widgets = widgets
        self.util = LearnModeUtil(state)

    def place(self):
        self.widgets[0].place(x=30.0, y=191.0)
        self.widgets[1].place(x=520.0, y=680.0, width=90.0, height=51.0)
        self.widgets[2].place(x=520.0, y=740.0, width=90.0, height=51.0)
        self.widgets[3].place(x=819.0, y=708.0, width=158.0, height=46.0)
        self.widgets[4].place(x=1006.0, y=708.0, width=158.0, height=46.0)
        self.widgets[5].place(x=30.0, y=700.0)
        self.widgets[6].place(x=300.0, y=700.0)
        self.widgets[7].place(x=761.0, y=156.0)
        self.widgets[8].place(x=979.0, y=156.0)
        self.widgets[9].place(x=630.0, y=201.0)
        self.widgets[10].place(x=979.0, y=201.0)
        self.widgets[11].place(x=670.0, y=246.0)
        self.widgets[12].place(x=979.0, y=246.0)
        self.widgets[13].place(x=630.0, y=291.0)
        self.widgets[14].place(x=979.0, y=291.0)
        self.widgets[15].place(x=630.0, y=336.0)
        self.widgets[16].place(x=630.0, y=381)
        self.widgets[17].place(x=975, y=382, height=282)
        self.widgets[18].place(x=1000, y=420)
        self.widgets[19].place(x=30.0, y=750.0)
        self.openPage()

    def openPage(self):
        pageData = self.util.generateLearningPageDataAfterStart()
        self.setPageData(pageData)

    def addCharacter(self):
        pageData = self.util.generateLearningPageDataAfterAdd()
        self.setPageData(pageData)

    def nextCharacter(self):
        pageData = self.util.generateLearningPageDataAfterNext()
        self.setPageData(pageData)

    def previousCharacter(self):
        pageData = self.util.generateLearningPageDataAfterPrevious()
        self.setPageData(pageData)
    def checkCanvas(self):
        pageData = self.util.generateLearningPageDataAfterCheck()
        self.setPageData(pageData)

    def setPageData(self,pageData):
        self.widgets[6]["text"] = pageData["capturedSign"]
        self.widgets[8]["text"] = pageData["sign"]
        self.widgets[10]["text"] = pageData["strokesNumber"]
        self.widgets[12]["text"] = pageData["frequencyRank"]
        self.widgets[14]["text"] = pageData["codepoint"]
        self.widgets[16].configure(state='normal')
        self.widgets[16].delete(1.0, tk.END)
        self.widgets[16].insert('end', pageData['translation'])
        self.widgets[16].configure(state='disabled')
        self.widgets[19]["text"] = pageData["announcement"]