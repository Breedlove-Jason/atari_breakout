from turtle import Turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BRICK_WIDTH = 100
BRICK_HEIGHT = 50
BRICK_ROWS = 8
BRICK_COLS = 10
BRICK_START_X = -452
BRICK_START_Y = 290
BRICK_COLORS = ["#FF00FF", "#00FFFF", "#FFFF00", "#FF8C00", "#FF1493", "#00FF00", "#FF4500", "#00FF7F"]


class Bricks:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_single_brick(self, x, y, color):
        brick = Turtle()
        brick.color(color)
        brick.shape("square")
        # brick.shapesize(stretch_wid=1, stretch_len=5)
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(x, y)
        brick.stamp()

        border = Turtle()
        border.color("black")
        border.shape("square")
        border.shapesize(stretch_wid=1.1, stretch_len=4.1)
        border.penup()
        border.goto(x, y)
        border.stamp()

        stamp_id = brick.stamp()
        brick.clear()
        self.bricks.append({'x': x, 'y': y, 'color': color, 'stamp_id': stamp_id, 'border': border})

    def create_bricks(self):
        for row in range(BRICK_ROWS):
            y = BRICK_START_Y - row * BRICK_HEIGHT
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            for x in range(BRICK_START_X, BRICK_START_X + int(BRICK_COLS * BRICK_WIDTH), int(BRICK_WIDTH)):
                self.create_single_brick(x, y, color)
