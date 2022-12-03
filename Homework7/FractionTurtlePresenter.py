from SimpleFraction import SimpleFraction
import turtle


class FractionTurtlePresenter:
    """
    FractionTurtlePresenter is a 'View' for the Fraction model. It is
    simply a way of rendering the Fraction as 'graphical text' using the Turtle
    package so we can effect a 'separation of concerns'. Graphic I/O is handled here
    whilst the fundamentals of what fractions do is preserved in the model class
    """

    def __init__(self, fraction):
        self.fraction = fraction

    def draw(self):
        turtle.write(self.fraction, font=("Verdana", 54, "normal"))

    def update_model(self, fraction):
        self.fraction = fraction
        self.update()

    def update(self):
        self.draw()
