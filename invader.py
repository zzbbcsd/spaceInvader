import turtle
from turtle import Turtle

class Invader(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.goto(position)
        self.x_move = 8
        self.y_move = -50

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor())
        if self.xcor() > 430 or self.xcor() < -430:
            self.x_move *= -1
            self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)


