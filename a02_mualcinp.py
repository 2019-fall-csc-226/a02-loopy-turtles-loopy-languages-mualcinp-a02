# Author: Phun Mualcin

# Username: mualcinp

# Assignment: A02: Exploring Turtles in Python

# Purpose: Draw something that brings a smile to your face using uses two turtles and one loop

import turtle

wn = turtle.Screen()

wn.bgcolor('black')


shape = turtle.Turtle()

turtle.color('blue')
turtle.pensize(20)
turtle.penup()




turtle.left(180)
turtle.forward(200)
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(250)
turtle.pendown()

turtle.left(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

aturtle = turtle.Turtle()
aturtle.pensize(20)
aturtle.shape('arrow')
aturtle.penup()
aturtle.setpos(125,200)
aturtle.pencolor('blue')
aturtle.pendown()


aturtle.right(90)
aturtle.forward(100)
aturtle.left(90)
aturtle.forward(100)
aturtle.left(90)
aturtle.forward(100)
aturtle.left(180)
aturtle.forward(200)

cturtle = turtle.Turtle()
cturtle.pensize(20)
cturtle.shape('arrow')
cturtle.penup()
cturtle.pencolor('blue')
cturtle.setpos(-50,250)
cturtle.pendown()

for i in range(3):
    cturtle.forward(300)
    cturtle.right(90)
    cturtle.forward(350)
    cturtle.right(90)
    cturtle.forward(200)










wn.exitonclick()