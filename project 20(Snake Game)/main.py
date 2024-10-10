from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scordboard import Score
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#creating the snake and food
snake=Snake()
food=Food()
score=Score()
snake.create_snake()
screen.listen()
screen.onkey(fun=snake.Up,key="Up")
screen.onkey(fun=snake.Down,key="Down")
screen.onkey(fun=snake.Right,key="Right")
screen.onkey(fun=snake.Left,key="Left")

#moving the whole snake

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.score_inc()
        snake.extend()
    if snake.head.xcor()> 280 or snake.head.xcor() <-280 or snake.head.ycor()> 280 or snake.head.ycor() <-280:
        score.reset_game()
        snake.reset()
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset_game()
            snake.reset()
















screen.exitonclick()