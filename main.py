from tkinter import *
import time

x = 20
y = 20

snakelength = 4
boxes = []


root = Tk()
canvas = Canvas(root, width = 500, height = 500)

for i in range (1,snakelength):
    boxes.append(canvas.create_rectangle(30*i, 10, (30*(i+1)), 40, fill="red", outline="black"))
canvas.pack()


def go_right(event):
    global boxes, snakelength
    boxcoords = []
    for i in range (0,len(boxes)):
        boxcoords.append(canvas.coords(boxes[i]))

    if boxcoords[0][2] < 490:
        for i in reversed(range(0,len(boxes)-1)):
            canvas.coords(boxes[i+1],boxcoords[i])
            canvas.move(boxes[len(boxes)-1], x, 0)
            root.update()




root.bind("<Right>", go_right)
#root.bind("<Left>", go_left)
#root.bind("<Up>", go_up)
#root.bind("<Down>", go_down)


root.mainloop()




