'''
    CS5001
    Fall 2022
    Jen Ting Huang
    Homework 2: Programming #3
'''
from turtledriver import *
import turtle
screen = turtle.Screen()
image = "shape_window.png"
# turtle.speed(5) # make the turtle walk fast

# Initialize a screen to a given size
screen.setup(width=970, height=635)
# Use an image as your background
screen.bgpic(image)
# Hide the turtle
turtle.hideturtle()

def main():
    # Draw a green square
    draw_square(80, 0, 0, "green", "")
    # Draw a circle
    draw_circle(40, 0, 0, "red", "")
    # move to the user input coordinate and draw fillcolor circle and square
    move("purple", "yellow")


if __name__ == "__main__":
    main()