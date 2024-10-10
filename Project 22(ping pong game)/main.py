from turtle import Screen, Turtle
from padels import Paddle
from ball import Ball
import time
from scoreboard import Score


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
#crating the padels
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()
score=Score()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh_ball()
    #bounce with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #bounce with the paddel
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


    #the r padel miss
    if ball.xcor()>380:
        ball.reset_position()
        score.left_score()


    #the l paddel miss
    if ball.xcor()<-380:
        ball.reset_position()
        score.right_score()















screen.exitonclick()