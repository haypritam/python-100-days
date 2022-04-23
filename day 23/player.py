from turtle import Screen,Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.lt(90)
    def go_up(self):
        self.fd(MOVE_DISTANCE)
    def re(self):
        self.goto(0, -280)
