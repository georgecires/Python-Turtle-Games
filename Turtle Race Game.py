from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")
colors=['red','orange','yellow','green','purple']
y_position=[-100,-60,-20,20,60]
speed=[]

for turtle in range(0,5):
    tim=Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle])
    tim.color(colors[turtle])
    speed.append(tim)

if user_bet:
    is_race_on=True


while is_race_on:
    for turtle in speed:
        if turtle.xcor()>230:
            winning=turtle.pencolor()
            if user_bet==winning:
                print(f'Ai castigat,testoasa{winning} a fost mai rapida')
                is_race_on=False
            else:
                print(f'Ai pierdut boss.Testoasa castigatoare este {winning}')
                is_race_on=False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)







screen.exitonclick()
