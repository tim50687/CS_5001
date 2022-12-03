from puzzle_game import *


class Tile:
    def __init__(
        self,
        coordinate_x=0,
        coordinate_y=0,
        image="",
        size=0,
        astamp=0,
        path="./slider_puzzle_project_fall2021_assets-2022/mario.puz",
        tile="mario",
    ):

        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.image = image
        self.size = size
        self.astamp = astamp
        self.path = path
        self.tile = tile

    def switch(self, other):
        temp_coordinate_x = self.coordinate_x
        self.coordinate_x = other.coordinate_x
        other.coordinate_x = temp_coordinate_x

        temp_coordinate_y = self.coordinate_y
        self.coordinate_y = other.coordinate_y
        other.coordinate_y = temp_coordinate_y


def main():
    test_tile = Tile()


if __name__ == "__main__":
    main()
