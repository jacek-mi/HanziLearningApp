
import savetopdf
import random
import tkinter as tk

import hanzicharacter as hc
import imagerecognition as ir
import programstate as ps
import guiutil as gu

from tkinter import ttk
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main():

    state = ps.ProgramState()
    recognition=ir.ImageRecognition()
    p = hc.PageScrapper('1')
    state.listOfAllCharacters = p.getHanziList()
    window = tk.Tk()
    window.title('Project')
    window.geometry("1200x800")
    window.resizable(False, False)
    frame = tk.Frame(master=window, width=1200, height=800,bg="#256150")
    frame.pack()
    addButtonImage = tk.PhotoImage(file=relative_to_assets("add.png"))
    addButton = tk.Button(image=addButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: addToLearningList(),relief="flat")
    title = tk.Label(frame, bg="#256150", anchor="nw", text="Hanzi Learing App",
                     font=("Montserrat Bold", 64 * -1), fg="#FFFFFF")
    canvas = tk.Canvas(frame, bg="white",height=480.0,width=500.0)

    learnButtonImage = tk.PhotoImage(file=relative_to_assets("learn.png"))
    learnButton = tk.Button(image=learnButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: learnModePlaceButton(),relief="flat")

    practiceButtonImage = tk.PhotoImage(file=relative_to_assets("practice.png"))
    practiceButton = tk.Button(image=practiceButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: testModePlaceButton(),relief="flat")
    browseButtonImage = tk.PhotoImage(file=relative_to_assets("browse.png"))
    browseButton = tk.Button(image=browseButtonImage,borderwidth=0,highlightthickness=0,
                             command=lambda: browseModePlaceButton(),relief="flat")

    clearButtonImage = tk.PhotoImage(file=relative_to_assets("clear.png"))
    clearButton = tk.Button(image=clearButtonImage,borderwidth=0,highlightthickness=0,
    command=lambda: gu.clearCanvas(canvas) ,relief="flat")

    checkButtonImage = tk.PhotoImage(file=relative_to_assets("check.png"))
    checkButton = tk.Button(image=checkButtonImage,borderwidth=0,highlightthickness=0,
    command=lambda: recognizeHanzi(state,capturedCharacterData, recognition, canvas, window, frame)
    ,relief="flat")

    previousButtonImage = tk.PhotoImage(
        file=relative_to_assets("previous.png"))
    previousButton = tk.Button(image=previousButtonImage,borderwidth=0,highlightthickness=0,
                               command=lambda: getPreviousCharacter(),relief="flat")

    nextButtonImage = tk.PhotoImage(file=relative_to_assets("next.png"))
    nextButton = tk.Button(image=nextButtonImage,borderwidth=0,highlightthickness=0,
                           command=lambda: getNextCharacter(),relief="flat")

    capturedCharacter = tk.Label(frame, bg="#256150", anchor="nw", text="Captured Sign:",
                                 font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    capturedCharacterData = tk.Label(frame, bg="#256150", anchor="nw", text="Data",
                                     font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    capturedCharacterData.place(x=300.0, y=700.0)

    signHanzi = tk.Label(frame, bg="#256150", anchor="nw", text="Sign Hanzi:",
                         font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    signHanziData = tk.Label(frame, bg="#256150", anchor="nw", text="Data",
                             font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    numberOfStrokes = tk.Label(frame, bg="#256150", anchor="nw", text="Number of Strokes:",
                               font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    numberOfStrokesData = tk.Label(frame, bg="#256150", anchor="nw", text="Num",
                                font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    frequencyRank = tk.Label(frame, bg="#256150", anchor="nw", text="Frequency Rank:",
                             font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    frequencyRankData = tk.Label(frame, bg="#256150", anchor="nw", text="Rank",
                                 font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    unicodeCodepoint = tk.Label(frame, bg="#256150", anchor="nw", text="Unicode Codepoint:",
                                font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    unicodeCodepointData = tk.Label(frame, bg="#256150", anchor="nw", text="Cpoint",
                                    font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    translation = tk.Label(frame, bg="#256150", anchor="nw", text="Translation:",
                           font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    translationData = tk.Text(window, height=8, width=20, fg="white", bg="gray10",
                              font=("Montserrat Bold", 30 * -1),wrap=tk.WORD)
    translationData.configure(state='normal')

    scrollbar = ttk.Scrollbar(window,orient='vertical',command=translationData.yview)

    translationData['yscrollcommand'] = scrollbar.set

    currentListOfSigns = tk.Label(frame, bg="#256150", anchor="nw", text="Current List Of Signs:",
                           font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    currentListOfSignsData = tk.Text(window, height=10, width=40, fg="white", bg="gray10",
                              font=("Montserrat Bold", 30 * -1), wrap=tk.WORD)

    scrollbarList = ttk.Scrollbar(window, orient='vertical', command=currentListOfSignsData.yview)

    currentListOfSignsData['yscrollcommand'] = scrollbarList.set
    currentListOfSignsData.configure(state='normal')
    currentListOfSignsData.delete(1.0, tk.END)

    text = ""
    for key in state.listOfAllCharacters:
        text = text + key + " "

    currentListOfSignsData.insert('end', text)
    currentListOfSignsData.configure(state='disabled')

    def handle_keypress(event):
        if (event.char == 'd'):
            savetopdf.saveLearningResults(state)
        if (event.char == 'f'):
            learnModePlaceButton()
        if (event.char == 'c'):
            gu.clearCanvas(canvas)
        if (event.char == 'r'):
            getRandomCharacter()
        if (event.char == 'x'):
            recognition.getter(canvas,window,frame)
            recognition.paste()
            capturedCharacterData["text"]=recognition.calculate()
        if (event.char == 'e'):
            if (recognition.checkIfMatch(capturedCharacterData, signHanziData)):
                print("wow")

    def recognizeHanzi(state,capturedCharacterData, recognition, canvas, window, frame):
        if state.currentWidgetList==state.learnWidgetList:
            capturedCharacterData["text"] = recognition.recognize(canvas, window, frame)
        if state.currentWidgetList==state.testWidgetList and state.listOfTrainingCharacters:
            sign = recognition.recognize(canvas, window, frame)
            if recognition.checkIfCapturedSignIsCorrect(state,sign):
                addToLearnedL = state.addToList(state.listOfLearnedCharacters)
                remFromTL = state.removeFromList(state.listOfTrainingCharacters)
                addToLearnedL(sign)
                remFromTL(sign)
                print(state.listOfLearnedCharacters)
                setNewValues()
                gu.clearCanvas(canvas)

    def clearPage():
        state.removeWidgets(state.currentWidgetList)
    def testModePlaceButton():
        clearPage()
        gu.clearCanvas(canvas)
        state.placeTestMode()
        setNewValues()
    def learnModePlaceButton():
        clearPage()
        gu.clearCanvas(canvas)
        state.placeLearnMode()
        setNewValues()
    def browseModePlaceButton():
        clearPage()
        gu.clearCanvas(canvas)
        state.placeBrowseMode()
    def paint(event):
        gu.paint(event,canvas)

    def getNextCharacter():
        gu.getNextCharacter(state,hc)

    def getPreviousCharacter():
        gu.getPreviousCharacter(state,hc)

    def getRandomCharacter():
        #hanzi = chr(int(listOfCharacters[random.randint(0, len(listOfCharacters) - 1)], base=16))
        hanzi = listOfCharacters[random.randint(0, len(listOfCharacters) - 1)]
        signHanziData["text"] = hanzi
        # c = hc.Character(chr(int(hanzi, base=16)))
        c=hc.Character(hanzi)
        numberOfStrokesData["text"]=c.strokesNumber
        frequencyRankData["text"]=c.frequencyRank
        unicodeCodepointData["text"]=c.codepoint
        translationData.configure(state='normal')
        translationData.delete(1.0, tk.END)
        text = ""
        for key in c.translation:
            text = text + key + "\n\n"
            for tr in c.translation[key]:
                text = text + " -" + tr + "\n"
            text = text + "\n"

        translationData.insert('end', text)
        translationData.configure(state='disabled')
    def addToLearningList():
        gu.addCharacter(state,hc,canvas)

    def setNewValues():
        gu.setNewValues(state,hc)

    state.createList(state.alwaysOnWidgetList,title,learnButton,practiceButton,browseButton)
    state.createList(state.browseWidgetList, currentListOfSigns, currentListOfSignsData,
                     scrollbarList,addButton)

    state.createList(state.testWidgetList,canvas,clearButton,checkButton,previousButton,nextButton,
                     capturedCharacter,capturedCharacterData,translation,translationData,scrollbar)

    state.createList(state.learnWidgetList,canvas,clearButton,checkButton,previousButton,
                     nextButton,capturedCharacter,capturedCharacterData,signHanzi,signHanziData,
                     numberOfStrokes,numberOfStrokesData,frequencyRank,frequencyRankData,
                     unicodeCodepoint,unicodeCodepointData,translation,translationData,scrollbar,addButton)

    state.placeAlwaysOnWidgets()
    learnModePlaceButton()
    window.bind('<Key>', handle_keypress)
    canvas.bind("<B1-Motion>", paint)
    window.mainloop()

def readLineByLine():
    f = open("TGSCC-Unicode.txt", 'r')
    lines = f.readlines()
    list = []
    for line in lines:
        list.append(line.partition("\t")[2].strip().replace("U+", ""))
    print(chr(int(list[0], base=16)))
    return list



if __name__ == "__main__":
    main()




