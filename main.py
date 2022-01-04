
import random
import tkinter as tk
from PIL import ImageGrab
import cv2
import hanzicharacter as hc
import imagerecognition as ir
import guiutil as gu
from tkinter import ttk
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main():

    recognition=ir.ImageRecognition()
    listOfCharacters = readLineByLine()
    window = tk.Tk()
    window.title('Project')
    window.geometry("1200x800")
    window.resizable(False, False)

    frame = tk.Frame(master=window, width=1200, height=800,bg="#256150")
    frame.pack()

    title = tk.Label(frame, bg="#256150", anchor="nw", text="Hanzi Learing App",
                     font=("Montserrat Bold", 64 * -1), fg="#FFFFFF")
    title.place(x=30, y=17)

    canvas = tk.Canvas(frame, bg="white",height=480.0,width=500.0)
    canvas.place(x=30.0, y=191.0)

    learnButtonImage = tk.PhotoImage(file=relative_to_assets("learn.png"))
    learnButton = tk.Button(image=learnButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: print("learn clicked"),relief="flat")
    learnButton.place(x=186.0,y=103.0,width=158.0,height=46.0)

    practiceButtonImage = tk.PhotoImage(file=relative_to_assets("practice.png"))
    practiceButton = tk.Button(image=practiceButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: print("practice clicked"),relief="flat")
    practiceButton.place(x=355.0,y=103.0,width=158.0,height=46.0)
    browseButtonImage = tk.PhotoImage(file=relative_to_assets("browse.png"))
    browseButton = tk.Button(image=browseButtonImage,borderwidth=0,highlightthickness=0,
                             command=lambda: print("browse clicked"),relief="flat")
    browseButton.place(x=524.0,y=104.0,width=158.0,height=46.0)

    clearButtonImage = tk.PhotoImage(file=relative_to_assets("clear.png"))
    clearButton = tk.Button(image=clearButtonImage,borderwidth=0,highlightthickness=0,
                            command=lambda: print("clear clicked"),relief="flat")
    clearButton.place(x=520.0,y=680.0,width=90.0,height=51.0)

    checkButtonImage = tk.PhotoImage(file=relative_to_assets("check.png"))
    checkButton = tk.Button(image=checkButtonImage,borderwidth=0,highlightthickness=0,
        command=lambda: print("check clicked"),relief="flat")
    checkButton.place(x=520.0,y=740.0,width=90.0,height=51.0)

    previousButtonImage = tk.PhotoImage(
        file=relative_to_assets("previous.png"))
    previousButton = tk.Button(image=previousButtonImage,borderwidth=0,highlightthickness=0,
                               command=lambda: print("previous clicked"),relief="flat")
    previousButton.place(x=819.0,y=708.0,width=158.0,height=46.0)

    nextButtonImage = tk.PhotoImage(file=relative_to_assets("next.png"))
    nextButton = tk.Button(image=nextButtonImage,borderwidth=0,highlightthickness=0,
                           command=lambda: print("next clicked"),relief="flat")
    nextButton.place(x=1006.0,y=708.0,width=158.0,height=46.0)

    capturedCharacter = tk.Label(frame, bg="#256150", anchor="nw", text="Captured Sign:",
                                 font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    capturedCharacter.place(x=30.0, y=700.0)

    capturedCharacterData = tk.Label(frame, bg="#256150", anchor="nw", text="Data",
                                     font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    capturedCharacterData.place(x=300.0, y=700.0)

    signHanzi = tk.Label(frame, bg="#256150", anchor="nw", text="Sign Hanzi:",
                         font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    signHanzi.place(x=761.0, y=156.0)

    signHanziData = tk.Label(frame, bg="#256150", anchor="nw", text="Data",
                             font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    signHanziData.place(x=979.0, y=156.0)

    numberOfStrokes = tk.Label(frame, bg="#256150", anchor="nw", text="Number of Strokes:",
                               font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    numberOfStrokes.place(x=630.0, y=201.0)
    numberOfStrokesData = tk.Label(frame, bg="#256150", anchor="nw", text="Num",
                                font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    numberOfStrokesData.place(x=979.0, y=201.0)

    frequencyRank = tk.Label(frame, bg="#256150", anchor="nw", text="Frequency Rank:",
                             font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    frequencyRank.place(x=670.0, y=246.0)

    frequencyRankData = tk.Label(frame, bg="#256150", anchor="nw", text="Rank",
                                 font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    frequencyRankData.place(x=979.0, y=246.0)

    unicodeCodepoint = tk.Label(frame, bg="#256150", anchor="nw", text="Unicode Codepoint:",
                                font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    unicodeCodepoint.place(x=630.0, y=291.0)

    unicodeCodepointData = tk.Label(frame, bg="#256150", anchor="nw", text="Cpoint",
                                    font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    unicodeCodepointData.place(x=979.0, y=291.0)

    translation = tk.Label(frame, bg="#256150", anchor="nw", text="Translation:",
                           font=("Montserrat Bold", 36 * -1), fg="#FFFFFF")
    translation.place(x=630.0, y=336.0)

    translationData = tk.Text(window, height=8, width=20, fg="white", bg="gray10",
                              font=("Montserrat Bold", 30 * -1),wrap=tk.WORD)
    translationData.configure(state='normal')
    translationData.place(x=630.0, y=381)

    scrollbar = ttk.Scrollbar(window,orient='vertical',command=translationData.yview)
    scrollbar.place(x=975, y=382, height=282)

    translationData['yscrollcommand'] = scrollbar.set




    def handle_keypress(event):
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


    def paint(event):
        gu.paint(event,canvas)

    def getRandomCharacter():
        hanzi = chr(int(listOfCharacters[random.randint(0, len(listOfCharacters) - 1)], base=16))
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


    window.bind('<Key>', handle_keypress)
    canvas.bind("<B1-Motion>", paint)
    window.mainloop()


def readLineByLine():
    f = open("TGSCC-Unicode.txt", 'r')
    lines = f.readlines()
    list = []
    for line in lines:
        list.append(line.partition("\t")[2].strip().replace("U+", ""))
    #print(chr(int(list[0], base=16)))
    return list


if __name__ == "__main__":
    main()




