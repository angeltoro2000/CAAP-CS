# Angel TOro
# Lab-4
# August 5
#Received help with the code from Andrea

# Imports the turtle graphics module
import turtle

# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")

# setting out box sizes to the n sq pixels per box
boxSize = 10

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)


# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


# Here is an example of how to draw a box using the box function
# Comment this out when you draw your own images
# box(boxSize)


# Challenge functions (2 bonus pts each)
# You need to make shapes with each
# def circle(intRadius):
# def triangle(intLength): #This can be an equilateral triangle
# def save_image(): # saves the screen to an image/vector file

# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the oen down and it draws as it moves
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()

# You will save your drawings as lists.
# This first list stores the color values
pallet_1 = ["#FFFFFF", "#FFFF00", "#000000", "#61380B", "#F4FA58"]
# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list
# Banana
pixels_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
pixels_1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 2, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 2, 4, 1, 2, 2, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 2, 4, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 2, 4, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 2, 4, 4, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 2, 4, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 2, 4, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 2, 4, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 2, 4, 1, 3, 2, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pixels_1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Mario
pallet_2 = ["#4B610B", "#FAFAFA", "#DF0101", "#FE9A2E"]
pixels_2 = [[1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]]
pixels_2.append([1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1])
pixels_2.append([1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 3, 0, 3, 1, 1, 1])
pixels_2.append([1, 1, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 1])
pixels_2.append([1, 1, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3])
pixels_2.append([1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 1])
pixels_2.append([1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1])
pixels_2.append([1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1])
pixels_2.append([1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1])
pixels_2.append([0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0])
pixels_2.append([3, 3, 3, 0, 2, 3, 2, 2, 2, 2, 3, 2, 0, 3, 3, 3])
pixels_2.append([3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3])
pixels_2.append([3, 3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 3, 3, 3])
pixels_2.append([1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1])
pixels_2.append([1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1])
pixels_2.append([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

# PacMan
pallet_3 = ["#FAFAFA", "#FFFF00", "#FE9A2E"]
pixels_3 = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0]]
pixels_3.append([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
pixels_3.append([0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0])
pixels_3.append([0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0])
pixels_3.append([0, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 2, 2, 0])
pixels_3.append([1, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 2, 2, 1])
pixels_3.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1])
pixels_3.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels_3.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels_3.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels_3.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels_3.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels_3.append([1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1])
pixels_3.append([1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1])

# Blue Monster
pallet_4 = ["#000000", "#0000FF"]
pixels_4 = [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]]
pixels_4.append([0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
pixels_4.append([0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0])
pixels_4.append([0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0])
pixels_4.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels_4.append([1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1])
pixels_4.append([1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1])
pixels_4.append([0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0])

# 3 Mushroom
pallet_5 = ["#ffffff", "#ff0000", "#000000"]
pixels_5 = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]
pixels_5.append([0, 0, 0, 1, 1, 2, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0])
pixels_5.append([0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0])
pixels_5.append([0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 0])
pixels_5.append([0, 1, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1, 0])
pixels_5.append([1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 1])
pixels_5.append([1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 1])
pixels_5.append([1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1])
pixels_5.append([1, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1])
pixels_5.append([1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 1])
pixels_5.append([1, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1])
pixels_5.append([0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0])
pixels_5.append([0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0])
pixels_5.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
pixels_5.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
pixels_5.append([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0])

# 4 Smiley Face
pallet_6 = ["#000000", "#FFFF00", "#F0F0F0", "#CD5C5C", "#9370db"]
pixels_6 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
pixels_6.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2])
pixels_6.append([2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 1, 1, 0, 2, 2, 2])
pixels_6.append([2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 1, 0, 2, 2])
pixels_6.append([2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 1, 0, 2, 2])
pixels_6.append([2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 0, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 2])
pixels_6.append([2, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 2])
pixels_6.append([2, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 2])
pixels_6.append([0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 0])
pixels_6.append([0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0])
pixels_6.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
pixels_6.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
pixels_6.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
pixels_6.append([2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2])
pixels_6.append([2, 0, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 0, 2])
pixels_6.append([2, 0, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 0, 2])
pixels_6.append([2, 2, 0, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 0, 2, 2])
pixels_6.append([2, 2, 0, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 0, 1, 1, 0, 2, 2])
pixels_6.append([2, 2, 2, 0, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 3, 0, 1, 1, 0, 2, 2, 2])
pixels_6.append([2, 2, 2, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 0, 1, 1, 1, 0, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 0, 1, 1, 1, 0, 0, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 0, 0, 0, 3, 4, 4, 4, 4, 0, 0, 0, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2])
pixels_6.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

pallet_7 = ["#ffffff", "#000000", "#0000FF", "#ffe0bd", "#ff0000"]
pixels_7 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
pixels_7.append([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])
pixels_7.append([1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0])
pixels_7.append([1, 0, 1, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 2, 0, 2, 0, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 3, 1, 1, 1, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0])
pixels_7.append([0, 1, 2, 2, 3, 3, 3, 3, 3, 2, 1, 4, 4, 4, 1, 0, 0, 0])
pixels_7.append([0, 1, 1, 2, 3, 3, 3, 3, 3, 1, 4, 0, 0, 0, 4, 1, 0, 0])
pixels_7.append([0, 0, 0, 1, 1, 1, 1, 1, 1, 4, 0, 4, 4, 4, 0, 4, 1, 0])
pixels_7.append([0, 0, 1, 2, 2, 2, 2, 1, 4, 0, 4, 2, 2, 2, 4, 0, 4, 1])
pixels_7.append([0, 1, 2, 1, 2, 2, 0, 1, 4, 0, 4, 2, 0, 2, 4, 0, 4, 1])
pixels_7.append([0, 1, 0, 1, 2, 2, 2, 1, 4, 0, 4, 2, 2, 2, 4, 0, 4, 1])
pixels_7.append([0, 1, 4, 1, 0, 4, 0, 4, 1, 4, 0, 4, 4, 4, 0, 4, 1, 0])
pixels_7.append([0, 0, 1, 1, 0, 4, 0, 4, 0, 1, 4, 0, 0, 0, 4, 1, 0, 0])
pixels_7.append([0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 4, 4, 4, 1, 0, 0, 0])
pixels_7.append([0, 0, 0, 1, 4, 4, 1, 1, 4, 4, 1, 1, 1, 1, 0, 0, 0, 0])
pixels_7.append([0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])

pallet_8 = ["#ffffff", "#000000", "#0000FF", "#ffe0bd"]
pixels_8 = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]]
pixels_8.append([0, 0, 1, 1, 2, 2, 2, 2, 1, 1, 0, 0])
pixels_8.append([0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0])
pixels_8.append([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1])
pixels_8.append([1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1])
pixels_8.append([1, 1, 2, 2, 1, 0, 3, 1, 2, 2, 1, 1])
pixels_8.append([1, 0, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1])
pixels_8.append([0, 1, 0, 0, 0, 1, 1, 3, 3, 3, 1, 0])
pixels_8.append([0, 1, 3, 0, 0, 0, 3, 3, 3, 3, 1, 0])
pixels_8.append([0, 0, 1, 1, 3, 3, 3, 3, 1, 1, 0, 0])
pixels_8.append([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0])



# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixel):
    for i in pixel:
        for j in i:
            myPen.color(pallet[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i) * boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)


# Should give the user a list of the possible drawing pieces you have and ask which one to draw
def main():
    print("This is a list of drawing pieces you can choose from: \n1. Banana\n2. Mario\n3. PacMan\n4. Monster\n5. Mushroom\n6. Smiley Face\n7. Captain America\n8. Pokeball")

    num = int(input("Which one would you like to draw?"))
    if num == 1:
        draw(pallet_1, pixels_1)
    elif num == 2:
        draw(pallet_2, pixels_2)
    elif num == 3:
        draw(pallet_3, pixels_3)
    elif num == 4:
        draw(pallet_4, pixels_4)
    elif num == 5:
        draw(pallet_5, pixels_5)
    elif num == 6:
        draw(pallet_6, pixels_6)
    elif num == 7:
        draw(pallet_7, pixels_7)
    elif num == 8:
        draw(pallet_8, pixels_8)
    else:
        print("Not an option, try again")

    # You need this to prevent the window from closing after drawing
    turtle.done()


main()