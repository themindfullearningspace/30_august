import turtle

snowflake = turtle.Turtle()
snowflake.speed(-10)
snowflake.color("cyan")

screen = turtle.Screen()
screen.bgcolor("black")

#Function to draw a Koch curve
def koch_curve(length, depth):
  if depth == 0:
    snowflake.forward(length)
  
  else:
    length /= 3.0
    koch_curve(length, depth - 1)
  
    snowflake.left(60)
    koch_curve(length, depth - 1)
    
    snowflake.right(120)
    koch_curve(length, depth - 1)
    
    snowflake.left(60)
    koch_curve(length, depth - 1)
    
# Function to draw a Koch snowflake
def koch_snowflake(length, depth):
  for _ in range(3):
    koch_curve(length, depth)
    snowflake.right(120)
    
koch_snowflake(200, 4)
turtle.done()