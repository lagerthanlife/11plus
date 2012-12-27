#! /usr/bin/env python2
#
# testing on simple algebra and area formulae for rectangles.
# use the basic turtle graphics!
# as well as the ubiquitous Tkinter of course.

import Tkinter
import turtle
from random import randint

top = Tkinter.Tk()


def nextQn():
    Turtle1.reset()
    Turtle1.speed('normal')
    Turtle2.reset()
    Turtle2.hideturtle()

    return False

def AskQn():
    width = randint(20,50)
    height = randint(5,width)
    scale = min(400/width, 270/height)

    xs = -width/2*scale
    ys = 100

    rect(xs, ys, width*scale, height*scale, Turtle1)

    Turtle1.pu()

    Turtle1.goto(xs+width/4*scale, ys+height*scale)
    Turtle1.write("width = " + str(width), font=("Arial", 14, "normal"))

    Turtle1.goto(xs+width/4*scale, ys+height/2*scale)
    Turtle1.write("area = " + str(width*height), font=("Arial", 14, "normal"))

    Turtle1.goto(xs+(width+2)*scale, ys+height/2*scale)
    Turtle1.write("height = ?", font=("Arial", 14, "normal"))
    Turtle1.hideturtle()

    txtCursorX = -200
    txtCursorY = 60
    Turtle1.goto(txtCursorX, txtCursorY)
    Turtle1.write("Ben ... what is the height?", font=("Arial", 14, "normal"))

    w.set(width)
    h.set(height)

    return False

def showAns():
    return False


C = Tkinter.Canvas(top, width = 800, height = 800)
top.title("Template Quiz")
C.pack()

ts= turtle.TurtleScreen(C)

Turtle1 = turtle.RawTurtle(ts)
Turtle2 = turtle.RawTurtle(ts)
Turtle1.hideturtle()
Turtle2.hideturtle()

Turtle1.speed('fast')

quitButton = Tkinter.Button(top, text="Quit", command=top.quit)
quitButton.place(x=50,y=450)

nextButton = Tkinter.Button(top, text="Next", command=nextQn)
nextButton.place(x=130,y=450)

showButton = Tkinter.Button(top, text="Show Answer", command=showAns)
showButton.place(x=220,y=450)

# w=Tkinter.IntVar()
# h=Tkinter.IntVar()


width, height = AskWidthAndHeight()
# w.set(width)
# h.set(height)

ts.bgcolor("white")

top.mainloop()



