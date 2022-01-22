import model.hanzicharacter as hc
class ProgramState():
    def __init__(self):
        
        self.currentHsk = 1;
        p = hc.PageScrapper(str(self.currentHsk))
        self.listOfAllCharactersInHSK = p.getHanziList()
        self.listOfLeftCharactersInHSK = self.listOfAllCharactersInHSK
        self.listOfLearningCharacters = []
        self.listOfTestingCharacters = []
        self.listOfLearnedCharacters = []
        self.currentLearningIndex = 0
        self.currentTestingIndex = 0

    def addToList(self, whatList):
        return lambda sign: whatList.append(sign)

    def removeFromList(self, whatList):
        return lambda sign: whatList.remove(sign)

    