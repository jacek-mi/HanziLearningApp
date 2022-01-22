
import viewmodel.pages as pg
import tkinter as tk
from tkinter import ttk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def drawInteractiveUI():
    window = tk.Tk()
    window.title('Project')
    window.geometry("1200x800")
    window.resizable(False, False)
    frame = tk.Frame(master=window, width=1200, height=800,bg="#256150")
    frame.pack()

    pagesViewModel = pg.Pages(window,frame)

    addButtonImage = tk.PhotoImage(file=relative_to_assets("add.png"))
    addButton = tk.Button(image=addButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: pagesViewModel.addButton(),relief="flat")

    title = tk.Label(frame, bg="#256150", anchor="nw", text="Hanzi Learing App",
                     font=("Montserrat Bold", 64 * -1), fg="#FFFFFF")
    canvas = tk.Canvas(frame, bg="white",height=480.0,width=500.0)

    learnButtonImage = tk.PhotoImage(file=relative_to_assets("learn.png"))
    learnButton = tk.Button(image=learnButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: pagesViewModel.enterLearnMode(),relief="flat")

    practiceButtonImage = tk.PhotoImage(file=relative_to_assets("practice.png"))
    practiceButton = tk.Button(image=practiceButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: pagesViewModel.enterTestMode(),relief="flat")
    browseButtonImage = tk.PhotoImage(file=relative_to_assets("browse.png"))
    browseButton = tk.Button(image=browseButtonImage,borderwidth=0,highlightthickness=0,
                             command=lambda: pagesViewModel.enterBrowseMode(),relief="flat")

    clearButtonImage = tk.PhotoImage(file=relative_to_assets("clear.png"))
    clearButton = tk.Button(image=clearButtonImage,borderwidth=0,highlightthickness=0,
    command=lambda: pagesViewModel.clearCanvas() ,relief="flat")

    checkButtonImage = tk.PhotoImage(file=relative_to_assets("check.png"))
    checkButton = tk.Button(image=checkButtonImage,borderwidth=0,highlightthickness=0,
    command=lambda: pagesViewModel.checkButton(),relief="flat")

    previousButtonImage = tk.PhotoImage(
        file=relative_to_assets("previous.png"))
    previousButton = tk.Button(image=previousButtonImage,borderwidth=0,highlightthickness=0,
                               command=lambda: pagesViewModel.previousButton(),relief="flat")

    nextButtonImage = tk.PhotoImage(file=relative_to_assets("next.png"))
    nextButton = tk.Button(image=nextButtonImage,borderwidth=0,highlightthickness=0,
                           command=lambda: pagesViewModel.nextButton(),relief="flat")

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
    currentListOfSignsData.insert('end', "")
    currentListOfSignsData.configure(state='disabled')

    def handle_keypress(event):
        vm.keyhandler(event);
    def handle_mouse(event):
        pagesViewModel.paintOnCanvas(event)

    pagesViewModel.createList(pagesViewModel.alwaysOnWidgetList,title,learnButton,practiceButton,browseButton)
    pagesViewModel.createList(pagesViewModel.browseWidgetList, currentListOfSigns, currentListOfSignsData,
                     scrollbarList, addButton)

    pagesViewModel.createList(pagesViewModel.testWidgetList,canvas,clearButton,checkButton,previousButton,nextButton,
                     capturedCharacter,capturedCharacterData,translation,translationData,scrollbar)

    pagesViewModel.createList(pagesViewModel.learnWidgetList,canvas,clearButton,checkButton,previousButton,
                     nextButton,capturedCharacter,capturedCharacterData,signHanzi,signHanziData,
                     numberOfStrokes,numberOfStrokesData,frequencyRank,frequencyRankData,
                     unicodeCodepoint,unicodeCodepointData,translation,translationData,scrollbar,addButton)

    pagesViewModel.initializeModes()
    pagesViewModel.placeAlwaysOnWidgets()
    pagesViewModel.enterBrowseMode()
    window.bind('<Key>', handle_keypress)
    canvas.bind("<B1-Motion>", handle_mouse)
    window.mainloop()


if __name__ == "__main__":
    drawInteractiveUI()




