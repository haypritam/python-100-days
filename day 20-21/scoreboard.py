from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center",font=("Arial",20,"normal"))
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=("Arial",20,"normal"))
    
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def increase_Score(self):
        self.score+=1
        self.update_scoreboard()
