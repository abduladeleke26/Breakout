from turtle import Turtle

class Bricks(Turtle):

    def __init__(self):
        self.bricks = []
        self.x = 370
        self.y = 240


    def place(self):
        for y in range(0,2):
            for x in range(0,16):
                red = Turtle()
                red.penup()
                red.color("red")
                red.shape("square")
                red.shapesize(stretch_wid=1, stretch_len=2)
                red.goto(self.x,self.y)
                self.x -= 50
                self.bricks.append(red)
            self.y -= 33
            self.x = 370

        for y in range(0,2):
            for x in range(0,16):
                orange = Turtle()
                orange.penup()
                orange.color("orange")
                orange.shape("square")
                orange.shapesize(stretch_wid=1, stretch_len=2)
                orange.goto(self.x,self.y)
                self.x -= 50
                self.bricks.append(orange)
            self.y -= 33
            self.x = 370

        for y in range(0,2):
            for x in range(0,16):
                green = Turtle()
                green.penup()
                green.color("green")
                green.shape("square")
                green.shapesize(stretch_wid=1, stretch_len=2)
                green.goto(self.x,self.y)
                self.x -= 50
                self.bricks.append(green)
            self.y -= 33
            self.x = 370

        for y in range(0,2):
            for x in range(0,16):
                yellow = Turtle()
                yellow.penup()
                yellow.color("yellow")
                yellow.shape("square")
                yellow.shapesize(stretch_wid=1, stretch_len=2)
                yellow.goto(self.x,self.y)
                self.x -= 50
                self.bricks.append(yellow)
            self.y -= 33
            self.x = 370

    def getLen(self):
        return len(self.bricks)

    def getbrick(self,x):
        return self.bricks[x]

    def deleteBrick(self,x):
        self.bricks[x].goto(1000,1000)

    def score(self,x):
        num = 0
        brick = self.bricks[x]
        if brick.pencolor() == "yellow":
            print("yellow")
            num += 1
            return num
        #elif self.bricks[x].pencolor() == "green":
            #return 2
        #elif self.bricks[x].pencolor() == "orange":
            #return 5
        #elif self.bricks[x].pencolor() == "red":
           #return 10

    def color(self,x):
        brick = self.bricks[x]
        return brick.pencolor()
