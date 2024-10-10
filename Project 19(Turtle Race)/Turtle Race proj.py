from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
race_is_on=False
user_choice=screen.textinput(title="who will win the race?",prompt="choose which color will win the race ")


color_list=["red","orange","blue","yellow","green","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle])
    all_turtles.append(new_turtle)


if user_choice:
    race_is_on=True
while race_is_on:

    for turt in all_turtles:

        random_distance =random.randint(0,10)
        turt.forward(random_distance)
        if turt.xcor()>230:
            race_is_on=False
            wining_color=turt.pencolor()
            if user_choice==wining_color:
                print(f" the wining color is {wining_color} ,you won  ")
            else:
                print(f" the wining color is {wining_color} ,you lost ")



















screen.exitonclick()