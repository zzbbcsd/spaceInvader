from main_craft import Craft
from invader import Invader
from scoreboard import Scoreboard
from turtle import Screen, Turtle
from beam import Beam

def shoot_beam():
    beam = Beam()
    beam.goto((craft.xcor(),craft.ycor()))
    beams.append(beam)

screen = Screen()
screen.bgcolor("black")
screen.bgpic('3500.png')
screen.setup(width=900, height=800)
screen.title("Welcome to Space Invader (Atomic Bomb Ver. XD)")
screen.tracer(0)

invaders = []
invader_x_coordinates =[-120,-80,-40,0,40,80,120]
beams=[]
for i in invader_x_coordinates:
    new_invader_1 = Invader((i,300))
    invaders.append(new_invader_1)
    new_invader_2 = Invader((i,340))
    invaders.append(new_invader_2)
    new_invader_3 = Invader((i,260))
    invaders.append(new_invader_3)

scoreboard = Scoreboard()
craft = Craft()

screen.listen()
screen.onkey(craft.go_left, "Left")
screen.onkey(craft.go_right, "Right")
screen.onkey(shoot_beam, "space")

game_is_on = True


while game_is_on:
    screen.update()
    for i in invaders:
        i.move()
        if i.ycor()< -320:
            game_is_on= False
            scoreboard.game_over()
        for beam in beams:
            beam.move()
            if i.distance(beam)<50:
                i.hideturtle()
                invaders.remove(i)
        if len(invaders)<=0:
            scoreboard.you_win()






screen.exitonclick()