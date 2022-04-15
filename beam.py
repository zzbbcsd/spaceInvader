from turtle import Turtle

class Beam(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shapesize(3,3)
        self.y_move = 1
        self.tiltangle(90)
        self.color("red")
    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
