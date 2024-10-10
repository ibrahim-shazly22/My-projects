# import random
# from turtle import Turtle,Screen

# screen=Screen()
# screen.setup(width=600,height=400)
# race_is_on=False
# user_input=screen.textinput(title="start the race",prompt="press y to start the race")
#
# color_list=["red","green","orange","yellow","blue","purple"]
# y_directions=[-80,-50,-20,10,40,70]
# all_turtles=[]
#
# for turtle_index in range(0,6):
#     new_turtle=Turtle(shape="turtle")
#     new_turtle.penup()
#     new_turtle.goto(x=-280,y=y_directions[turtle_index])
#     new_turtle.color(color_list[turtle_index])
#     all_turtles.append(new_turtle)
#
# if user_input:
#     race_is_on=True
# while race_is_on:
#     prize=0
#     for turtle in all_turtles:
#         random_distance=random.randint(0,10)
#         turtle.forward(random_distance)
#         if turtle.xcor()>290:
#             prize+=1000
#             print(f"the {turtle.pencolor()} team won the first place , and won {prize}$ ")
#             race_is_on = False
#         elif turtle.xcor()>287 and turtle.xcor()<=290:
#             prize += 500
#             print(f"the {turtle.pencolor()} team won the second place , and won {prize}$ ")
#
#         elif turtle.xcor()>285 and turtle.xcor()<=287:
#             prize+=200
#             print(f"the {turtle.pencolor()} team won the third place , and won {prize}$ ")

import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")

# Create turtles
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtles = []

start_y = -100
for color in colors:
    t = turtle.Turtle()
    t.color(color)
    t.shape("turtle")
    t.penup()
    t.goto(-200, start_y)
    t.pendown()
    turtles.append(t)
    start_y += 40

# Draw the finish line
finish_line = 200
line = turtle.Turtle()
line.penup()
line.goto(finish_line, 150)
line.right(90)
line.pendown()
line.forward(300)
line.hideturtle()

# Race the turtles
places = []

while len(places) < 3:
    for t in turtles:
        if t.xcor() < finish_line:
            t.forward(random.randint(1, 10))
        if t.xcor() >= finish_line and t not in places:
            places.append(t)

# Declare the first three places
for i in range(3):
    print(f"Place {i + 1}: {places[i].color()[0]} turtle")

# Keep the window open
screen.mainloop()










# screen.exitonclick()







