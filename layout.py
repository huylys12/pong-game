from turtle import Turtle


class Outline:
    def __init__(self) -> None:
        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.penup()
        self.drawer.color("white")
        self.create_outline()
        self.create_middle_line()
        
    def create_outline(self):
        self.drawer.goto(-350, -250)
        self.drawer.pendown()
        for _ in range(2):
            self.drawer.forward(700)
            self.drawer.left(90)
            self.drawer.forward(500)
            self.drawer.left(90)
        

    def create_middle_line(self):
        self.drawer.penup()
        self.drawer.goto(0,-250)
        self.drawer.setheading(90)
        while self.drawer.ycor() < 250:
            self.drawer.pendown()
            self.drawer.forward(10)
            self.drawer.penup()
            self.drawer.forward(10)




        
