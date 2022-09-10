from turtle import Turtle

FONT = ('Segue UI', 40, 'bold')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 200)
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.left_score}       {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, side):
        if side == 'left':
            self.left_score += 1
        if side == 'right':
            self.right_score += 1
        self.update()

    def game_over(self, winner):
        self.setpos(0, 0)
        self.write(f"{winner} win", align=ALIGNMENT, font=FONT)
