import turtle as t
import random as rd
import colorgram as cg

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()

# Extracting colors from the image
colors = cg.extract("image.jpg", 10)

# Creating a list of tuples of rgb colors
color = []
for each_color in colors:
    r = each_color.rgb.r
    g = each_color.rgb.g
    b = each_color.rgb.b
    rgb_color = (r, g, b)
    color.append(rgb_color)

screen.exitonclick()
