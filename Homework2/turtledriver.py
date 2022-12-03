'''
    CS5001
    Fall 2022
    Jen Ting Huang
    Homework 2: Programming #3
'''
import turtle


def draw_square(length, X, Y, color, fillColor):
    '''
    Function --
        Draw a square
    :param length: length of square
    :param X: X coordinate
    :param Y: T coordinate
    :param color: pen color
    :param fillColor: fillcolor
    :return: void
    '''

    turtle.fillcolor(fillColor)  # set up the color you want to fill in
    turtle.begin_fill()
    turtle.penup()  # pull the pen up
    turtle.setpos(X - 40, Y + 40)  # set a position
    turtle.pendown()  # pull the pen down
    turtle.pencolor(color)  # put on the color
    # Draw circle
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.end_fill()


def draw_circle(radius, X, Y, color, fillColor):
    '''
    Function --
        Draw a circlr
    :param radius: radius of circle
    :param X: X coordinate
    :param Y: Y coordinate
    :param color: pen color
    :param fillColor: fillcolor
    :return: void
    '''
    # Draw a circle
    turtle.fillcolor(fillColor)  # set up the color you want to fill in
    turtle.begin_fill()
    turtle.penup()  # pull the pen up
    turtle.setpos(X + 40, Y)  # set a position
    turtle.pendown()  # pull the pen down
    turtle.pencolor(color)  # put on the color
    turtle.circle(radius)  # draw circle
    turtle.end_fill()


def move(fillcolor_square, fillcolor_circle):
    """
    Function --
        Let user input the coordina
    :param fillcolor_square:
    :param fillcolor_circle:
    :return:
    """
    # Ask the user to input new coordinate for square and circle
    squareX = int(input("X coordinate for the square "))
    squareY = int(input("Y coordinate for the square "))
    circleX = int(input("X coordinate for the circle "))
    circleY = int(input("Y coordinate for the circle "))

    # Clear screen
    turtle.clear()

    # right now the turtle is facing up! Need to make it turn right!
    turtle.right(90)  # make it turn right

    # redraw the fillcolor square (yellow)
    draw_square(80, squareX, squareY, fillcolor_square, fillcolor_square)

    # redraw the fillcolor circle
    draw_circle(40, circleX, circleY, fillcolor_circle, fillcolor_circle)

    turtle.done()
