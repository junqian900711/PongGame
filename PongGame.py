import turtle
import os
import winsound
# link as :   https://www.jianshu.com/p/c72073fef985
# https://www.jianshu.com/p/0628abdd38f4
# https://www.youtube.com/watch?v=C6jJg9Zan7w&t=626s
# https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg

wn = turtle.Screen()
wn.title("Pong by @Jun Qian")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
# default is 20pix * 20pix
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
print(paddle_a.ycor())

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1/10
ball.dy = -1/10

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0   Player B : 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)  same as below
        # winsound.MessageBeep(winsound.MB_OK)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # os.system("aplay bounce.wav&")
        winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
        # winsound.MessageBeep(winsound.MB_OK)

    if ball.xcor() > 390:
        # ball.setx(390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        # ball.setx(390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collision
    if (340 < ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        # os.system("afplay bounce.wav&")

    if (-350 < ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        # os.system("afplay bounce.wav&")

