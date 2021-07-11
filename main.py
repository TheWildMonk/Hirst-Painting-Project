import turtle as t
import random as rd
import colorgram as cg

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()

# Extracting colors from the image
colors = cg.extract("image.jpg", 10)

# Creating a list of tuples of rgb colors
rgb_colors = []
for each_rgb in range(len(colors)):
    color = []
    for each_color in range(3):
        color.append(colors[each_rgb].rgb[each_color])
    color_tuple = tuple(color)
    rgb_colors.append(color_tuple)

screen.exitonclick()
