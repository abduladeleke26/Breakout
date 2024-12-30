from turtle import Screen, Turtle
from ball import Ball
from bar import Bar
from bricks import Bricks
import math

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("BREAKOUT")

scoree = Turtle()
scoree.hideturtle()
scoree.penup()
scoree.goto(-25,260)
scoree.color("white")
scoree.write("000",font=("typewriter",24,"normal"))


game = True
num = 0
ball = Ball()
ball.beforeMove()
bar = Bar()
bricks = Bricks()

specificBrick = None

screen.tracer(0)
bricks.place()
screen.tracer(1)


def follow():
    mouse_x,_ = screen.cv.winfo_pointerxy()
    screen_x = 43+mouse_x - screen.window_width()


    if(screen_x>300):
        bar.goto(290,bar.ycor())
    elif (screen_x<-300):
        bar.goto(-295, bar.ycor())
    else:
        bar.goto(screen_x, bar.ycor())
    screen.ontimer(follow,1)


def barCollision(bar, ball):
    x = 1
    while x <= 100:
        distance = math.sqrt((bar.xcor() - ball.xcor()) ** 2 + (bar.ycor() - ball.ycor()) ** 2)
        leftDistance = math.sqrt(((bar.xcor()-x) - ball.xcor()) ** 2 + (bar.ycor() - ball.ycor()) ** 2)
        rightDistance = math.sqrt(((bar.xcor()-(-x)) - ball.xcor()) ** 2 + (bar.ycor() - ball.ycor()) ** 2)
        x += 1
        if(distance<20):
            return distance<20
            x = 101
        elif(leftDistance<20):
            return leftDistance < 20
            x = 101
        elif(rightDistance<20):
            return rightDistance < 20
            x = 101

def brickCollision(brick,ball):
    global num
    x = 0
    while x <= 127:
        distance = math.sqrt((brick.getbrick(x).xcor() - ball.xcor()) ** 2 + ((brick.getbrick(x).ycor()) - ball.ycor()) ** 2)
        if(distance<20):
            brick.getbrick(x).hideturtle()
            screen.tracer(0)
            brick.deleteBrick(x)
            screen.tracer(1)
            num += score(x)
            return distance<20
        x += 1


def updateScore():
    global num
    scoree.clear()
    if num < 10:
        scoree.write(f"00{num}", font=("typewriter", 24, "normal"))
    elif num < 99:
        scoree.write(f"0{num}", font=("typewriter", 24, "normal"))
    elif num < 1000:
        scoree.write(f"{num}", font=("typewriter", 24, "normal"))

def score(x):
    if bricks.color(x) == "yellow":
        return 1
    elif bricks.color(x) == "green":
        return 2
    elif bricks.color(x) == "orange":
        return 5
    elif bricks.color(x) == "red":
        return 10






follow()
while game:

    screen.update()


    ball.move()

    bricks.score(0)

    if ball.ycor() > 287 or barCollision(bar,ball):
        ball.ybounce()

    elif  brickCollision(bricks,ball):
        ball.shift()
        ball.ybounce()
        updateScore()
        #specificBrick.hideturtle()

    elif ball.ycor() < -320:
        scoree.clear()
        scoree.color("red")
        scoree.goto(-75,260)
        scoree.write(f"GAME OVER", font=("typewriter", 24, "normal"))
        game = False


    if ball.xcor() > 387 or ball.xcor() < -387:
        ball.xbounce()

    if num == 576:
        scoree.clear()
        scoree.color("green")
        scoree.goto(-75, 260)
        scoree.write(f"YOU WIN!!", font=("typewriter", 24, "normal"))
        game = False







screen.exitonclick()