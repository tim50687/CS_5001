import turtle
import time
import random
from Tile import *
from PositionService import *
import os
from copy import deepcopy


class Gameboard:

    resource_path = "./slider_puzzle_project_fall2021_assets-2022/Resources/"
    image_path = "./slider_puzzle_project_fall2021_assets-2022/"
    defualt_puzzle = "mario"
    reset_path = resource_path + "resetbutton.gif"
    load_path = resource_path + "loadbutton.gif"
    quit_path = resource_path + "quitbutton.gif"

    # put this into function
    # find all of the available puzzle
    all_puzzle = [
        file
        for file in os.listdir("./slider_puzzle_project_fall2021_assets-2022")
        if file.endswith(".puz")
    ]

    correct_answer = []

    def __init__(
        self,
        name="Tim",
        play_times=10,
        puzzle=(-355, 320, 480, 480),
        leader=(170, 320, 185, 480),
        control=(-355, -205, 710, 115),
        reset=(80, -262),
        load=(180, -262),
        quit=(280, -262),
        thumbnail=(262.5, 250),
    ):
        self.name = name
        self.play_times = play_times
        self.puzzle = puzzle
        self.leader = leader
        self.control = control
        self.reset = reset
        self.load = load
        self.quit = quit
        self.thumbnail = thumbnail


class Turtle(Gameboard):
    # need to update tilerlist everytime change
    # cause tile click logic follows it
    tile_list = []
    click_count = 0
    count_stamp = 0

    def __init__(
        self,
        name=None,
        play_times=None,
        puzzle=(-355, 320, 480, 480),
        leader=(170, 320, 185, 480),
        control=(-355, -205, 710, 115),
        reset=(80, -262),
        load=(180, -262),
        quit=(280, -262),
        thumbnail=(262.5, 250),
        ttl=turtle.Turtle(),
        wds=turtle.Screen(),
        # create a eraser for write player move and clear player move
        eraser=turtle.Turtle(),
    ):
        super().__init__(
            name=None,
            play_times=None,
            puzzle=(-355, 320, 480, 480),
            leader=(170, 320, 185, 480),
            control=(-355, -205, 710, 115),
            reset=(80, -262),
            load=(180, -262),
            quit=(280, -262),
            thumbnail=(262.5, 250),
        )
        self.wds = wds
        self.eraser = eraser
        self.eraser.pencolor("black")  # put on the color
        self.eraser.speed(0)
        self.eraser.hideturtle()
        self.ttl = ttl
        self.ttl.pencolor("black")  # put on the color
        self.ttl.speed(0)
        self.ttl.width(4)  # thickness of turtle

    def splash_screen(self):  # get user data
        self.wds.setup(800, 730)
        self.wds.addshape(Turtle.resource_path + "/splash_screen.gif")

        # set the turtle shape to shape with a given name
        self.ttl.shape(Turtle.resource_path + "/splash_screen.gif")
        time.sleep(1)
        self.ttl.hideturtle()

    def get_user_data(self):
        self.name = self.wds.textinput("CS 5001 Puzzle Slide", "Your name:")
        self.play_times = self.wds.textinput(
            "CS 5001 Puzzle Slide - Moves",
            "Enter the number of moves (chances) you want (5-200)?",
        )

    def draw_square(self, tpl):
        x, y, length, width = tpl
        self.ttl.penup()  # pull the pen up
        self.ttl.setpos(x, y)  # set a position
        self.ttl.pendown()  # pull the pen down
        # Draw square
        self.ttl.forward(length)
        self.ttl.right(90)
        self.ttl.forward(width)
        self.ttl.right(90)
        self.ttl.forward(length)
        self.ttl.right(90)
        self.ttl.forward(width)
        self.ttl.right(90)

    def draw_image(self, tpl, gif):
        """_summary_

        Parameters
        ----------
        tpl : _type_
            _description_
        gif : _type_
            _description_
        """
        x, y = tpl
        self.ttl.penup()
        self.ttl.setpos(x, y)
        self.ttl.pendown()
        self.wds.addshape(gif)
        self.ttl.shape(gif)
        # Whatever the shape of the turtle is, it is printed at that point
        # and continues with the next instructions.
        astamp = self.ttl.stamp()
        self.count_stamp += 1
        return astamp

    def add_tile(self):
        """

        Returns
        -------
        _type_
            _description_
        """
        lst = []  # create a list to store created tile object
        list, size, thumbnail = self.puzzle_to_list(
            self.defualt_puzzle
        )  # puzzle will change

        ## safe the correct answer by making a deepcopy
        self.correct_answer = deepcopy(list)
        print(self.correct_answer)

        random.shuffle(list)  # shuffle the puzzle
        count = 0
        puzzle_num_dict = {16: 4, 9: 3, 4: 2}  # use the root
        divisor = puzzle_num_dict.get(len(list))
        x = -295
        y = 260
        for i in list:
            ## keep track of the blank tile
            if "blank" in i:
                # create a instance to keep track of blank
                set_position(x, y)
            if count % divisor == 0 and count != 0:
                y -= size
                x -= size * divisor
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            else:
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            # create a tile object
            lst.append(
                Tile(x, y, Gameboard.image_path + i, size, astamp)
            )  # pass in the coordinate, ignore tile and path first
            x += size
            count += 1
        # draw thumbnail
        self.draw_image(self.thumbnail, Gameboard.image_path + thumbnail)
        # everytime add a tile change the tile_data property
        self.tile_list = lst
        # # clear the count
        # self.click_count = 0

    @staticmethod
    def swap_element_in_list(list, element1, element2):
        list[element1], list[element2] = list[element2], list[element1]
        return list

    @staticmethod
    def puzzle_to_list(puzzle):
        """sort the puzzle data

        Parameters
        ----------
        puzzle : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        # clean data
        path = "./slider_puzzle_project_fall2021_assets-2022/" + puzzle + ".puz"
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            gif_data = f.readlines()[4:]
            f.seek(0)
            gif_size = f.readlines()[2].strip("\n").strip("size: ")
            f.seek(0)
            gif_thumbnail = f.readlines()[3].strip("\n").strip("thumbnail: ")

            for i in range(len(gif_data)):
                gif_data[i] = gif_data[i].strip("\n").strip(str(i + 1) + ": ")
        return gif_data, int(gif_size), gif_thumbnail

    def click(self, x, y):
        # get the size of the tile
        size = self.tile_list[0].size
        if 240 < x < 320 and -288.5 < y < -235.5:
            self.quit_click(x, y)

        elif 40 < x < 120 and -302 < y < -222:
            self.reset_click(x, y)
        elif 140 < x < 220 and -300 < y < -224:
            self.load_click(x, y)
        # else:
        elif (
            -355 < x < -355 + (len(self.tile_list) ** (1 / 2)) * size
            and 320 - (len(self.tile_list) ** (1 / 2)) * size < y < 320
        ):
            self.tile_click(x, y)

    def quit_click(self, x, y):
        self.draw_image((0, 0), Gameboard.resource_path + "quitmsg.gif")
        self.wds.update()
        time.sleep(3)
        self.wds.bye()

    def load_click(self, x, y):
        # get all the puzzle
        puz = "\n".join(Gameboard.all_puzzle)
        new_puzzle = self.wds.textinput("Load Puzzle!", puz)
        print("tile need to be clean", len(self.tile_list))
        # also need to remove how many time you move
        # for tile in self.tile_list:
        #     self.ttl.clearstamp(tile.astamp)
        print(-len(self.tile_list))
        self.ttl.clearstamps(-len(self.tile_list) - 1)
        self.click_count = 0
        self.extra_stamp = 0
        self.defualt_puzzle = new_puzzle.strip(".puz")
        # clear before puzzle moves
        self.eraser.clear()
        self.add_tile()

        print(self.tile_list[0].image)

    def reset_click(self, x, y):
        lst = []
        list, size, thumbnail = self.puzzle_to_list(self.defualt_puzzle)
        count = 0
        puzzle_num_dict = {16: 4, 9: 3, 4: 2}  # use the root
        divisor = puzzle_num_dict.get(len(list))
        x = -295
        y = 260
        self.ttl.clearstamps(-len(self.tile_list) - 1)
        for i in list:

            ## keep track of the blank tile
            if "blank" in i:
                # create a instance to keep track of blank
                set_position(x, y)
            if count % divisor == 0 and count != 0:
                y -= size
                x -= size * divisor
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            else:
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            # create a tile object
            lst.append(
                Tile(x, y, Gameboard.image_path + i, size, astamp)
            )  # pass in the coordinate, ignore tile and path first
            x += size
            count += 1
        self.draw_image(self.thumbnail, Gameboard.image_path + thumbnail)
        self.tile_list = lst
        print("reset")

    def tile_click(self, x, y):
        """logic when clicking on the tile, win, and lose

        Parameters
        ----------
        x : _type_
            _description_
        y : _type_
            _description_
        """
        list = []
        self.click_count += 1
        blank_x = get_position_x()
        blank_y = get_position_y()
        # find the tile that can be change
        for tile in self.tile_list:
            if (
                tile.coordinate_x + tile.size == blank_x
                or tile.coordinate_x - tile.size == blank_x
            ) and tile.coordinate_y == blank_y:
                list.append(tile)
            if (
                tile.coordinate_y + tile.size == blank_y
                or tile.coordinate_y - tile.size == blank_y
            ) and tile.coordinate_x == blank_x:
                list.append(tile)
            if "blank" in tile.image:
                blank = tile

        for adjacent_tile in list:
            if (
                adjacent_tile.coordinate_x - adjacent_tile.size / 2
                < x
                < adjacent_tile.coordinate_x + adjacent_tile.size / 2
                and adjacent_tile.coordinate_y - adjacent_tile.size / 2
                < y
                < adjacent_tile.coordinate_y + adjacent_tile.size / 2
            ):
                # switch the position in the tile_list to check if the user solve the puzzle
                # self.swap_element_in_list(self.tile_list, )
                # switch the tile
                adjacent_tile.switch(blank)
                # reset the blank tile x, y
                set_position(blank.coordinate_x, blank.coordinate_y)

                self.ttl.clearstamp(adjacent_tile.astamp)

                self.ttl.clearstamp(blank.astamp)

                astamp = self.draw_image(
                    (adjacent_tile.coordinate_x, adjacent_tile.coordinate_y),
                    adjacent_tile.image,
                )
                adjacent_tile.astamp = astamp  # update the stamp
                bstamp = self.draw_image(
                    (blank.coordinate_x, blank.coordinate_y),
                    blank.image,
                )
                blank.astamp = bstamp  # update the stamp
        # write the player move and keep update
        self.eraser.clear()
        self.eraser.penup()
        self.eraser.setpos(-340, -275)
        self.eraser.pendown()
        self.eraser.write(
            f"Player move: {self.click_count}", font=("Calibri", 30, "bold")
        )
        # win or lose logic
        if self.click_count > int(self.play_times):
            self.lose()

    def win(self):
        self.draw_image((0, 0), Gameboard.resource_path + "winner.gif")
        self.wds.update()
        time.sleep(3)
        self.wds.bye()

    def lose(self):
        self.draw_image((0, 0), Gameboard.resource_path + "Lose.gif")
        self.wds.update()
        time.sleep(3)
        self.wds.bye()

    def pregame(self, square_func, image_func):
        """Control turtle to implement the pregame layout

        Parameters
        ----------
        square_func : _type_
            _description_
        image_func : _type_
            _description_
        """
        self.splash_screen()
        self.get_user_data()
        square_func(self.puzzle)
        square_func(self.leader)
        square_func(self.control)
        image_func(self.reset, Turtle.reset_path)
        image_func(self.load, Turtle.load_path)
        image_func(self.quit, Turtle.quit_path)


def main():
    a = Turtle()
    a.add_tile()
    print(a.correct_answer)


if __name__ == "__main__":
    main()
