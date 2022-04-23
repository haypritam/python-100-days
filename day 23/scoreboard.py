from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("Black")
        self.pu()
        self.ht()
        self.updateScore()
    def updateScore(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Score:{self.score}", align="center",font=(FONT))
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=(FONT))

