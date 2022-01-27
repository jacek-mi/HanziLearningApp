import viewmodel.pages as pg
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os

def drawUI():
    window = tk.Tk()
    d = os.getcwd()
    d = d + '/assets/'
    window.title('Project')
    window.geometry("1200x800")
    window.resizable(False, False)
    frame = tk.Frame(master=window, width=1200, height=800, bg="#256150")
    frame.pack()

    pagesViewModel = pg.Pages(window, frame)
    selectButtonImage = tk.PhotoImage(file= d + "select.png")
    selectButton = tk.Button(image=selectButtonImage, borderwidth=0,
                             highlightthickness=0, command=lambda: pagesViewModel.selectResultsButton(), relief="flat")
    checkedSignInformation = tk.Label(frame, bg="#256150", anchor="nw", text="TEST",
                               font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    CurrentHskLevel = tk.Label(frame, bg="#256150", anchor="nw", text="Current HSK: ",
                               font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    CurrentHskLevelSpinbox = ttk.Spinbox(frame, from_=1, to=6, wrap=True)
    printResultsButtonImage = tk.PhotoImage(file=d +"print.png")
    printResultsButton = tk.Button(image=printResultsButtonImage, borderwidth=0,
                                   highlightthickness=0, command=lambda: pagesViewModel.printRessultsButton(),
                                   relief="flat")

    addButtonImage = tk.PhotoImage(file=d + "add.png")
    addButton = tk.Button(image=addButtonImage, borderwidth=0, highlightthickness=0,
                          command=lambda: pagesViewModel.addButton(), relief="flat")

    title = tk.Label(frame, bg="#256150", anchor="nw", text="Hanzi Learing App",
                     font=("Montserrat Bold", 64 * -1), fg="#FFFFFF")
    canvas = tk.Canvas(frame, bg="white", height=480.0, width=500.0)

    learnButtonImage = tk.PhotoImage(file=d+"learn.png")
    learnButton = tk.Button(image=learnButtonImage, borderwidth=0, highlightthickness=0,
                            command=lambda: pagesViewModel.enterLearnMode(), relief="flat")

    practiceButtonImage = tk.PhotoImage(file=d+"practice.png")
    practiceButton = tk.Button(image=practiceButtonImage, borderwidth=0, highlightthickness=0,
                               command=lambda: pagesViewModel.enterTestMode(), relief="flat")
    browseButtonImage = tk.PhotoImage(file=d +"browse.png")
    browseButton = tk.Button(image=browseButtonImage, borderwidth=0, highlightthickness=0,
                             command=lambda: pagesViewModel.enterBrowseMode(), relief="flat")

    clearButtonImage = tk.PhotoImage(file=d+"clear.png")
    clearButton = tk.Button(image=clearButtonImage, borderwidth=0, highlightthickness=0,
                            command=lambda: pagesViewModel.clearCanvas(), relief="flat")

    checkButtonImage = tk.PhotoImage(file=d+"check.png")
    checkButton = tk.Button(image=checkButtonImage, borderwidth=0, highlightthickness=0,
                            command=lambda: pagesViewModel.checkButton(), relief="flat")

    previousButtonImage = tk.PhotoImage(file=d+"previous.png")
    previousButton = tk.Button(image=previousButtonImage, borderwidth=0, highlightthickness=0,
                               command=lambda: pagesViewModel.previousButton(), relief="flat")

    nextButtonImage = tk.PhotoImage(file=d+"next.png")
    nextButton = tk.Button(image=nextButtonImage, borderwidth=0, highlightthickness=0,
                           command=lambda: pagesViewModel.nextButton(), relief="flat")

    capturedCharacter = tk.Label(frame, bg="#256150", anchor="nw", text="Captured Sign:",
                                 font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    capturedCharacterData = tk.Label(frame, bg="#256150", anchor="nw", text="Data",
                                     font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

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
                              font=("Montserrat Bold", 30 * -1), wrap=tk.WORD)
    translationData.configure(state='normal')

    scrollbar = ttk.Scrollbar(window, orient='vertical', command=translationData.yview)

    translationData['yscrollcommand'] = scrollbar.set

    currentListOfSigns = tk.Label(frame, bg="#256150", anchor="nw", text="Current List Of Signs:",
                                  font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")

    currentListOfSignsData = tk.Text(window, height=10, width=40, fg="white", bg="gray10",
                                     font=("Montserrat Bold", 30 * -1), wrap=tk.WORD)

    scrollbarList = ttk.Scrollbar(window, orient='vertical', command=currentListOfSignsData.yview)

    currentListOfSignsData['yscrollcommand'] = scrollbarList.set
    currentListOfSignsData.configure(state='normal')
    currentListOfSignsData.delete(1.0, tk.END)
    currentListOfSignsData.insert('end', "")
    currentListOfSignsData.configure(state='disabled')

    pagesViewModel.createList(pagesViewModel.alwaysOnWidgetList, title, learnButton, practiceButton, browseButton)
    pagesViewModel.createList(pagesViewModel.browseWidgetList, currentListOfSigns, currentListOfSignsData,
                              scrollbarList, addButton, CurrentHskLevel, CurrentHskLevelSpinbox, selectButton)

    pagesViewModel.createList(pagesViewModel.testWidgetList, canvas, clearButton, checkButton, previousButton,
                              nextButton,capturedCharacter, capturedCharacterData, translation, translationData, scrollbar,
                              printResultsButton, checkedSignInformation)

    pagesViewModel.createList(pagesViewModel.learnWidgetList, canvas, clearButton, checkButton, previousButton,
                              nextButton, capturedCharacter, capturedCharacterData, signHanzi, signHanziData,
                              numberOfStrokes, numberOfStrokesData, frequencyRank, frequencyRankData,
                              unicodeCodepoint, unicodeCodepointData, translation, translationData, scrollbar,
                              addButton, checkedSignInformation)

    pagesViewModel.initializeModes()
    pagesViewModel.placeAlwaysOnWidgets()
    pagesViewModel.enterBrowseMode()

    def handle_keypress(event):
        pagesViewModel.keyHandler(event)

    def handle_mouse(event):
        pagesViewModel.paintOnCanvas(event)

    window.bind('<Key>', handle_keypress)
    canvas.bind("<B1-Motion>", handle_mouse)
    window.mainloop()


if __name__ == "__main__":
    drawUI()
