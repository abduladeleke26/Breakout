from turtle import Turtle

class Bar(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=10)
        self.setpos(x=0,y=-235)


