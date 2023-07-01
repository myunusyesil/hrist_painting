# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirstpaint.jpg', 30)
#
# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

hirst_colors = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203),
                (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (38, 43, 67),
                (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165),
                (195, 79, 72), (161, 201, 219), (45, 74, 78), (79, 74, 44), (57, 126, 122), (219, 175, 187),
                (168, 206, 170), (220, 182, 169)]

print(hirst_colors)


def random_color():
    return random.choice(hirst_colors)


rafael = t.Turtle()
t.colormode(255)
rafael.width(20)
rafael.speed("fast")
rafael.penup()
position_y = -200
rafael.goto(-200, position_y)

for _ in range(10):
    for _ in range(10):
        rafael.color(random_color())
        rafael.dot(20)
        rafael.penup()
        rafael.forward(50)
    position_y += 50
    rafael.goto(-200, position_y)

my_screen = t.Screen()
my_screen.exitonclick()
