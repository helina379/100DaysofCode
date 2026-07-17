# import colorgram
from turtle import Turtle, Screen
import random
#this is how i extracted the colours from a sample hirst spot painting :)
# colors_list = []
# colors = colorgram.extract('image.jpg', 25)
#
# # print(colors[0])
# for color in colors:
#     colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(colors_list)

final_color_list = [(199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 104, 56), (5, 57, 83), (222, 223, 226), (200, 216, 204), (108, 67, 85), (39, 36, 35), (86, 142, 59), (20, 122, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (209, 200, 115), (179, 174, 177), (151, 176, 165), (93, 142, 156), (28, 80, 59)]


screen = Screen()
coco = Turtle()

coco.speed("fastest")
screen.colormode(255)
for _ in range(10):
    coco.setpos(0, -(_ * 50))
    for i in range(10):
        coco.color(random.choice(final_color_list))
        coco.begin_fill()
        coco.circle(10)
        coco.end_fill()
        coco.color((255, 255, 255))
        coco.forward(50)





# print(random.choice(final_color_list))

screen = Screen()
screen.exitonclick()