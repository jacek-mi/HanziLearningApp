import tkinter as tk

def clearCanvas(canvas):
    canvas.create_rectangle(0, 0, 520, 500, fill='white')

def paint(event,canvas):
    # Co-ordinates.
    x1, y1, x2, y2 = (event.x - 9), (event.y - 9), (event.x + 9), (event.y + 9)
    # Colour
    Colour = "black"
    # specify type of display
    canvas.create_oval(x1, y1, x2,
                       y2, fill=Colour)

def addCharacter(state,hc):
    if state.currentWidgetList == state.learnWidgetList and state.listOfLearningCharacters:
        addToTrainingList(state,hc)
    elif state.browseWidgetList[1].tag_ranges("sel") and state.listOfAllCharacters:
        addToLearningList(state)

def addToTrainingList(state,hc):
    addToTL = state.addToList(state.listOfTrainingCharacters)
    remFromLL = state.removeFromList(state.listOfLearningCharacters)
    addToTL(state.learnWidgetList[8]["text"])
    remFromLL(state.learnWidgetList[8]["text"])
    state.currentLearningIndex = 0
    setNewValues(state, hc)
    getNextCharacter(state, hc)

def addToLearningList(state):
    addToLL = state.addToList(state.listOfLearningCharacters)
    remFromAL = state.removeFromList(state.listOfAllCharacters)
    start = int(str(state.browseWidgetList[1].tag_ranges("sel")[0]).replace("1.", ""))
    end = int(str(state.browseWidgetList[1].tag_ranges("sel")[1]).replace("1.", ""))
    text = ""
    for key in state.listOfAllCharacters:
        text = text + key + " "
    for i in range(start, end):
        if text[i] != " ":
            addToLL(text[i])
            remFromAL(text[i])
    text = ""
    for key in state.listOfAllCharacters:
        text = text + key + " "
    print(text)
    state.browseWidgetList[1].tag_remove(tk.SEL, "1.0", tk.END)
    state.browseWidgetList[1].configure(state='normal')
    state.browseWidgetList[1].delete(1.0, tk.END)
    state.browseWidgetList[1].insert('end', text)
    state.browseWidgetList[1].configure(state='disabled')

def getNextCharacter(state,hc):
    if state.currentWidgetList == state.learnWidgetList:
        if state.listOfLearningCharacters:
            if (state.currentLearningIndex == len(state.listOfLearningCharacters) - 1):
                state.currentLearningIndex = 0
            else:
                state.currentLearningIndex = state.currentLearningIndex + 1
            setLearningUI(state,hc)
    if state.currentWidgetList == state.testWidgetList:
        if state.listOfTrainingCharacters:
            if (state.currentTrainingIndex == len(state.listOfTrainingCharacters) - 1):
                state.currentTrainingIndex = 0
            else:
                state.currentTrainingIndex = state.currentTrainingIndex + 1
            setTrainingUI(state,hc)

def getPreviousCharacter(state,hc):
    if state.currentWidgetList == state.learnWidgetList:
        if state.listOfLearningCharacters:
            if (state.currentLearningIndex == 0):
                state.currentLearningIndex = len(state.listOfLearningCharacters)-1
            else:
                state.currentLearningIndex = state.currentLearningIndex - 1
            setLearningUI(state,hc)
    if state.currentWidgetList == state.testWidgetList:
        if state.listOfTrainingCharacters:
            if (state.currentTrainingIndex == 0):
                state.currentTrainingIndex = len(state.listOfTrainingCharacters) - 1
            else:
                state.currentTrainingIndex = state.currentTrainingIndex - 1
            setTrainingUI(state,hc)

def setLearningUI(state,hc):
    hanzi = state.listOfLearningCharacters[state.currentLearningIndex]
    c = hc.Character(hanzi)
    setValuesOfLearningUI(state, c,hanzi)
    setLearningTranslation(state, c)

def setValuesOfLearningUI(state,c,hanzi):
    state.learnWidgetList[8]["text"] = hanzi
    state.learnWidgetList[10]["text"] = c.strokesNumber
    state.learnWidgetList[12]["text"] = c.frequencyRank
    state.learnWidgetList[14]["text"] = c.codepoint

def setLearningTranslation(state,c):
    startSettingTranslation(state)
    text=""
    for key in c.translation:
        text = text + key + "\n\n"
        for tr in c.translation[key]:
            text = text + " -" + tr + "\n"
        text = text + "\n"
    endSettingTranslation(state,text)

def startSettingTranslation(state):
    state.learnWidgetList[16].configure(state='normal')
    state.learnWidgetList[16].delete(1.0, tk.END)

def endSettingTranslation(state,text):
    state.learnWidgetList[16].insert('end', text)
    state.learnWidgetList[16].configure(state='disabled')

def setTrainingUI(state,hc):
    hanzi = state.listOfTrainingCharacters[state.currentTrainingIndex]
    c = hc.Character(hanzi)
    setTrainingTranslation(state, hanzi, c)

def setTrainingTranslation(state,hanzi,c):
    startSettingTranslation(state)
    text=""
    for key in c.translation:
        for tr in c.translation[key]:
            text = text + " -" + tr.replace(hanzi, "") + "\n"
        text = text + "\n"
    endSettingTranslation(state,text)


def setNewValues(state,hc):
    if state.currentWidgetList == state.learnWidgetList:
        if state.listOfLearningCharacters:
            setLearningUI(state,hc)
        else:
            setEmptyUI(state)
    if state.currentWidgetList == state.testWidgetList:
        if state.listOfTrainingCharacters:
            setTrainingUI(state,hc)
        else:
            setEmptyUI(state)

def setEmptyUI(state):
    text = ""
    state.learnWidgetList[8]["text"] = "Empty"
    state.learnWidgetList[10]["text"] = ""
    state.learnWidgetList[12]["text"] = ""
    state.learnWidgetList[14]["text"] = ""
    startSettingTranslation(state)
    endSettingTranslation(state,text)