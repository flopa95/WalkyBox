from tkinter import *
import random
import time
import collections

x = 30
y = 30
randomx = 10
randomy = 10
candyexist = False
b = None


snakelength = 10
boxes = []
direction = "Right"


root = Tk()
canvas = Canvas(root, width = 500, height = 500)

for i in range (1,snakelength+1):
    boxes.append(canvas.create_rectangle(30*i, 10, (30*(i+1)), 40, fill="red", outline="black"))
canvas.pack()



def go_right(event):
    global boxes, snakelength, direction

    if direction != "Left":
        direction = "Right"
        boxcoords = []
        for i in range (0,len(boxes)):
            boxcoords.append(canvas.coords(boxes[i]))


        for i in reversed(range(1,len(boxes))):
            canvas.coords(boxes[i-1],boxcoords[i])

        canvas.move(boxes[len(boxes)-1], x, 0)

        check_game_over()
        check_eat()
        spawn_candy()
        root.update()



def go_down(event):
    global boxes, snakelength, direction
    if direction != "Up":
        direction = "Down"
        boxcoords = []
        for i in range (0,len(boxes)):
            boxcoords.append(canvas.coords(boxes[i]))


        for i in reversed(range(1,len(boxes))):
            canvas.coords(boxes[i-1],boxcoords[i])

        canvas.move(boxes[len(boxes)-1], 0, y)
        root.update()
        check_game_over()
        check_eat()
        spawn_candy()


def go_left(event):
    global boxes, snakelength, direction
    if direction != "Right":
        direction = "Left"
        boxcoords = []
        for i in range (0,len(boxes)):
            boxcoords.append(canvas.coords(boxes[i]))


        for i in reversed(range(1,len(boxes))):
            canvas.coords(boxes[i-1],boxcoords[i])

        canvas.move(boxes[len(boxes)-1], -x, 0)
        root.update()
        check_game_over()
        check_eat()
        spawn_candy()

def go_up(event):
    global boxes, snakelength, direction
    if direction != "Down":
        direction = "Up"
        boxcoords = []
        for i in range (0,len(boxes)):
            boxcoords.append(canvas.coords(boxes[i]))


        for i in reversed(range(1,len(boxes))):
            canvas.coords(boxes[i-1],boxcoords[i])

        canvas.move(boxes[len(boxes)-1], 0, -y)
        root.update()
        check_game_over()
        check_eat()
        spawn_candy()



def check_game_over():
    global boxes
    boxcoords = []
    #overlap = []
    for i in range(0, len(boxes)):
        boxcoords.append(canvas.coords(boxes[i]))

    overlap = set(map(tuple,boxcoords))
    if len(overlap) != len(boxcoords):
        canvas.delete(ALL)

def check_eat():
    global boxes, randomx, randomy,b, candyexist
    boxcoords = []
    #overlap = []
    for i in range(0, len(boxes)):
        boxcoords.append(canvas.coords(boxes[i]))

    overlap = canvas.find_overlapping(randomx, randomy, randomx+10, randomy+10)
    #print(len(overlap))

    if len(overlap)>1:
        canvas.delete(b)
        candyexist = False
        spawn_candy()
        shrink()






def spawn_candy():
    global randomx, randomy, candyexist, b

    if candyexist == False:
        randomx = get_random_coord(randomx)
        randomy = get_random_coord(randomy)
        #randomx = random.randint(20,480)
        #randomy = random.randint(20,480)

    overlap_candy = canvas.find_overlapping(randomx, randomy, randomx + 10, randomy + 10)
    #get_candy_coords(randomx,randomy)

    print(overlap_candy)

    if overlap_candy == () and candyexist == False:
        b = canvas.create_rectangle(randomx,randomy,randomx+10,randomy+10, fill = "blue")
        candyexist = True
        canvas.pack()
        root.update()


def get_random_coord(x):
    random.seed
    x = random.randint(20,480)
    return x


#test

def shrink():
    global boxes
    #print (len(boxes))
    #popper = int(len(boxes))-1
    canvas.delete(boxes[len(boxes)-1])
    boxes.pop(len(boxes)-1)







root.bind("<Right>", go_right)
root.bind("<Left>", go_left)
root.bind("<Up>", go_up)
root.bind("<Down>", go_down)


root.mainloop()




