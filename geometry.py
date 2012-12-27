#! /usr/bin/env python2
#
# testing on simple algebra and area formulae for rectangles.
# use the basic turtle graphics!
# as well as the ubiquitous Tkinter of course.

import Tkinter
import turtle
from random import randint

top = Tkinter.Tk()

def rect(x,y,width,height, donatello):
    donatello.pu()
    donatello.goto(x,y)
    donatello.seth(0)
    donatello.pd()

    for i in range(2):
        donatello.forward(width)
        donatello.left(90)
        donatello.forward(height)
        donatello.left(90)

def nextQn():
    Turtle1.reset()
    Turtle1.speed('normal')
    Turtle2.reset()
    Turtle2.hideturtle()

    if(randint(1,2)==1):
        width,height = AskHeight()
    else:
        width,height = AskWidthAndHeight()
    w.set(width)
    h.set(height)

    C.postscript(file="testgeom.ps")
    return w,h

def AskHeight():
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

    return width,height

def AskWidthAndHeight():
    width = randint(20,50)
    height = randint(5,width)
    scale = min(400/width, 300/width)

    xs = -width/2*scale
    ys = 100

    rect(xs, ys, width*scale, height*scale, Turtle1)

    Turtle1.pu()

    Turtle1.goto(xs+width/4*scale, ys+height*scale)
    Turtle1.write("width = ?", font=("Arial", 14, "normal"))

    Turtle1.goto(xs+width/4*scale, ys+height/2*scale)
    Turtle1.write("area = " + str(width*height), font=("Arial", 14, "normal"))

    Turtle1.goto(xs+(width+2)*scale, ys+height/2*scale)
    Turtle1.write("height = ?", font=("Arial", 14, "normal"))
    Turtle1.hideturtle()

    txtCursorX = -200
    txtCursorY = 60
    Turtle1.goto(txtCursorX, txtCursorY)
    Turtle1.write("Total Perimeter = " + str(2*(width+height)), font=("Arial", 14, "normal"))
    Turtle1.seth(270)
    Turtle1.pu()
    Turtle1.forward(25)
    Turtle1.write("Ben ... what's the width and height?",font=("Arial", 14, "normal"))

    Turtle1.forward(25)
    Turtle1.write("You know the area and the perimeter already.",font=("Arial", 14, "normal"))
    w.set(width)
    h.set(height)

#    print w.get(), h.get()
    return width,height

def showAns():
    Turtle2.pu()
    Turtle2.goto(-200,-200)
    Turtle2.write("width = " + str(w.get()), font=("Arial", 14, "normal"))
    Turtle2.seth(270)
    Turtle2.forward(25)
    Turtle2.write("height = " + str(h.get()), font=("Arial", 14, "normal"))

C = Tkinter.Canvas(top, width = 800, height = 800)
top.title("Geometry Quiz")
C.pack()

ts= turtle.TurtleScreen(C)

Turtle1 = turtle.RawTurtle(ts)
Turtle2 = turtle.RawTurtle(ts)
Turtle2.hideturtle()

Turtle1.speed('fast')

quitButton = Tkinter.Button(top, text="Quit", command=top.quit)
quitButton.place(x=50,y=450)

nextButton = Tkinter.Button(top, text="Next", command=nextQn)
nextButton.place(x=130,y=450)

w=Tkinter.IntVar()
h=Tkinter.IntVar()

showButton = Tkinter.Button(top, text="Show Answer", command=showAns)
showButton.place(x=220,y=450)

width, height = AskWidthAndHeight()
w.set(width)
h.set(height)

ts.bgcolor("white")

top.mainloop()



