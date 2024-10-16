from turtle import Turtle,Screen
POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.all_segments=[]
        self.create_snake()
        self.head=self.all_segments[0]



    def create_snake(self):
        for seg_pos in POSITION:
            self.add_seg(seg_pos)


    def add_seg(self,seg_pos):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(seg_pos)
        self.all_segments.append(new_segment)

    def extend(self):
        self.add_seg(self.all_segments[-1].position())

    def reset(self):
        for seg in self.all_segments:
            seg.goto(100,1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]




    def snake_move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
    def Right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)
    def Left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)






