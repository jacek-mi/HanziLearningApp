class BrowseModeUtil:
    def __init__(self,state):
        self.state = state
        self.pageData = {
            "signList": ""
        }
        self.InitialPageList()

    def generateBrowsingPageDataAfterAdd(self,start,end):
        if self.state.listOfLeftCharactersInHSK:
            self.BrowsePageDataFor(start, end)
            return self.pageData
        self.pageData = dict.fromkeys(self.pageData, "")
        return self.pageData

    def BrowsePageDataFor(self,start,end):
        addToLearningCharacters = self.state.addToList(self.state.listOfLearningCharacters)
        remFromLeftCharactersInHSK = self.state.removeFromList(self.state.listOfLeftCharactersInHSK)
        text = ""
        for key in self.state.listOfLeftCharactersInHSK:
            text = text + key + " "
        for i in range(start, end):
            if text[i] != " ":
                addToLearningCharacters(text[i])
                remFromLeftCharactersInHSK(text[i])
        text = ""
        for key in self.state.listOfLeftCharactersInHSK:
            text = text + key + " "
        self.pageData["signList"]=text

    def InitialPageList(self):
        text=""
        for key in self.state.listOfLeftCharactersInHSK:
            text = text + key + " "
        self.pageData["signList"]=text