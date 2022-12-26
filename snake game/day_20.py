from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
snake = Snake()
screen = Screen()
food = Food()
score = Scoreboard()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    h = snake.snake[0].heading()
    if h == 0 or h == 360:
        screen.onkey(snake.turn_left, "Up")
        screen.onkey(snake.turn_right, "Down")
        screen.onkey(snake.n_c, "Left")
    elif h == 90:
        screen.onkey(snake.turn_left, "Left")
        screen.onkey(snake.turn_right, "Right")
        screen.onkey(snake.n_c, "Down")
    elif h == 180:
        screen.onkey(snake.turn_left, "Down")
        screen.onkey(snake.turn_right, "Up")
        screen.onkey(snake.n_c, "Right")

    elif h == 270 or h == -90:
        screen.onkey(snake.turn_left, "Right")
        screen.onkey(snake.turn_right, "Left")
        screen.onkey(snake.n_c, "Up")
    else:
        snake.move_forward()


    if snake.snake[0].distance(food) < 15:
        food.refresh()
        score.update_score()
    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        game_on = False
        score.game_over()




# screen.mode("standard")
screen.exitonclick()