import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Circle")
screen.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(4)

# Function to draw a circle
def draw_circle(radius):
    drawer.circle(radius)

# Draw a circle with a radius of 50
draw_circle(100)

# Hide the turtle and display the result
drawer.hideturtle()

# Keep the window open until clicked
screen.exitonclick()




# import turtle

# # Function to draw a circle
# def draw_circle(radius):
#     drawer.clear()
#     drawer.penup()
#     drawer.goto(0, -radius)
#     drawer.pendown()
#     drawer.circle(radius)
#     drawer.penup()
#     drawer.goto(-radius, radius + 20)
#     drawer.pendown()

# # Function to restart drawing
# def restart():
#     draw_circle(50)

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Draw a Circle with Restart Button")
# screen.bgcolor("white")

# # Create a turtle named "drawer"
# drawer = turtle.Turtle()
# drawer.color("black")
# drawer.pensize(2)

# # Draw the initial circle
# draw_circle(50)

# # Create a button to restart drawing
# button = turtle.Turtle()
# button.penup()
# button.goto(-50, 100)
# button.write("Restart", align="center", font=("Arial", 16, "normal"))
# button.goto(-50, 80)
# button.shape("square")
# button.shapesize(1, 5)
# button.color("lightgray")
# button.pendown()

# # Make the button respond to clicks
# button.penup()
# button.goto(-50, 80)
# button.onclick(lambda x, y: restart())

# # Hide the turtle used for drawing the circle
# drawer.hideturtle()

# # Keep the window open until clicked
# screen.mainloop()
