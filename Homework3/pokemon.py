import random


def get_player(num):
    """
    Function --
        returns the name of the Pokemon associated with the number
    Parameter --
        num: number of the Pokemon
    return --
        the name of the Pokemon associated with the number
    """
    if num == 1:
        return "Bulbasaur"
    elif num == 2:
        return "Charmander"
    elif num == 3:
        return "Butterfree"
    elif num == 4:
        return "Rattata"
    elif num == 5:
        return "Weedle"
    elif num == 6:
        return "Pikachu"
    elif num == 7:
        return "Sandslash"
    elif num == 8:
        return "Jigglypuff"
    elif num == 9:
        return "Raichu"
    else:
        return "Diglett"


def num2RPS(num):
    """
    Function --
        turn number to rock, paper, scissors
    Paramaters --
        num: 1 or 2 or 3
    Return --
        ROCK if 1, PAPER if 2, SCISSORS if 3
    """
    if num == 1:
        return "ROCK"
    elif num == 2:
        return "PAPER"
    else:
        return "SCISSORS"


def rps2num(rps):
    """
    Function --
        turn rock, paper, scissors to number
    Paramaters --
        rps: ROCK, PAPER or SCISSORS
    Return --
        1 if ROCK, 2 if PAPER, 3 if SCISSORS
    """
    if rps == "ROCK":
        return 1
    elif rps == "PAPER":
        return 2
    else:
        return 3


def check_battle(computer, player):
    """
    Function --
        Get the result of a single Rock-Paper-Scissors encounter
    Parameters --
        computer: RPS selection for the computer
        player: RPS selection for the player
    Return --
        result of a single Rock-Paper-Scissors encounter
    """
    # if computer win, return computer
    if (
        (computer == 1 and player == 3)
        or (computer == 2 and player == 1)
        or (computer == 3 and player == 2)
    ):
        return "COMPUTER"
    # if player win, return player
    elif (
        (computer == 1 and player == 2)
        or (computer == 2 and player == 3)
        or (computer == 3 and player == 1)
    ):
        return "PLAYER"
    # if the RPS battle is tie, return draw
    elif computer == player:
        return "DRAW!"


def tournament():
    """
    Function --
        computer v.s. human Pokemon tournament. Play RPS against Pokemon.
    """
    # number of rounds red/blue team win
    red_win = 0
    blue_win = 0
    user_color = str(input("What team do you want (red or blue)? ")).upper()

    stop_game = False
    while not stop_game:
        if user_color == "RED":
            computer_color = "BLUE"
            # choose red team pokemon
            red_poke = get_player(random.randint(1, 10))
            # choose blue team pokemon
            blue_poke = get_player(random.randint(1, 10))
            print(
                f"{user_color} pokemon {red_poke} v.s.",
                f"{computer_color} pokemon {blue_poke}",
            )
            # user's RPS
            user_RPS = num2RPS(
                int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors "))
            )
            # computer's RPS
            computer_RPS = num2RPS(random.randint(1, 3))
            print(
                f"{red_poke} played {user_RPS}.",
                f"{blue_poke} played {computer_RPS}",
            )
            # turn user and computer RPS to number
            user_RPS = rps2num(user_RPS)
            computer_RPS = rps2num(computer_RPS)
            if check_battle(computer_RPS, user_RPS) == "COMPUTER":
                print(f"{computer_color} team wins with {blue_poke}!")
                blue_win += 1
            elif check_battle(computer_RPS, user_RPS) == "PLAYER":
                print(f"{user_color} team wins with {red_poke}")
                red_win += 1
            else:
                print("It's a draw! No winner!")
            # ask if user want to play again
            print("\n")
            again = input("Do you want to play again? (y/n) ")
            if again.lower() == "n":
                print("Tournament has ended!")
                print(f"RED team: {red_win}       BLUE team: {blue_win} ")
                if red_win > blue_win:
                    print("You win")
                elif blue_win > red_win:
                    print("I win!")
                else:
                    print("No winner!")
                stop_game = True  # stop game

        else:
            computer_color = "RED"
            # choose red team pokemon
            red_poke = get_player(random.randint(1, 10))
            # choose blue team pokemon
            blue_poke = get_player(random.randint(1, 10))
            print(
                f"{user_color} pokemon {blue_poke} v.s.",
                f"{computer_color} pokemon {red_poke}",
            )
            # user's RPS
            user_RPS = num2RPS(
                int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors "))
            )
            # computer's RPS
            computer_RPS = num2RPS(random.randint(1, 3))
            print(
                f"{blue_poke} played {user_RPS}.",
                f"{red_poke} played {computer_RPS}",
            )
            # turn user and computer RPS to number
            user_RPS = rps2num(user_RPS)
            computer_RPS = rps2num(computer_RPS)
            if check_battle(computer_RPS, user_RPS) == "COMPUTER":
                print(f"{computer_color} team wins with {red_poke}!")
                red_win += 1
            elif check_battle(computer_RPS, user_RPS) == "PLAYER":
                print(f"{user_color} team wins with {blue_poke}")
                blue_win += 1
            else:
                print("It's a draw! No winner!")
            # ask if user want to play again
            print("\n")
            again = input("Do you want to play again? (y/n) ")
            if again.lower() == "n":
                print("Tournament has ended!")
                print(f"RED team: {red_win}       BLUE team: {blue_win} ")
                if red_win > blue_win:
                    print("I win")
                elif blue_win > red_win:
                    print("You win!")
                else:
                    print("No winner!")
                stop_game = True  # stop game


if __name__ == "__main__":
    tournament()
