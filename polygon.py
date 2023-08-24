# import turtle
from turtle import *
# also import the random module - we'll need it
from random import *

# define the turtle shape
t=Turtle()
t.shape("turtle")
# create a list of colors
color = ["CornFlowerBlue","DarkOrchid","red","IndianRed","SeaGreen",
         "SlateGray","wheat","Black","LightSeaGreen","DeepSkyBlue",]

# the function takes the number of sides
def create_shape (num):
    # divides it by 360 to get the angle in between
    angle = 360/num
    # for EACH side
    for _ in range (num):
        # the color changes randomly
        t.color(choice(color))
        # moves forward 80 paces
        t.forward (80)
        # and moves left at the given angle
        t.left (angle)

# create a loop which goes the number of times as 3-10 sides
for sides in range (3,11):  
# this then puts the number of side in a function  
    create_shape (sides)

screen1=Screen()
screen1.exitonclick()