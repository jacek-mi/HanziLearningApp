import model.hanzicharacter as hc
import model.imagerecognition as ir
class LearnModeUtil:
    def __init__(self,state):
        self.state = state
        self.pageData  = {
            "capturedSign": "",
            "sign": "None",
            "strokesNumber": "",
            "frequencyRank": "",
            "codepoint": "",
            "translation": ""
        }
        self.recognition = ir.ImageRecognition()

    def generateLearningPageDataAfterStart(self):
        if self.state.listOfLearningCharacters:
            self.learningPageDataFor(self.state.listOfLearningCharacters[self.state.currentLearningIndex])
            return self.pageData
        self.state.currentLearningIndex = 0
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def generateLearningPageDataAfterAdd(self):
        if self.state.listOfLearningCharacters:
            currSign = self.state.listOfLearningCharacters[self.state.currentLearningIndex]
            addToTrainingCharacters = self.state.addToList(self.state.listOfTestingCharacters)
            remFrLearningCharacters = self.state.removeFromList(self.state.listOfLearningCharacters)
            addToTrainingCharacters(currSign)
            remFrLearningCharacters(currSign)
            if self.state.listOfLearningCharacters:
                self.state.currentLearningIndex = 0
                self.learningPageDataFor(self.state.listOfLearningCharacters[self.state.currentLearningIndex])
                return  self.pageData
        self.state.currentLearningIndex = 0
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData


    def generateLearningPageDataAfterNext(self):
        if self.state.listOfLearningCharacters:
            max = len(self.state.listOfLearningCharacters)
            self.state.currentLearningIndex = self.state.currentLearningIndex + 1
            if (self.state.currentLearningIndex > max -1):
                self.state.currentLearningIndex = 0
            self.learningPageDataFor(self.state.listOfLearningCharacters[self.state.currentLearningIndex])
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def generateLearningPageDataAfterPrevious(self):
        if self.state.listOfLearningCharacters:
            max = len(self.state.listOfLearningCharacters)
            self.state.currentLearningIndex = self.state.currentLearningIndex - 1
            if (self.state.currentLearningIndex < 0 ):
                self.state.currentLearningIndex = max - 1
            self.learningPageDataFor(self.state.listOfLearningCharacters[self.state.currentLearningIndex])
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def generateLearningPageDataAfterCheck(self):
        if self.state.listOfLearningCharacters:
            self.learningPageDataFor(self.state.listOfLearningCharacters[self.state.currentLearningIndex])
            self.pageData["capturedSign"]=self.recognition.recognize()
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        self.pageData["capturedSign"] = self.recognition.recognize()
        return self.pageData

    def learningPageDataFor(self,sign):
        signData = hc.Character(sign)
        self.pageData["capturedSign"]=""
        self.pageData["sign"] = sign
        self.pageData["strokesNumber"] = signData.strokesNumber
        self.pageData["frequencyRank"] = signData.frequencyRank
        self.pageData["codepoint"] = signData.codepoint
        text = ""
        for key in signData.translation:
            text = text + key + "\n\n"
            for tr in signData.translation[key]:
                text = text + " -" + tr + "\n"
            text = text + "\n"
        self.pageData["translation"]=text


