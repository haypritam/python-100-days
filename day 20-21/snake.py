from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)


    def add_segment(self,position):
        new_s=Turtle("square")
        new_s.color("white")
        new_s.pu()
        new_s.goto(position)
        self.segments.append(new_s)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].fd(MOVE_DISTANCE)
    
    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading()!=RIGHT:
            self.segments[0].setheading(LEFT)
