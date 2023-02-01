import turtle

import colorgram
import random
from turtle import Turtle,Screen


tim = Turtle()
turtle.colormode(255)
colors = colorgram.extract("images.jpg",30)
# print(colors)
# tim.color(random_color)
# print(colors[0].rgb)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(250)
tim.setheading(0)

def forward(angle,n):
    for i in range(6):
        random_color = random.choice(colors).rgb
        tim.dot(20,random_color)
        tim.penup()
        tim.forward(50)
        tim.dot(20,random_color)
    tim.setheading(angle)
    tim.forward(50)
    if n % 2 != 0:
        tim.setheading(angle*2)
    else:
        tim.setheading(0)

n = 1

while n < 6:
    forward(90,n)
    n +=1



screen = Screen()
screen.exitonclick()