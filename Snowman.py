# Import Turtle module from Python Library

import turtle
from turtle import *

# Setting Turtle speed and screensize
speed(0.1)
window = turtle.Screen()
window.bgcolor("red")
turtle.hideturtle()
setup(800,600)

#Green background
penup()
goto(0,-320)
pendown()
color("green")
begin_fill()
circle(320)
end_fill()

#bottom of body
penup()
goto(0, -280)
pendown()
color("white")
begin_fill()
circle(110)
end_fill()

#middle of body
penup()
goto(0, -110)
pendown()
color("white")
begin_fill()
circle(90)
end_fill()

#head of body
penup()
goto(0, 20)
pendown()
color("white")
begin_fill()
circle(70)
end_fill()

# Function to draw 1 small black circle (to be called to make buttons later)
def black_circle():
    color("black")
    begin_fill()
    circle(10)
    end_fill()

# Draw eyes of the snowman
x= -20
for i in range(2):
    penup()
    goto(x, 110)
    pendown()
    black_circle()  #We call the function to make circles
    x = x + 40

# Draw buttons on the snowman (using function - black circle)
y = 0
for i in range(5):
    penup()
    goto(0, y)
    pendown()
    black_circle()  #We call the function to make circles
    y = y - 55

# Mouth of the snowman
penup()
goto(0, 70)
color("red")
begin_fill()
circle(17)
end_fill()

# Smaller mouth of the snowman
penup()
goto(0, 75)
color("white")
begin_fill()
circle(17)
end_fill()

# Create the right arm
penup()
goto(75,0)
pendown()
color("brown")
begin_fill()
left(40)
for i in range(2):
    forward(75)
    left(90)
    forward(7)
    left(90)
end_fill()

# Now create right finger 1
penup()
goto(115,38)
pendown()
color("brown")
begin_fill()
left(40)
for i in range(2):
    forward(25)
    left(90)
    forward(5)
    left(90)
end_fill()

# Now create right finger 2
goto(115,35)
begin_fill()
color("brown")
right(100)
for i in range(2):
    forward(25)
    left(90)
    forward(5)
    left(90)
end_fill()

# Now create left arm
penup()
goto(-130, 50)
pendown()
color("brown")
begin_fill()
right(10)
for i in range(2):
    forward(75)
    right(90)
    forward(7)
    right(90)
end_fill()

# Now create left finger 1
penup()
goto(-112, 58)
pendown()
color("brown")
begin_fill()
right(40)
for i in range(2):
    forward(25)
    right(90)
    forward(5)
    right(90)
end_fill()

# Now create left finger 2
penup()
goto(-108, 30)
pendown()
color("brown")
begin_fill()
right(100)
for i in range(2):
    forward(25)
    right(90)
    forward(5)
    right(90)
end_fill()


# Making the snowman hat
penup()
goto(50, 150)
pendown()
color("black")
begin_fill()
right(10)
forward(100)
right(90)
forward(10)
right(90)
forward(20)
left(90)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
left(90)
forward(20)
right(90)
end_fill()

# Nose of the snowman
penup()
goto(-6, 95)
pendown()
color("red")
begin_fill()
circle(5)
end_fill()


# Write Merry Christmas on Screen
penup()
goto(-135, 240)
pendown()
color("white")
write("Merry Christmas!", font=("Kunstler Script", 40, "bold"))
penup()
goto(-110, 210)
write("The Langley Academy", font=("Kunstler Script", 22,"normal", ))
pendown()

# Prevent turtle window from closing
turtle.done()