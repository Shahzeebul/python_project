import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Star")
screen.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(2)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        drawer.forward(size)
        drawer.right(144)  # Turning angle for a five-pointed star

# Draw a star with each side of length 100
draw_star(200)

# Hide the turtle and display the result
drawer.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
