from puzzle_game import *
from PositionService import *


def main():
    a = Turtle()
    # a.splash_screen()
    a.pregame(a.draw_square, a.draw_image)

    a.add_tile()
    # print(a.switch_tile(2, 2))
    a.wds.onclick(a.click)
    turtle.done()


if __name__ == "__main__":
    main()
