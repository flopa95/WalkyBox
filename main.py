from tkinter import *
import time

x = 1
y = 1

root = Tk()
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
box = canvas.create_rectangle(10, 10, 30, 30, fill="red", outline="black")

def draw_stuff():
    global x, y
    x = x
    y = y
    #box = canvas.create_rectangle(10, 10, 30, 30, fill="red", outline="black")
    #canvas.delete(box)
    canvas.move(box,x,0)
    root.update()
    root.after(20,draw_stuff)
    #print("x")


root.after(0,draw_stuff)
root.mainloop()




