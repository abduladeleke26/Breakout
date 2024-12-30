from turtle import Turtle
import random
class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.goto(random.randint(-367,367),-197)
        self.direction = random.randint(0,1)


    def beforeMove(self):
        if self.direction == 1:
            self.x_move *= 1
        elif self.direction == 0:
            self.x_move *= -1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def shift(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

    def ybounce(self):
        self.y_move *= -1

    def xbounce(self):
        self.x_move *= -1
