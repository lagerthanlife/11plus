! /usr/bin/env python2
# Quiz generation
#

import numpy as np
from numpy.random import random_integers
from numpy import mean

from random import randint
from random import seed

import reportlab as rp
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.pdfgen.canvas import Canvas

np.random.seed(72)
seed(random_integers(1000000))

def setqn(seq, flag):
    if (flag==0):
        qn = random_integers(len(seq)-2)
        seq[qn] = "..."
        seq[qn+1] = "..."
    else:
        seq[len(seq)-2]= "..."
        seq[len(seq)-1]= "..."

    return seq


def seq1(L):
    a = random_integers(20)
    # d = random_integers(15) * (-1+np.random.binomial(1,0.5)*2)
    
    d = random_integers(15)
    seq = [str(a)]
    
    for i in range(1, L):
        seq.append(str(a + i * d))
        
    return seq

def seq2(L):
    A = seq1(L)
    B = seq1(L)
    
    seq = []
    for i in range(1,L):
        seq.append(A[i])
        seq.append(B[i])
    
    start = random_integers(len(seq)-L-1)
    
    return seq[start:(start+L)]

def seq3(L):
    a = random_integers(20)
    x = randint(2,5)
    seq = [str(a)]
    
    for i in range(1,L):
        seq.append(str(a*x**i))
        
    return seq


def lcm(numbers):
    return reduce(__lcm, numbers)

def __lcm(a, b):
    return ( a * b ) / __gcd(a, b)

def __gcd(a, b):
    a = int(a)
    b = int(b)
    while b:
        a,b = b,a%b
    return a

def beatsPerMinute():
    beats = randint(1,10)*10
    startHr = randint(0,11)
    startMin = randint(0,3)*15
    endHr = randint(startHr+1,23-startHr)
    endMin = randint(0,3)*15

    start = str(startHr).zfill(2) + ":" + str(startMin).zfill(2)
    end = str(endHr).zfill(2) + ":" + str(endMin).zfill(2)

    s1 = "A child's heart beats " + str(beats) + " times per minute."
    s2 = "How many times will it beat between " + start + " and " + end + " on the same day."

    return (s1,s2)

def cricket():
    Runs = []
    for i in range(10):
        Runs.append(randint(0,99))

    Runs.append(int(mean(Runs))*(1+len(Runs)) - sum(Runs))
    # Runs = [0, 25, 15, 40, 52, 15, 6, 8, 25, 35, 10]

    s1 = "The following table shows the runs that Anthony scored in a series."
    s2 = str(Runs)[1:-1]

    s3 = "a) What was the mean number of runs he scored per innings?"
    s4 = "b) What was the median number of runs he scored?"

    return s1, s2, s3, s4

def lcmtest():
    arr = np.arange(1,21)
    np.random.shuffle(arr)
    arr = arr[:4]

    s1 = "What is the smallest number that can be divided"
    s2 = "by the following numbers:"
    s3 = str(np.sort(arr))
    return s1, s2, s3

def MilkerBaker(page):
    milk_freq = randint(2, 6)
    baker_freq = milk_freq

    while (baker_freq == milk_freq):
        baker_freq = randint(2, 6)
    
    L = lcm([milk_freq, baker_freq])
    firstMeet = randint(1,7)
    page.textLine("The milkman and the baker first meet on "+str(firstMeet)+" January.")
    page.textLine("The milkman comes back to visit every " + str(milk_freq) + " days.")
    page.textLine("The baker comes back to visit every " + str(baker_freq) + " days.")
    page.textLine("")
    page.textLine("Q1. When do they next meet?")
    page.textLine("Q2. How many times do they meet this year? (Including "+str(firstMeet)+" January.)")


isth = ['1st', '2nd', '3rd']

for i in range(4,21):
    isth.append(str(i)+'th')

pdf = Canvas("test.pdf")
pdf.setFont("Courier", 12)

qns = pdf.beginText(inch*1, inch*10)

qns.textLine("[LOWEST COMMON MULTIPLES - MILKER/BAKER problems.]")
qns.textLine("")

for i in range(5):
    MilkerBaker(qns)
    qns.textLine("")

pdf.drawText(qns)
pdf.showPage()
pdf.save()
