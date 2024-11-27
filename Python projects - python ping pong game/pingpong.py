import turtle

# Setup the screen
window = turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=800, height=600)
window.tracer(0)  # Set the delay for update
window.bgcolor(.1, .1, .1)  # Background color

# Setup game objects
# Ball
ball = turtle.Turtle()
ball.speed(0)  # Fastest speed
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(x=0, y=0)  # Initial position
ball.penup()  # Lift the pen up
ball_dx, ball_dy = 1, 1  # Initial velocity (speed of the ball)
# Center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=.1, stretch_wid=25)
center_line.penup()
center_line.goto(x=0, y=0)

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.color("blue")
player1.penup()
player1.goto(x=-350, y=0)

# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.color("red")
player2.penup()
player2.goto(x=350, y=0)

# Score text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0, y=260)
player1_score = 0
player2_score = 0
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 14, "normal"))  # Initial score
score.hideturtle()  # Hide the object because we don't want to see it

# Player Movement
players_speed = 20

def p1_move_up():  # Move up
    if player1.ycor() < 250:  # Prevent moving out of bounds
        player1.sety(player1.ycor() + players_speed)

def p1_move_down():  # Move down
    if player1.ycor() > -240:  # Prevent moving out of bounds
        player1.sety(player1.ycor() - players_speed)

def p2_move_up():  # Move up
    if player2.ycor() < 250:  # Prevent moving out of bounds
        player2.sety(player2.ycor() + players_speed)

def p2_move_down():  # Move down
    if player2.ycor() > -240:  # Prevent moving out of bounds
        player2.sety(player2.ycor() - players_speed)

# Keyboard bindings
window.listen()  # Listen for keyboard input
window.onkeypress(p1_move_up, "w")  # Move player 1 up
window.onkeypress(p1_move_down, "s")  # Move player 1 down
window.onkeypress(p2_move_up, "Up")  # Move player 2 up
window.onkeypress(p2_move_down, "Down")  # Move player 2 down

# Game loop
while True:
    window.update()
    
    # Ball movement
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Ball & borders collision
   