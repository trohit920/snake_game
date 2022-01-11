from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Models snake in the game."""
    def __init__(self):
        self.segment = []
        self.snake_body()
        self.head = self.segment[0]

    def snake_body(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.segment.append(body)

    def extend(self):
        # Extend snake by 1 block when food is eaten
        self.add_segment(self.segment[-1].position())

    def move(self):
        for num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[num - 1].xcor()
            new_y = self.segment[num - 1].ycor()
            self.segment[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.snake_body()
        self.head = self.segment[0]

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.left(UP)

    def left(self):
        self.head.setheading(LEFT)
        if self.head.heading() != RIGHT:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
