"""
    CS 5001
    Fall 2022
    Jen Ting Huang
    Homework3: Programming #1
"""
import turtle
import PositionService

_pen = turtle


image = "shape_window.png"
screen = turtle.Screen()
# _pen.speed(0)  # make the turtle walk fast

# Initialize a screen to a given size
screen.setup(width=970, height=635)
# Use an image as your background
screen.bgpic(image)
# hide the turtle
_pen.hideturtle()


def draw_circle(X, Y, radius, color):
    """
    Function --
        draw a circle
    Parameters --
        X: X coordinate for circle
        Y: Y coordinate for circle
        radius: radius of circle
        color: color of your pen
    Return --
        void
    """
    _pen.pencolor(color)
    _pen.penup()  # pull the pen up
    _pen.setpos(X, Y - 80)  # set a position
    _pen.pendown()  # pull the pen down
    _pen.circle(radius)


def play():
    """
    Function --
        Playing the game:
        Start drawing circle at (0,0)
        When you click anywhere outside of a drawn circle, the click is ignored.
        When you click anywhere on a blank canvas, draw the circle,
        with the center at the (x, y) coordinates where you clicked
    Return --
        void
    """
    global _pen  # using the global pen
    # Start drawing circle at (0,0)
    draw_circle(0, 0, 80, "green")
    # store x, y coordinate in virtual notebook(PositionService)
    PositionService.set_visible(True)
    PositionService.set_position_x(0)
    PositionService.set_position_y(0)
    screen.onclick(click)


def click(x, y):
    """
    Function --
        Define what will happen after you click the screen while playing game
    Parameters --
        x: the X coordinate from the user click
        y: the Y coordinate from the user click
    Return --
        void
    """
    # get the last x position you saved
    center_x = PositionService.get_position_x()
    print(center_x)

    # get the last y position you saved
    center_y = PositionService.get_position_y()
    print(center_y)
    # When you click anywhere outside of a drawn circle, the click is ignored.
    if (
        -80 < (x - center_x) < 80
        and -80 < (y - center_y) < 80
        and PositionService.is_visible() == True
    ):
        _pen.clear()
        PositionService.set_visible(False)
    # If circle is hidden, when you click anywhere on a blank canvas, draw the circle,
    # with the center at the (x, y) coordinates where you clicked
    elif PositionService.is_visible() == False:
        draw_circle(x, y, 80, "green")
        PositionService.set_position_x(x)
        PositionService.set_position_y(y)
        PositionService.set_visible(True)
        print("I caught you clicking at ({}, {})!".format(x, y))


def main():
    play()
    _pen.done()  # stop the screen from disapearing


if __name__ == "__main__":
    main()
