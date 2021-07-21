import random
from random import randint
import string
import turtle

turtle.title("The Matrix")
turtle.bgcolor("black")
screen = turtle.Screen()



screen.setup(width = 1.0, height = 1.0)



coords = []

style = ('Arial', 30, 'italic')
while True:
    x = randint(-1000, 1000)
    if x in coords:
        continue
    if type(x/25) != float:
        continue
    coords.append(x)
    
    y = 480
    t = turtle.Turtle()
    t.speed("fastest")
    t.color('green')
    t.hideturtle()
    t.penup()
    while True:
        if y <= -530:
            break
        t.goto(x, y)
        y = y - 30
        t.write(random.choice(string.ascii_letters).upper(), font=style)
