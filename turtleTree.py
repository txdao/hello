import turtle
import random
import math
import numpy as np

def tree(branchLen,t):
    if branchLen > 5:
        heading = (t.heading() + 180) % 360 -180
        x, y = t.pos()
        t.pensize((branchLen/10)**1.25)
        t.color(setcolor(branchLen))
        t.forward(branchLen)

        angle1 = random.randint(5, 35)
        angle2 = random.randint(5, 35)
        baseLength = int(65 - 30*downardness(heading) - 15*inwardness(x, heading))
        newLength = branchLen*random.randint(baseLength-10, max(baseLength + 10, 100))/100
        newLength2 = branchLen*random.randint(baseLength-10, max(baseLength + 10, 100))/100

        t.right(angle1)
        tree(newLength,t)
        t.left(angle1 + angle2)
        tree(newLength2,t)
        t.right(angle2)
        t.color(setcolor(branchLen))
        t.backward(branchLen)

def setcolor(branchLen):
    if branchLen < 20:
        return 'green'
    else:
        return 'brown'

def downardness(heading):
    return int(abs(heading) > 90)

def outwardness(x, heading):
    if heading != 0:
        return int(np.sign(x)*np.sign(heading) > 0)
    else:
        return 1

def inwardness(x, heading):
    return int(not outwardness(x, heading))

def main():
    t = turtle.Turtle()
    turtle.mode("logo")
    myWin = turtle.Screen()
    t.up()
    t.backward(400)
    t.down()
    t.color("green")
    t.speed(10)
    tree(100,t)
    myWin.exitonclick()

main()
