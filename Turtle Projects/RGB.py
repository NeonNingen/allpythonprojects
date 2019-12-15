import math
import turtle
import random


ts = turtle.Screen()
ts.bgcolor('black')
t1 = turtle.Turtle()
t1.speed(30)
t1.color('red')
rotate=int(360)
def drawUnique(t,size):
    for i in range(10):
        t.left(size)
        t.forward(5)
        t.right(size)
        size=size-4        
def drawUnique2(t,size,repeat):
  for i in range (repeat):
    drawUnique(t,size)
    t.right(360/repeat)
drawUnique2(t1,100,10)
t2 = turtle.Turtle()
t2.speed(0)
t2.color('green')
rotate=int(90)

def drawUnique(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawUnique2(t,size,repeat):
    for i in range (repeat):
        drawUnique(t,size)
        t.right(360/repeat)
drawUnique2(t2,100,10)
t3 = turtle.Turtle()
t3.speed(0)
t3.color('blue')
rotate=int(80)


