from PIL import Image
import pytesseract
import random
import tkinter as tk
from PIL import ImageGrab
import cv2
import hanzicharacter as hc
import imagerecognition as ir
def main():
    recognition=ir.ImageRecognition()
    listOfCharacters = readLineByLine()
    window = tk.Tk()
    window.title('Project')
    window.geometry("800x800")
    window.minsize(800, 800)
    window.maxsize(800, 800)
    frame = tk.Frame(master=window, width=700, height=700)
    frame.pack()
    canvas = tk.Canvas(frame, bg="white", height=400, width=400)
    canvas.place(x=50, y=50)
    label2 = tk.Label(master=frame, text="Sign", foreground="black", background="white")
    label2.config(font=('Bauhaus', 60))
    label = tk.Label(master=frame, text="Sign", foreground="black", background="white")
    label.config(font=('Bauhaus', 60))
    label.place(x=500, y=300)
    label2.place(x=500, y=50)
    canvas2 = tk.Canvas(frame, bg="red", height=50, width=50)
    canvas2.place(x=500, y=200)

    def handle_keypress(event):
        if (event.char == 'c'):
            canvas.create_rectangle(0, 0, 800, 800, fill='white')
        if (event.char == 'v'):
            recognition.getter(canvas,window,frame)
        if (event.char == 'k'):
            calculate()
        if (event.char == 'p'):
            recognition.paste()
        if (event.char == 'r'):
            getRandomCharacter()
        if (event.char == 'x'):
            canvas2.create_rectangle(0, 0, 60, 60, fill='red')
            recognition.getter(canvas,window,frame)
            recognition.paste()
            label["text"]=recognition.calculate()
        if (event.char == 'e'):
            canvas2.create_rectangle(0, 0, 60, 60, fill='red')
            if (recognition.checkIfMatch(label, label2)):
                canvas2.create_rectangle(0, 0, 60, 60, fill='cyan')

    def calculate():
        img = cv2.imread('out.png')
        text = pytesseract.image_to_string(img, lang='chi_sim')
        print(text)
        print(text[len(text) - 2])
        label["text"] = text[len(text) - 2]

    def paint(event):
        # Co-ordinates.
        x1, y1, x2, y2 = (event.x - 9), (event.y - 9), (event.x + 9), (event.y + 9)

        # Colour
        Colour = "black"

        # specify type of display
        canvas.create_oval(x1, y1, x2,
                           y2, fill=Colour)

    def getRandomCharacter():
        hanzi = chr(int(listOfCharacters[random.randint(0, len(listOfCharacters) - 1)], base=16))
        label2["text"] = hanzi
        # c = hc.Character(chr(int(hanzi, base=16)))
        c=hc.Character(hanzi)
        c.print()

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




