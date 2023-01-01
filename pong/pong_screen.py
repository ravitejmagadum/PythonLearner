from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import math
import time
from scoreboard import Scoreboard


WIDTH = 800
HEIGHT = 600

ball = Ball()
screen = Screen()
score = Scoreboard()

r_paddle = Paddle(380, 0)
l_paddle = Paddle(-388, 0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")

# max_distance = math.sqrt((WIDTH/2)**2+(HEIGHT/2**2)) + 20

while True:
    ball.move()

    if ball.ycor() < -(HEIGHT / 2)+20 or ball.ycor() > (HEIGHT / 2)-20:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320: #== l_paddle.ycor() or ball.pos() == r_paddle.pos():
        ball.jump()


    if ball.xcor() < -(WIDTH/2):
        ball.reset()
        score.r_p()
    elif ball.xcor() > (WIDTH/2):
        ball.reset()
        score.l_p()
    else:
        pass

screen.exitonclick()
