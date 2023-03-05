from turtle import Turtle

class Name(Turtle):

    def __init__(self):
        super().__init__()

        self.color("black")
        self.hideturtle()
        self.penup()

    def goto_loc(self, x, y, answer_state):
        self.goto(x, y)
        self.write(f"{answer_state}", font=("Arial", 8, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("Arial", 16, "normal"))





