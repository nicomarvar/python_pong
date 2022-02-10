# Import 
import turtle #Package
import winsound

# Create and setup window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=900, height=600)
# Tracer does: Stops window from updating automatically
window.tracer(0)

# Scores
score_left = 0
score_right = 0

#Middle line
middleLine = turtle.Turtle()
middleLine.speed(0)
middleLine.shape("square")
middleLine.color("white")
middleLine.shapesize(stretch_wid=45, stretch_len=0.1)

# Paddle A
paddle_a = turtle.Turtle()
# Speed sets the speed of animation 0 being the fastest
paddle_a.speed(0)
# Square is built in shape
paddle_a.shape("square")
paddle_a.color("white")# default size 20px x 20px
paddle_a.shapesize(stretch_wid=6, stretch_len=1)# stretchs multiply by default size 
# When using turtle moving objects leave a trail(writing). Pen up gets rid of that
paddle_a.penup()
# Goto is the initial position on the window at coordinates (>0,0^) being the center
paddle_a.goto(-425, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(425, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5 #Marks how many pixels at the time the ball moves

#Pen for scores
scoreLeft = turtle.Turtle()
scoreLeft.speed(0)
scoreLeft.color("gray")
scoreLeft.penup()
scoreLeft.hideturtle()#Hide the pen
scoreLeft.goto(-380, 270)
scoreLeft.write("Score: {}".format(score_left), align="center", font=("Courier", 18, "bold"))

scoreRight = turtle.Turtle()
scoreRight.speed(0)
scoreRight.color("gray")
scoreRight.penup()
scoreRight.hideturtle()#Hide the pen
scoreRight.goto(378, -290)
scoreRight.write("Score: {}".format(score_right), align="center", font=("Courier", 18, "bold"))


# Functions
def paddle_a_up():# functions needs to be DEFined
    # getting initial position
    if paddle_a.ycor() < 240:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > -240:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() < 240:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


# Keyboard binding(event)
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    window.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        scoreLeft.clear()
        scoreLeft.write("Score: {}".format(score_left), align="center", font=("Courier", 18, "bold"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        scoreRight.clear()
        scoreRight.write("Score: {}".format(score_left), align="center", font=("Courier", 18, "bold"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # Paddle bounce
    if (ball.xcor() > 405 and ball.xcor() < 415) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(405)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -405 and ball.xcor() > -415) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-405)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)