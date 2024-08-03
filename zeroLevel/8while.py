"""Demonstration of while loop using turtle python library by drawing objects"""
# answer = '0'
# while answer != '4':
#     answer = input("What is 2+2")
# print ("yes 2+2 = 4")
# import turtle
# counter = 0 

# while counter < 4:
#     turtle.forward(100)
#     turtle.right(90)
#     cott =0
#     while cott < 4:
#         turtle.forward(50)
#         turtle.right(90)
#         cott+=1
#     counter+=1
import turtle
leng = 1
while leng != 0:
    color = input("Enter the colour of line ")
    length = int(input("Enter line length "))
    side = int (input('How many sides you want '))
    leng = length
    counter = 0
    while counter < side:
        turtle.color(color)
        turtle.forward(length)
        turtle.right(360/side)
        counter+=1

