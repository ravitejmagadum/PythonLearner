from turtle import Turtle, Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

screen = Screen()
screen.listen()
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()





    def create_snake(self, x=0, y=0):
        for i in range(3):
            timi = Turtle()
            timi.penup()
            timi.shape("square")
            timi.pencolor("white")
            timi.fillcolor("white")
            current = timi.setposition(x, y)
            x -= 20
            self.snake.append(timi)

    def move_forward(self):
        for turtle in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[turtle - 1].xcor()
            new_y = self.snake[turtle - 1].ycor()
            self.snake[turtle].goto(new_x, new_y)
        self.snake[0].forward(20)

    def turn_left(self):
        self.snake[0].left(90)


    def turn_right(self):
        self.snake[0].right(90)

    def n_c(self):
        pass