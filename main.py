from PIL import Image
import pytesseract
import tkinter as tk
from PIL import ImageGrab
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def main():
    window=tk.Tk()
    window.title('Project')
    window.geometry("800x800")
    window.minsize(800,800)
    window.maxsize(800,800)
    frame = tk.Frame(master=window, width=700, height=700)
    frame.pack()
    canvas = tk.Canvas(frame,bg="white",height=400,width=400)
    canvas.place(x=50,y=50)
    label = tk.Label(master=frame, text="Sign", foreground="black", background="white")
    label.config(font=('Bauhaus', 60))
    label.place(x=500, y=50)
    def handle_keypress(event):
        if (event.char == 'c'):
            canvas.create_rectangle(0,0,800,800, fill='white')
        if (event.char == 'v'):
            getter(canvas)
        if (event.char == 'k'):
            calculate()
        if (event.char == 'p'):
            paste()
        if (event.char == 'x'):
            getter(canvas)
            paste()
            calculate()
    def calculate():
        img = cv2.imread('out.png')
        text=pytesseract.image_to_string(img, lang='chi_sim')
        print(text)
        print(text[len(text)-2])
        label["text"]=text[len(text)-2]
    def paint(event):
        # Co-ordinates.
        x1, y1, x2, y2 = (event.x - 7), (event.y - 7), (event.x + 7), (event.y + 7)

        # Colour
        Colour = "black"

        # specify type of display
        canvas.create_oval(x1, y1, x2,
                           y2, fill=Colour)
    def paste():
        img1=Image.open('first.png')
        img1 = img1.resize((100, 100))
        img2 = Image.open('second.png')
        img2 = img2.resize((100, 100))
        img3 = Image.open('third.png')
        img3 = img3.resize((100, 100))
        img=Image.open('image.png','r')
        img=img.resize((100,100))
        background = Image.new('RGBA', (1000,1000), (255, 255, 255, 255))
        background.paste(img1, (100, 500))
        background.paste(img2, (200, 500))
        background.paste(img3, (300, 500))
        background.paste(img, (400,500))
        background.save('out.png')

    def getter(widget):
        x = window.winfo_rootx() + frame.winfo_x()+ widget.winfo_x()
        y = window.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save('image.png')

    window.bind('<Key>', handle_keypress)
    canvas.bind("<B1-Motion>", paint)
    window.mainloop()

if __name__ == "__main__":
    main()