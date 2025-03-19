from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter the color:")

turtles =[]

colors = ["red", "blue", "green", "black", "purple"]

def finish():
    finish_line = Turtle()
    finish_line.width(10)
    finish_line.color("red")
    finish_line.penup()
    finish_line.goto(200,200)
    finish_line.pendown()
    finish_line.right(90)
    finish_line.forward(400)

finish()

for i in range (1,6):
    turtles.append(Turtle(shape="turtle"))

color_index = 0

for turtle in turtles:
    turtle.color(colors[color_index])
    color_index +=1

x = -240
y=-180
for turtle in turtles:
    turtle.penup()
    turtle.goto(x,y )
    y += 90

finish = False
while finish == False:
    for turtle in turtles:
        turtle.forward(random.randint(1,20))
        if turtle.xcor() >= 200:
            finish = True
            winner= turtle.pencolor()
            break

print(f"The winner is {winner}")
if user_bet == winner:
    print("Congrats you won!")
else:
    print("You lost!")
    
screen.exitonclick()

