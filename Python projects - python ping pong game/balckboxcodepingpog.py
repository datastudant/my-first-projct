import turtle

# Constants for configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_SIZE = 1
BALL_COLOR = "white"
CENTER_LINE_COLOR = "white"
PLAYER1_COLOR = "blue"
PLAYER2_COLOR = "red"  # Example color for Player 2
PLAYER_WIDTH = 5
PLAYER_HEIGHT = 1
CENTER_LINE_WIDTH = 0.1
CENTER_LINE_LENGTH = 25

def setup_turtle(t, shape, color, stretch_len, stretch_wid, x, y):
    """Utility function to set up a turtle."""
    t.shape(shape)
    t.color(color)
    t.shapesize(stretch_len=stretch_len, stretch_wid=stretch_wid)
    t.penup()
    t.goto(x, y)

def create_ball():
    ball = turtle.Turtle()
    setup_turtle(ball, "circle", BALL_COLOR, BALL_SIZE, BALL_SIZE, 0, 0)
    return ball

def create_center_line():
    center_line = turtle.Turtle()
    center_line.speed(0)
    setup_turtle(center_line, "square", CENTER_LINE_COLOR, CENTER_LINE_WIDTH, CENTER_LINE_LENGTH, 0, 0)
    return center_line

def create_player(x, color):
    player = turtle.Turtle()
    player.speed(0)
    setup_turtle(player, "square", color, PLAYER_HEIGHT, PLAYER_WIDTH, x, 0)
    return player

# Main setup
screen = turtle.Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Create game elements
ball = create_ball()
center_line = create_center_line()
player1 = create_player(-350, PLAYER1_COLOR)
player2 = create_player(350, PLAYER2_COLOR)  # Assuming Player 2 starts on the right

# Initial velocity for the ball
ball_dx, ball_dy = 1, 1  # Speed of the ball

# Main loop (if needed)
# while True:
#     # Game logic and movement code would go here
#     pass

# Keep the window open
turtle.done()