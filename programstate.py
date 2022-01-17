class ProgramState():
    def __init__(self):
        self.currentWidgetList = []
        self.alwaysOnWidgetList =[]
        self.testWidgetList = []
        self.learnWidgetList = []
        self.browseWidgetList = []
        self.currentHsk = 1;
        self.listOfAllCharacters = []
        self.listOfTrainingCharacters = []
        self.listOfLearnedCharacters = []
        self.currentLearningIndex = 0
        self.currentTrainingIndex = 0

    def createList(self,listVar,*args):
        for arg in args:
            listVar.append(arg)
    def removeWidgets(self,listVar):
        for element in listVar:
            element.place_forget()
    def addToList(self,listVar):
        return lambda sign : listVar.append(sign)

    def dropFromList(self,listVar):
        return lambda sign : listVar.drop(sign)

    def clearList(self,listVar):
        listVar.clear()
    def setPageNumber(self,page):
        self.whatPage = page
    def getPageNumber(self):
        return self.whatPage
    def setCurrentHsk(self,hsk):
        self.currentHsk = hsk
    def getCurrentHsk(self):
        return self.currentHsk
    def placeAlwaysOnWidgetList(self):
        self.browseWidgetList[0].place(x=30, y=17)
        self.browseWidgetList[1].place(x=186.0, y=103.0, width=158.0, height=46.0)
        self.browseWidgetList[2].place(x=355.0, y=103.0, width=158.0, height=46.0)
        self.browseWidgetList[3].place(x=524.0, y=104.0, width=158.0, height=46.0)
    def placeLearnMode(self):
        self.currentWidgetList = self.learnWidgetList
        self.learnWidgetList[0].place(x=30.0, y=191.0)
        self.learnWidgetList[1].place(x=520.0, y=680.0, width=90.0, height=51.0)
        self.learnWidgetList[2].place(x=520.0, y=740.0, width=90.0, height=51.0)
        self.learnWidgetList[3].place(x=819.0, y=708.0, width=158.0, height=46.0)
        self.learnWidgetList[4].place(x=1006.0, y=708.0, width=158.0, height=46.0)
        self.learnWidgetList[5].place(x=30.0, y=700.0)
        self.learnWidgetList[6].place(x=300.0, y=700.0)
        self.learnWidgetList[7].place(x=761.0, y=156.0)
        self.learnWidgetList[8].place(x=979.0, y=156.0)
        self.learnWidgetList[9].place(x=630.0, y=201.0)
        self.learnWidgetList[10].place(x=979.0, y=201.0)
        self.learnWidgetList[11].place(x=670.0, y=246.0)
        self.learnWidgetList[12].place(x=979.0, y=246.0)
        self.learnWidgetList[13].place(x=630.0, y=291.0)
        self.learnWidgetList[14].place(x=979.0, y=291.0)
        self.learnWidgetList[15].place(x=630.0, y=336.0)
        self.learnWidgetList[16].place(x=630.0, y=381)
        self.learnWidgetList[17].place(x=975, y=382, height=282)

    def placeBrowseMode(self):
        self.currentWidgetList = self.browseWidgetList
        self.browseWidgetList[0].place(x=200.0, y=160.0)
        self.browseWidgetList[1].place(x=200.0, y=205)
        self.browseWidgetList[2].place(x=880, y=206, height=352)

    def placeTestMode(self):
        self.currentWidgetList = self.testWidgetList
        self.testWidgetList[0].place(x=370.0, y=191.0)
        self.testWidgetList[1].place(x=900.0, y=350.0, width=90.0, height=51.0)
        self.testWidgetList[2].place(x=1000.0, y=350.0, width=90.0, height=51.0)
        self.testWidgetList[3].place(x=819.0, y=708.0, width=158.0, height=46.0)
        self.testWidgetList[4].place(x=1006.0, y=708.0, width=158.0, height=46.0)
        self.testWidgetList[5].place(x=880.0, y=191.0)
        self.testWidgetList[6].place(x=1000.0, y=240.0)
        self.testWidgetList[7].place(x=0.0, y=191.0)
        self.testWidgetList[8].place(x=0.0, y=236)
        self.testWidgetList[9].place(x=345, y=237, height=282)

    def placeAlwaysOnWidgets(self):
        self.alwaysOnWidgetList[0].place(x=30, y=17)
        self.alwaysOnWidgetList[1].place(x=186.0, y=103.0, width=158.0, height=46.0)
        self.alwaysOnWidgetList[2].place(x=355.0, y=103.0, width=158.0, height=46.0)
        self.alwaysOnWidgetList[3].place(x=524.0, y=104.0, width=158.0, height=46.0)