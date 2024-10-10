import random
import turtle
from turtle import Turtle,Screen
import colorgram

# colors = colorgram.extract('image.jpg', 6)      #exctracting the list of colors from cologram
# rgb_color=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_rgb=(r,g,b)
#     rgb_color.append(tuple_rgb)
# print(rgb_color)




my_turtle=Turtle()
turtle.colormode(255)




color_list=[(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56)]
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.setheading(225)
my_turtle.forward(250)
my_turtle.setheading(0)
num_of_dots=100
for dots in range(1,num_of_dots+1):
    my_turtle.dot(20,random.choice(color_list))

    my_turtle.forward(50)
    if dots % 10==0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


screen=Screen()
screen.exitonclick()
















