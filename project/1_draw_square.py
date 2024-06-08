import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Square")
screen.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(4)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        drawer.forward(size)
        drawer.right(90)

# Draw a square of size 100
draw_square(200)

# Hide the turtle and display the result
drawer.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
