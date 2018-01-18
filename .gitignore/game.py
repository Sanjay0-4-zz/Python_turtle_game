#!/bin/python3
from turtle import *
from random import randint
import time
speed(0)
penup()
goto(-140, 140)
for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
      penup()
      forward(10)
      pendown()
      forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('blue')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()
 
for turn in range(10):
    ada.right(36)

bob = Turtle()
bob.color('red')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 75)
bob.pendown()

for turn in range(72):
    bob.left(5)

ivy = Turtle()
ivy.shape('turtle')
ivy.color('black')

ivy.penup()
ivy.goto(-160, 50)
ivy.pendown()

for turn in range(60):
    ivy.right(6)

jim = Turtle()
jim.shape('turtle')
jim.color('yellow')

jim.penup()
jim.goto(-160, 25)
jim.pendown()

for turn in range(30):
    jim.left(12)

ele = Turtle()
ele.shape('turtle')
ele.color('green')

ele.penup()
ele.goto(-160, 5)
ele.pendown()

for turn in range(15):
    ele.right(24)

# turtle which keeps score
scorer = Turtle()
scorer.color("red")
scorer.speed(0)

scorer.penup()
scorer.goto(-80,70)
f=("Arial",25,"normal")

# turtle which keeps winner
winner = Turtle()
winner.color("black")
winner.speed(0)

winner.penup()
winner.goto(-80,70)
f=("Arial",15,"normal")

# count down to start
for countdown in ["READY","SET","GO"]:
    
    scorer.write(countdown,font=f)
time.sleep(1)
scorer.clear()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    ivy.forward(randint(1,5))
    jim.forward(randint(1,5))
    ele.forward(randint(1,5))
