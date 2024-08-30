import turtle
import random

sierpinski = turtle.Turtle()
sierpinski.speed(-5)
sierpinski.color("white")

screeen = turtle.Screen()
screeen.bgcolor("black")

# Function to draw the Sierpinski triangle
def sierpinski_triangle(length, depth):
  if depth == 0:
    for _ in range(3):
      sierpinski.forward(length)
      sierpinski.left(120)
  
  else:
    for i in range(200):
      sierpinski.color(random.choice(["red", "blue", "green", "orange", "purple", "yellow"]))
      
      sierpinski_triangle(length / 2, depth - 1)
      
      sierpinski.forward(length / 2)
      sierpinski_triangle(length / 2, depth - 1)
      
      sierpinski.backward(length / 2)
      sierpinski.left(60)
      
      sierpinski.forward(length / 2)
      sierpinski.right(60)
      
      sierpinski_triangle(length / 2, depth)
      
      sierpinski.left(60)
      sierpinski.backward(length / 2)
      sierpinski.right(60)
    
sierpinski_triangle(500, 3)
turtle.done()