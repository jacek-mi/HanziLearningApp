import model.hanzicharacter as hc
import model.imagerecognition as ir
class TestModeUtil:
    def __init__(self,state):
        self.state = state
        self.pageData  = {
            "capturedSign": "",
            "translation": "",
            "announcement": ""
        }
        self.recognition = ir.ImageRecognition()

    def generateTestingPageDataAfterStart(self):
        if self.state.listOfTestingCharacters:
            self.testingPageDataFor(self.state.listOfTestingCharacters[self.state.currentTestingIndex])
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def generateTestingPageDataAfterNext(self):
        if self.state.listOfTestingCharacters:
            max = len(self.state.listOfTestingCharacters)
            self.state.currentTestingIndex = self.state.currentTestingIndex + 1
            if self.state.currentTestingIndex > max - 1:
                self.state.currentTestingIndex = 0
            self.testingPageDataFor(self.state.listOfTestingCharacters[self.state.currentTestingIndex])
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def generateTestingPageDataAfterPrevious(self):
        if self.state.listOfTestingCharacters:
            max = len(self.state.listOfTestingCharacters)
            self.state.currentTestingIndex = self.state.currentTestingIndex - 1
            if self.state.currentTestingIndex < 0:
                self.state.currentTestingIndex = max - 1
            self.testingPageDataFor(self.state.listOfTestingCharacters[self.state.currentTestingIndex])
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def generateTestingPageDataAfterCheck(self):
        sign = self.recognition.recognize()
        if self.state.listOfTestingCharacters:

            self.pageData["capturedSign"] = sign
            if sign == self.state.listOfTestingCharacters[self.state.currentTestingIndex]:
                addToLearnedCharacters = self.state.addToList(self.state.listOfLearnedCharacters)
                remFrTestingCharacters = self.state.removeFromList(self.state.listOfTestingCharacters)
                addToLearnedCharacters(sign)
                remFrTestingCharacters(sign)
                self.state.currentTestingIndex =0
                self.generateTestingPageDataAfterStart()
                self.pageData["capturedSign"] = sign
                self.pageData["announcement"] = "Well Done"
                return self.pageData
            else:
                self.testingPageDataFor(self.state.listOfTestingCharacters[self.state.currentTestingIndex])
                self.pageData["capturedSign"] = sign
                self.pageData["announcement"] = "Uncorrect Sign"
                return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        self.pageData["capturedSign"] = sign
        return self.pageData

    def testingPageDataFor(self,sign):
        signData = hc.Character(sign)
        self.pageData["capturedSign"]=" "
        text = ""
        for key in signData.translation:
            for tr in signData.translation[key]:
                text = text + " -" + tr + "\n"
            text = text + "\n"
        self.pageData["translation"]=text
        self.pageData["announcement"]=""


