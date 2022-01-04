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