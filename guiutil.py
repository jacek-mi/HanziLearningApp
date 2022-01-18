import tkinter as tk
@staticmethod
def clearCanvas(canvas):
    canvas.create_rectangle(0, 0, 520, 500, fill='white')
@staticmethod
def paint(event,canvas):
    # Co-ordinates.
    x1, y1, x2, y2 = (event.x - 9), (event.y - 9), (event.x + 9), (event.y + 9)
    # Colour
    Colour = "black"
    # specify type of display
    canvas.create_oval(x1, y1, x2,
                       y2, fill=Colour)

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

def setTrainingUI(state,hc):
    hanzi = state.listOfTrainingCharacters[state.currentTrainingIndex]
    c = hc.Character(hanzi)
    setTrainingTranslation(state, hanzi, c)

def setValuesOfLearningUI(state,c,hanzi):
    state.learnWidgetList[8]["text"] = hanzi
    state.learnWidgetList[10]["text"] = c.strokesNumber
    state.learnWidgetList[12]["text"] = c.frequencyRank
    state.learnWidgetList[14]["text"] = c.codepoint


def startSettingTranslation(state):
    state.learnWidgetList[16].configure(state='normal')
    state.learnWidgetList[16].delete(1.0, tk.END)

def endSettingTranslation(state,text):
    state.learnWidgetList[16].insert('end', text)
    state.learnWidgetList[16].configure(state='disabled')

def setLearningTranslation(state,c):
    startSettingTranslation(state)
    text=""
    for key in c.translation:
        text = text + key + "\n\n"
        for tr in c.translation[key]:
            text = text + " -" + tr + "\n"
        text = text + "\n"
    endSettingTranslation(state,text)
def setTrainingTranslation(state,hanzi,c):
    startSettingTranslation(state)
    text=""
    for key in c.translation:
        for tr in c.translation[key]:
            text = text + " -" + tr.replace(hanzi, "") + "\n"
        text = text + "\n"
    endSettingTranslation(state,text)