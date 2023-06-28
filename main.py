import turtle as t
from bricks import Bricks

STARTING_POSITION = (0, -250)
screen = t.Screen()
screen.setup(width=1000, height=600)
screen.title("Atari Breakout")
screen.bgcolor("black")
# screen.tracer(0)

paddle = t.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(STARTING_POSITION)

brick = Bricks()

screen.exitonclick()
