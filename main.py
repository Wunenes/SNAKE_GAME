from turtle import Screen
import snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake game")
screen.setup(width=500, height=500)
screen.tracer(0)

snake = snake.Snake()
food = Food()
scores = Score()

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Left", fun=snake.left)
game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scores.score_display(tot_score=score)
    if snake.segments[0].distance(food) < 15:
        food.recoup()
        snake.extend()
        score += 1

    if snake.segments[0].xcor() > 240 or snake.segments[0].ycor() > 240 or snake.segments[0].ycor() < -240 or \
            snake.segments[0].xcor() < -250:
        score = 0
        snake.reset()
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 5:
            game_is_on = False
            scores.game_over()
screen.exitonclick()
