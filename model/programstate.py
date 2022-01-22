import model.hanzicharacter as hc
import model.savetopdf as sp
class ProgramState:
    def __init__(self):
        self.currentHsk = 1
        p = hc.PageScrapper(str(self.currentHsk))
        self.listOfAllCharactersInHSK = p.getHanziList()
        self.listOfLeftCharactersInHSK = self.listOfAllCharactersInHSK
        self.listOfLearningCharacters = []
        self.listOfTestingCharacters = []
        self.listOfLearnedCharacters = []
        self.currentLearningIndex = 0
        self.currentTestingIndex = 0
        self.saver = sp.pdfSaver()

    def addToList(self, whatList):
        return lambda sign: whatList.append(sign)

    def removeFromList(self, whatList):
        return lambda sign: whatList.remove(sign)

    def printResults(self):
        self.saver.saveLearningResults(self)

    def changeHsk(self,newHsk):
        self.currentHsk = newHsk
        p = hc.PageScrapper(str(self.currentHsk))
        self.listOfAllCharactersInHSK = p.getHanziList()
        self.listOfLeftCharactersInHSK = self.listOfAllCharactersInHSK
        self.listOfLearningCharacters = []
        self.listOfTestingCharacters = []
        self.listOfLearnedCharacters = []
        self.currentLearningIndex = 0
        self.currentTestingIndex = 0