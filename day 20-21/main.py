from logging.handlers import WatchedFileHandler
from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake =Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.segments[0].distance(food)<15:
        scoreboard.increase_Score()
        food.refresh()
    



screen.exitonclick()