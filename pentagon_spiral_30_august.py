import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
pentagon_spiral = turtle.Turtle()
pentagon_spiral.speed(0)
pentagon_spiral.color("orange")

# Function to draw a pentagon
def draw_pentagon(length):
    for _ in range(5):
        pentagon_spiral.forward(length)
        pentagon_spiral.right(72)

# Draw a spiral of pentagons
for i in range(30):
    draw_pentagon(i * 10)
    pentagon_spiral.right(10)

turtle.done()
