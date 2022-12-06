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
    defualt_puzzle = "mario"  # keep track of the current puzzle
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
    is_reset = False

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
        leader_pencil=turtle.Turtle(),
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
        self.leader_pencil = leader_pencil
        self.leader_pencil.pencolor("blue")  # put on the color
        self.leader_pencil.speed(0)
        self.leader_pencil.hideturtle()
        self.ttl = ttl
        self.ttl.pencolor("black")  # put on the color
        self.ttl.speed(0)
        self.ttl.width(4)  # thickness of turtle
        self.ttl.hideturtle()

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

    @staticmethod
    def bubble_sort(list):
        """to sort the leader

        Parameters
        ----------
        list : _type_
            _description_
        """
        for passnum in range(len(list) - 1, 0, -1):

            for i in range(passnum):
                if int(list[i].split()[1]) > int(list[i + 1].split()[1]):
                    temp = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = temp
        return list

    def leader_board_info(self):
        """update the leader board corresponding to the puzzle"""
        # always shows the top 5 - to do
        self.leader_pencil.clear()
        self.leader_pencil.penup()
        self.leader_pencil.setpos(195, 150)
        self.leader_pencil.pendown()
        # create a empty list to store current puzzzle top 5 leader
        current_leader = []
        with open("./leader.txt", "r", encoding="utf-8") as f:
            for line in f:
                puzzle = line.strip("\n").split(" ")[2]
                if puzzle == self.defualt_puzzle:
                    current_leader.append(line)

        self.leader_pencil.write(
            f"Puzzle: {self.defualt_puzzle}\nLeaders: ",
            align="left",
            font=("Calibri", 15, "bold"),
        )
        leader_Y_position = 130  # first leader showup position
        self.bubble_sort(current_leader)
        for i in range(len(current_leader)):
            if i > 4:  # only shows up
                break
            self.leader_pencil.penup()
            self.leader_pencil.setpos(195, leader_Y_position)
            self.leader_pencil.pendown()
            self.leader_pencil.write(
                f"{current_leader[i].split()[0]}: {current_leader[i].split()[1]}",
                align="left",
                font=("Calibri", 15, "bold"),
            )
            leader_Y_position -= 20  # move down a bit

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
        ## in order to compare to the tilelist
        self.correct_answer = deepcopy(list)
        print("before shuffle", list)
        for i in range(len(self.correct_answer)):
            self.correct_answer[i] = Gameboard.image_path + self.correct_answer[i]

        random.shuffle(list)  # shuffle the puzzle
        count = 0
        puzzle_num_dict = {16: 4, 9: 3, 4: 2}  # use the root
        divisor = puzzle_num_dict.get(len(list))
        x = -295
        y = 260
        print(list)
        for i in list:
            ## keep track of the blank tile
            print(i)
            if "blank" in i:
                # create a instance to keep track of blank
                set_position(x, y)
            if count % divisor == 0 and count != 0:
                print(i)
                y -= size + 2
                x -= (size + 2) * divisor
                if "blank" in i:
                    # create a instance to keep track of blank
                    set_position(x, y)
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            else:
                print(i, x, y)
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            # create a tile object
            lst.append(
                Tile(x, y, Gameboard.image_path + i, size, astamp)
            )  # pass in the coordinate, ignore tile and path first
            x += size + 2
            count += 1
        # draw thumbnail
        self.draw_image(self.thumbnail, Gameboard.image_path + thumbnail)
        #  write leader board
        self.leader_board_info()
        # everytime add a tile change the tile_data property
        self.tile_list = lst
        # # clear the count
        # self.click_count = 0

    @staticmethod
    def swap_element_in_list(list, element1, element2):
        """swtich the element in the list

        Parameters
        ----------
        list : _type_
            _description_
        element1 : _type_
            _description_
        element2 : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        index1, index2 = list.index(element2), list.index(element1)
        list[index1], list[index2] = list[index2], list[index1]
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
            -295 - size / 2
            < x
            < -295
            + (len(self.tile_list) ** (1 / 2)) * (size + 2)
            - size / 2
            - (len(self.tile_list) ** (1 / 2)) * 2
            and 260
            - ((len(self.tile_list) ** (1 / 2)) - 1) * (size + 2)
            - size / 2
            - ((len(self.tile_list) ** (1 / 2)) - 1) * 2
            < y
            < 260 + size / 2
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
        # also need to remove how many time you move
        # for tile in self.tile_list:
        #     self.ttl.clearstamp(tile.astamp)
        self.ttl.clearstamps(-len(self.tile_list) - 1)
        self.click_count = 0
        self.extra_stamp = 0
        self.defualt_puzzle = new_puzzle.strip(".puz")
        # clear before puzzle moves
        self.eraser.clear()
        self.add_tile()

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
                y -= size + 2
                x -= (size + 2) * divisor
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            else:
                astamp = self.draw_image((x, y), Gameboard.image_path + i)
            # create a tile object
            lst.append(
                Tile(x, y, Gameboard.image_path + i, size, astamp)
            )  # pass in the coordinate, ignore tile and path first
            x += size + 2
            count += 1
        self.draw_image(self.thumbnail, Gameboard.image_path + thumbnail)
        self.tile_list = lst
        self.is_reset = True  #
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
        print("inside the tile")
        list = []
        # self.click_count += 1
        blank_x = get_position_x()
        blank_y = get_position_y()
        # find the tile that can be change
        for tile in self.tile_list:
            if (
                tile.coordinate_x + tile.size + 2 == blank_x
                or tile.coordinate_x - tile.size - 2 == blank_x
            ) and tile.coordinate_y == blank_y:
                list.append(tile)
            if (
                tile.coordinate_y + tile.size + 2 == blank_y
                or tile.coordinate_y - tile.size - 2 == blank_y
            ) and tile.coordinate_x == blank_x:
                list.append(tile)
            if "blank" in tile.image:
                blank = tile
        print(list)

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
                self.swap_element_in_list(self.tile_list, adjacent_tile, blank)
                # switch the tile
                adjacent_tile.switch(blank)
                # after using reset button, make user still need to swap the tile to win
                self.is_reset = False
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
                # if user swap tile, click +=1
                self.click_count += 1
        # write the player move and keep update
        if self.click_count >= 1:
            self.eraser.clear()
            self.eraser.penup()
            self.eraser.setpos(-340, -275)
            self.eraser.pendown()
            self.eraser.write(
                f"Player move: {self.click_count}", font=("Calibri", 30, "bold")
            )
        # win or lose logic
        # each click check if user lose logic
        if self.click_count > int(self.play_times):
            self.lose()
        # then each click check if user win logic
        for i in range(len(self.tile_list)):
            if self.tile_list[i].image == self.correct_answer[i]:
                if (
                    i == len(self.tile_list) - 1
                    and self.tile_list[i].image == self.correct_answer[i]
                    and self.click_count <= int(self.play_times)
                    and not self.is_reset
                ):
                    # put the winner in the txt file
                    with open("./leader.txt", "a", encoding="utf-8") as f:
                        f.write(
                            self.name
                            + " "
                            + str(self.click_count)
                            + " "
                            + self.defualt_puzzle
                            + "\n"
                        )
                    self.win()
                continue
            break

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
    a.leader_board_info()


if __name__ == "__main__":
    main()
