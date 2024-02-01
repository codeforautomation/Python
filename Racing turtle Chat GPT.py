# This code is created by Chat GPT and dont know much about this code
import turtle
import random

# Function to move the turtle forward randomly
def move_turtle(t):
    distance = random.randint(1, 20)
    t.forward(distance)

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")

# Create turtles
turtle_1 = turtle.Turtle()
turtle_1.shape("turtle")
turtle_1.color("red")

turtle_2 = turtle.Turtle()
turtle_2.shape("turtle")
turtle_2.color("blue")

# Set starting positions
turtle_1.penup()
turtle_1.goto(-200, 20)
turtle_1.pendown()

turtle_2.penup()
turtle_2.goto(-200, -20)
turtle_2.pendown()

# Run the race
for _ in range(100):
    move_turtle(turtle_1)
    move_turtle(turtle_2)

# Determine the winner
winner = "Red" if turtle_1.xcor() > turtle_2.xcor() else "Blue" if turtle_2.xcor() > turtle_1.xcor() else "It's a tie!"

# Display the winner
turtle.goto(-50, 0)
turtle.write(f"The winner is {winner} turtle!", align="center", font=("Arial", 16, "normal"))

# Close the window on click
screen.exitonclick()
