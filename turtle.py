import turtle as turtle
import random

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Verdana", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Verdana", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  # Star
  turtle.color("gold","gold")
  turtle.begin_fill()
  for side in range(0,5):

    turtle.forward(110)
    turtle.left(216)
  turtle.end_fill()
  turtle.penup()
  turtle.right(90)
  turtle.forward(125)
  turtle.color("black")
  turtle.write("Gold star for you!", font=("Verdana", 10, "normal"))
  turtle.forward(20)

def square():
  # Square
  turtle.color("blue","blue")
  turtle.begin_fill()
  for side in range(0,4):
    turtle.forward(80)
    turtle.left(90)
  turtle.end_fill()
  turtle.penup()
  turtle.right(90)
  turtle.forward(75)
  turtle.color("black")
  turtle.write("It's a blue square!", font=("Verdana", 10, "normal"))
  turtle.forward(20)

def hexagon():
  turtle.penup()
  #turtle.forward(30)
  turtle.right(60)
  turtle.pendown()
  turtle.color("purple","purple")
  turtle.begin_fill()
  # Hexagon
  for side in range(0,6):
    turtle.forward(80)
    turtle.left(60)
  turtle.end_fill()
  turtle.penup()
  #turtle.right(90)
  turtle.forward(100)
  turtle.color("black")
  turtle.write("It's a purple hexagon!", font=("Verdana", 10, "normal"))
  turtle.forward(20)

selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
