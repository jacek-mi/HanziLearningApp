from bs4 import BeautifulSoup
import requests
class Character:
    def __init__(self, hanzi):
        self.hanzi=hanzi
        w=WebScrapper(hanzi)
        data = w.getHanziData()
        self.translation = w.getTranslation()
        self.strokesNumber = int(data['Number of strokes'])
        self.frequencyRank = int(data['Frequency rank'])
        self.codepoint = "U+"+str(hex(ord(hanzi))).replace("0x","").upper()
        self.indexNumber = int(data['General standard index number'])
    def print(self):
        print(self.hanzi)
        for key in self.translation:
            print(key)
            print(self.translation[key])
        print("\nCodepoint " + str(self.codepoint))
        print("Frequency Rank " + str(self.frequencyRank))
        print("Number of strokes "+str(self.strokesNumber))
        print("Index number " +  str(self.indexNumber))

class WebScrapper():
    def __init__(self,hanzi):
        self.hanzi=hanzi
        self.url = "http://hanzidb.org/character/" + requests.utils.quote(hanzi)
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def getTranslation(self):
        results = self.soup.find_all("div", class_="ceent")
        keys=[]
        values=[]
        for result in results:
            keys.append(result.text.strip().partition(": ")[0])
            lines = result.text.strip().partition(": ")[2].replace("- ", "\n").strip().splitlines()
            values.append(lines)
        myDict = dict(zip(keys,values))
        return myDict
    def getHanziData(self):
        abo = self.soup.find_all("div", class_="abo")
        pageText = ""
        for element in abo:
            pParams =  element.find_all("p")
        for element in pParams:
            pageText = pageText + "\n" + element.text
        myList = pageText.replace("Examples", "\nExamples").replace("Other", "\nOther").strip().splitlines()
        myList = list(filter(("").__ne__, myList))
        keys = [x.partition(": ")[0] for x in myList]
        values = [x.partition(": ")[2] for x in myList]
        myDict = dict(zip(keys,values))
        return myDict

