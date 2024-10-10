from turtle import Turtle,Screen


my_turtle=Turtle()
#challange num 1
def move_forward ():
    my_turtle.forward(20)
def move_Back ():
    my_turtle.back(20)
def right():
    my_turtle.right(30)
def left():
    my_turtle.left(30)
def clear():
    my_turtle.reset()

screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_Back)
screen.onkey(key="a",fun=right)
screen.onkey(key="d",fun=left)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
