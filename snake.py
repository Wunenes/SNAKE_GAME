import turtle
SNAKE_STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.snake_attribute()

    def snake_attribute(self):
        for position in SNAKE_STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.snake_attribute()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def left(self):
        if self.segments[0].heading() == 0:
            pass
        else:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() == 180:
            pass
        else:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() == 270:
            pass
        else:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() == 90:
            pass
        else:
            self.segments[0].setheading(-90)
