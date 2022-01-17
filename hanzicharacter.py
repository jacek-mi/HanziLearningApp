from bs4 import BeautifulSoup
import requests
class Character:
    def __init__(self, hanzi):
        self.hanzi=hanzi
        w=WebScrapper(hanzi)
        data = w.getHanziData()
        self.translation = w.getTranslation()
        if 'Frequency rank' in data:
            self.frequencyRank = int(data['Frequency rank'])
        else:
            self.frequencyRank = 'None'
        if 'Number of strokes' in data:
            self.strokesNumber = int(data['Number of strokes'])
        else:
            self.strokesNumber = 'None'
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

class PageScrapper():
    def __init__(self,hsk):
        self.url = "http://hanzidb.org/character-list/hsk/level-" + str(hsk)
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
    def getHanziList(self):
        href = self.soup.find_all("a",href=True)
        pagesList = []
        signsOnPage = []
        for element in href:
            if self.url.replace('http://hanzidb.org/',"") in str(element):
                pagesList.append(
                    int(str(element).replace('<a href="/character-list/hsk/level-',"").replace('</a>',"").split(">")[1]))
        for element in href:
            if "Kangxi" not in str(element) and "character/" in str(element)  :
                signsOnPage.append(str(element).replace('">',"").replace('<a href="/character/',"").replace('</a>',"")[:1])
        for i in range(2,max(pagesList)+1):
            url = self.url + "?page=" + str(i)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            href = soup.find_all("a",href=True)
            for element in href:
                if "Kangxi" not in str(element) and "character/" in str(element):
                    signsOnPage.append(
                        str(element).replace('">', "").replace('<a href="/character/', "").replace('</a>', "")[:1])
        return list(dict.fromkeys(signsOnPage))
