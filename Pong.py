import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Sapir")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)  # left_side

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)  # right_side

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("Red")
ball.penup()
ball.goto(0, 0)  # middle

# every time the ball moves 0.2 pixels
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("light Green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  player B: 0", align="center", font=("Courier", 20, "bold"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y > 240:
        y = 250
    else:
        y += 15
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y < -240:
        y = -250
    else:
        y -= 15
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y > 240:
        y = 250
    else:
        y += 15
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y < -240:
        y = -250
    else:
        y -= 15
    paddle_b.sety(y)


# keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball border checking
    # top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # bottom
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # right
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

    # left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

    # paddle and ball
    if 340 > ball.xcor() > 330 and paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if -330 > ball.xcor() > -340 and paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
