import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @thm1d")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # 20x20 px
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # 20x20 px
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle") # 20x20 px
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.30
ball.dy = -0.30

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 230:
        y += 20
    elif y == 230:
        y += 10
    elif y == 240:
        y += 10
    else:
        y = y
    
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -230:
        y -= 20
    elif y == -230:
        y -= 10
    elif y == -240:
        y -= 10
    else:
        y = y
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 230:
        y += 20
    elif y == 230:
        y += 10
    elif y == 240:
        y += 10
    else:
        y = y
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -230:
        y -= 20
    elif y == -230:
        y -= 10
    elif y == -240:
        y -= 10
    else:
        y = y
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    # AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()