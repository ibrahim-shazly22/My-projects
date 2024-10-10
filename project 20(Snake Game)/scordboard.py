from turtle import Turtle
FONT=("Arial", 14, "normal")
ALIIGMENT="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highest_score=int(data.read())


        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()



    def update(self):
        self.clear()
        self.write(f"score is {self.score},Highest score is {self.highest_score}", align=ALIIGMENT, font=FONT)
    def score_inc(self):
       self.score+=1
       self.clear()
       self.update()

    def reset_game(self):
        if self.score>self.highest_score:
            self.highest_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score=0
        self.update()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="Game Over", align=ALIIGMENT, font=FONT)
