import turtle
from turtle import Turtle

class Craft(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        turtle.register_shape('craft.gif')
        self.shape("craft.gif")
        self.goto((0,-350))

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def shoot_beam(self):
        beam = Turtle()
        beam.color("white")
        beam.penup()
        beam.goto((0,0))
