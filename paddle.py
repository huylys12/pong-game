from turtle import Turtle

START_POSITIONS_X = [-330, 330]
START_POSITIONS_Y = [-40, -20, 0, 20, 40]


class Paddle:
    def __init__(self, side):
        self.segments = []
        if side == 'left':
            self.xcor = START_POSITIONS_X[0]
        else:
            self.xcor = START_POSITIONS_X[1]
        self.create_paddle()

    def create_paddle(self):
        for pos_y in START_POSITIONS_Y:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setheading(90)
            new_segment.speed("fastest")
            new_segment.goto(self.xcor, pos_y)
            self.segments.append(new_segment)

    def up(self):
        if self.segments[-1].pos()[1] >= 235:
            return
        for index in range(len(self.segments)):
            self.segments[index].forward(20)

    def down(self):
        if self.segments[0].pos()[1] <= -235:
            return
        for index in range(len(self.segments)):
            self.segments[index].backward(20)
