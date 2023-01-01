from turtle import Turtle, Screen
import random
import math


WIDTH = 800
HEIGHT = 600


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")

        #
        # angle = int(math.degrees(math.atan((HEIGHT/2-20)/(WIDTH/2-20))))
        # angles = [random.randint(-angle, angle), random.randint(190 - angle, 170 + angle)]
        # print(angles)
        # self.setheading(random.choice(angles))

        self.penup()
        self.angle()

    def angle(self):
        angle = random.randint(1, 359)
        self.setheading(angle)

    def move(self):
        self.forward(4)

    def bounce(self):
        ang = self.heading() * -1
        self.setheading(ang )

    def jump(self):
        ang = self.heading()
        if self.xcor() > 0 and self.ycor() > 0:
            self.setheading(180)
            self.setheading(180 - ang)
            self.fd(10)
        elif self.xcor() < 0 and self.ycor() > 0:
            self.setheading(0)
            self.setheading(180 - ang)
            self.fd(10)
        elif self.xcor() > 0 and self.ycor() < 0:
            self.setheading(0)
            self.setheading(90 - ang + 45)
            self.fd(10)
        elif self.xcor() < 0 and self.ycor() < 0:
            self.setheading(180)
            self.setheading(90 - ang + 45)
            self.fd(10)
        else:
            pass

    def reset(self):
        self.goto(0, 0)
        self.angle()