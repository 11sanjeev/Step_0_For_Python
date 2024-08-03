"""Demonstration of for loop using turtle python library by drawing objects"""
import turtle
# for steps in range (8):
#     turtle.forward(100)
#     turtle.right(360/8)
# turtle.Screen().exitonclick()
side = int(input("Enter side of object:"))
for steps in range(side):
    turtle.forward(50)
    turtle.right(360/side)
    for steps in range (side):
        turtle.forward(25)
        turtle.right(360/side)
turtle.Screen().exitonclick()