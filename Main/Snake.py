# This is my first python legit project!
# This is just a demo!
# Do not judge me!

# This is it, part 1.

# Import all needed and uneeded modules

# This is all the screen modules

import turtle
import time
import random

# from PyQt5 import *


delay = 0.074

#End of modules

movement_value_snake = 20

# Setup The Screen
wn = turtle.Screen()
wn.title("My First Snake App With Python! By @elijahsears7 aka the_common_coder")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)


# The Snake!
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(40, 100)

# Key Binding Functions

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

# End of key binding methods.

# Key Bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")


# Segments of Snake Body

segments = []

def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + movement_value_snake)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - movement_value_snake)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + movement_value_snake)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - movement_value_snake)


def calc():
    num1 = input("Enter first number:")
    num2 = input("Enter seccond number:")

    anwser = float(num1) + float(num2)
    print(anwser)

while True:
    wn.update()

    # Check Colision With Borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)

        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    if head.distance(food) < 20:
        print("You Have Colided!")

        # Add The segments

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Move the food
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Move the segments bacwords
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

        # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            # Hide The segments
            segments.clear()


    time.sleep(delay)

wn.mainloop()
