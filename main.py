from tkinter import *
import time

x = 10
y = 10

root = Tk()
canvas = Canvas(root, width = 500, height = 500)
box = canvas.create_rectangle(10, 10, 30, 30, fill="red", outline="black")

canvas.pack()

def draw_stuff():
    global x, y
    x = x
    y = y
    #box = canvas.create_rectangle(10, 10, 30, 30, fill="red", outline="black")
    #canvas.delete(box)
    canvas.move(box,x,0)
    root.update()
    #root.after(20,draw_stuff)
    #print("x")



def go_right(event):
    coords = canvas.coords(box)
    if coords[2] < 500:
        canvas.move(box, x, 0)
        root.update()

def go_left(event):
    coords = canvas.coords(box)
    if coords[0] > 0:
        canvas.move(box, -x, 0)
        root.update()

def go_up(event):
    coords = canvas.coords(box)
    if coords[1] > 0:
        canvas.move(box, 0, -y)
        root.update()

def go_down(event):
    coords = canvas.coords(box)
    if coords[3] < 500:
        canvas.move(box, 0, y)
        root.update()



root.bind("<Right>", go_right)
root.bind("<Left>", go_left)
root.bind("<Up>", go_up)
root.bind("<Down>", go_down)

root.after(0,draw_stuff)
root.mainloop()




