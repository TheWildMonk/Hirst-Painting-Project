import turtle as t
import random as rd

color_list = [(241, 222, 86), (35, 98, 185), (86, 174, 218),
              (169, 67, 37), (217, 158, 84), (187, 16, 34), (173, 49, 85), (78, 108, 210), (225, 57, 103),
              (161, 163, 23), (166, 27, 17), (75, 176, 77), (232, 70, 44), (225, 123, 172), (125, 198, 117),
              (20, 55, 146), (59, 119, 64), (118, 226, 184), (71, 30, 43), (135, 216, 233), (238, 158, 217),
              (41, 172, 183), (29, 41, 84), (242, 175, 152), (162, 165, 235), (90, 30, 22)]


# Setting screen attributes
screen = t.Screen()
screen.canvwidth = 500
screen.canvheight = 500

# Resetting the turtle world coordinates
screen.reset()
screen.setworldcoordinates(-50, -50, 500, 500)

# Setting turtles attributes
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()


def reset_line_position():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.setx(0)
    tim.left(180)


# Function to create the art in a line
def create_art():
    for _ in range(10):
        tim.penup()
        tim.dot(20, rd.choice(color_list))
        if _ < 9:
            tim.forward(50)


# While loop to create the 10x10 art
end_of_canvas = 1
while end_of_canvas < 11:
    create_art()
    if end_of_canvas < 10:
        reset_line_position()
    end_of_canvas += 1

screen.exitonclick()
