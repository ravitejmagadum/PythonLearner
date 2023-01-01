from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 6)
        self.penup()
        self.speed("fastest")


        self.goto(x, y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




