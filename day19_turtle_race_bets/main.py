import random
import turtle
from turtle import Turtle, Screen



screen = Screen()

is_race_on = False


screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt = '''Choose your turtle(colour):
 These are the available colours: ['darkred', 'coral', 'darkorchid', 'deeppink', 'darkgoldenrod','lightseagreen']''')

colours = ['darkred', 'coral', 'darkorchid', 'deeppink', 'darkgoldenrod','lightseagreen']
y_coordinates = [-80, -50, -20, 10, 40, 70]
all_turtles = []


for i in range(6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.penup()
    new_turtle.goto(x = -230, y= y_coordinates[i])
    new_turtle.color(colours[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:



    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won!! The {winning_colour} turtle won!!")
            else:
                print(f"You've lost!! The {winning_colour} turtle won!!")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
