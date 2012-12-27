#! /usr/bin/env python2
#
# testing on quantities and fractions.
# use the basic turtle graphics!
# as well as the ubiquitous Tkinter of course.

import Tkinter
import turtle
from random import randint

top = Tkinter.Tk()

market = {'melon(s)': 0.80, 'banana(s)':0.40, 'apple(s)':0.35}
mktweight = {'melon(s)': 2.40, 'banana(s)': 4.00, 'apple(s)': 2.80}
people = ['Mark', 'Ben', 'Curtis', 'Zoe', 'Heidi', 'Betty', 'Lucas']

def askQn():
    quantity = randint(5,15)
    fruit = market.keys()[randint(0,len(market)-1)]
    person = people[randint(0,len(people)-1)]

    qn = person + " has a market stall.\n"
    qn += person + " sells {fruit} for ${price:.2f} for each kilogram.".format(fruit = fruit, price = mktweight[fruit])

    cost = quantity * market[fruit]
#    qn = "I have " + str(quantity) + " " + fruit + "\n"
#    qn += "I paid ${0:.2f}".format(cost)

    C.itemconfig(txtbox, text = qn)

def nextQn():
    C.itemconfig(txtbox, text = "Hello Ben!")
    return False


def showAns():
    return False

C = Tkinter.Canvas(top, width = 800, height = 400)
top.title("Fruits Quiz")
C.pack()

ts= turtle.TurtleScreen(C)
ts.bgcolor("white")

Turtle1 = turtle.RawTurtle(ts)
Turtle2 = turtle.RawTurtle(ts)
Turtle1.hideturtle()
Turtle2.hideturtle()

Turtle1.speed('fast')

quitButton = Tkinter.Button(top, text="Quit", command=top.quit)
quitButton.place(x=50,y=300)

nextButton = Tkinter.Button(top, text="Next", command=nextQn)
nextButton.place(x=130,y=300)


fruit=Tkinter.IntVar()
quantity=Tkinter.IntVar()
cost=Tkinter.IntVar()
person=Tkinter.StringVar()

txtbox=Tkinter.IntVar()
txtbox=C.create_text(-380, -180, text = "11+ Question Master", anchor=Tkinter.NW)

showButton = Tkinter.Button(top, text="Show Answer", command=showAns)
showButton.place(x=220,y=300)

askQn()

top.mainloop()



