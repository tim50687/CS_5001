"""
    CS 5001     
    Fall 2022
    Jen Ting Huang
    Homework5: ReMix Master
"""
from music import *
import copy
import random


def user_menu():
    """
    Function --
        Shows the user menu and store user's choice
    Return --
        User's choice
    """
    user_choice = str(
        input(
            "ReMix-Master:\n L: Load a different song\n "
            "T: Title of current song\n S: Substitute a word\n "
            "P: Playback your song\n R: Reverse it!\n "
            "X: Reset to original song\n "
            "Q: Quit?\n Your choice: "
        )
    )
    return user_choice


def show_song(song):
    """
    Function --
        Shows the song's lyrics
    Parameter --
        song: list of song that is currently remixing
    Return --
        None
    """
    for i in range(len(song)):
        print(song[i])


def show_playlist():
    """
    Function --
        Show the index and song of the playlist
    Return --
        None
    """
    for i, j in enumerate(PLAYLIST):
        print(f"{i+1}: {j}")


def new_lyrics_list(song):
    """
    Function --
        Get the new list of song lyrics,
        elements are the string of each line of lyrics
        (Punctuation removed!)
    Parameter --
        song: song that is currently remixing,
              which is the list containing
              multiple strings
    Return --
        None
    """
    for line in range(len(song)):
        # Remove the punctuation in each word
        for chr in [",", ".", "?"]:
            song[line] = song[line].replace(chr, "")
    return None


def word_in_lyrics(song, old_word):
    """
    Function --
        Take a song, and check if the word exists
        in the song
    Parameters --
        song: song that is currently remixing,
              which is the list containing
              multiple strings
        old_word: word you want to check if its in
                  the lyrics
    Return --
        count: How many time the word shows in the lyrics
    """
    # Use copy to test if the word
    # is in the lyrics, so that it won't
    # effect the original song
    copy_song = song.copy()
    new_lyrics_list(copy_song)
    count = 0  # count the times that word shows up
    for i in range(len(copy_song)):
        line = copy_song[i].split()
        if str(old_word) in line:
            count += 1
    return count


def substitute(song, old_word, new_word):
    """
    Function --
        Takes a song, replaces every occurence
        of the old word with the new word
    Parameters --
        song: song that is currently remixing,
              which is the list containing
              multiple strings
        old_word: word you want to replace with
        new_word: new replacement word
    Return --
        If the old word is found and replace, return True.
        Otherwise, return False
    """
    count = word_in_lyrics(song, old_word)
    # if old_word not found, return False
    if count == 0:
        return False
    # get new lyrics, removed the punctuation
    new_lyrics_list(song)
    for i in range(len(song)):
        line = song[i].split()
        for j in range(len(line)):
            if str(old_word) == line[j]:
                line[j] = str(new_word)
        song[i] = " ".join(line)
    return True


def reverse_it(song):
    """
    Function --
        Reverse each line of lyrics
    Parameter --
        song: song that is currently remixing,
              which is the list containing
              multiple strings
    Return --
        Song which each line of lyrics are reversed
    """
    # get new lyrics, removed the punctuation
    new_lyrics_list(song)
    for i in range(len(song)):
        # reversed each line of lyrics
        word = song[i].split()[::-1]
        line = " ".join(word)
        # modified the song
        song[i] = line
    return song


def load_song(selection):
    """
    Function --
        Takes an integer(which is index
        in playlist), and return a list
        that contain the selected song,
        and a string represents the song
    Parameter --
        selection: index of playlist
    Return --
        List:
            index 0 -> selected song
            index 1 -> song's title
    """
    # If user's input is not integer or
    # not in the range of playlist
    # return False
    list = []
    if not str(selection).isdigit():
        return list
    elif int(selection) not in range(1, len(PLAYLIST) + 1):
        return list
    list.append(SONGS[int(selection) - 1])  # add song
    list.append(PLAYLIST[int(selection) - 1])  # add title
    return list


def main():
    # randomly choose a default song in the beginning
    number = str(random.randint(1, len(PLAYLIST)))
    current_song = load_song(number)
    # create a deepcopy of SONGS
    copy_song = copy.deepcopy(SONGS)
    # Keep asking until user quit
    while True:
        user_choice = user_menu()
        # Load a different song
        if user_choice.upper() == "L":
            print("Choose the number of song you want to load\n")
            show_playlist()
            song_choice = input("Your choice: ")
            current_song = load_song(song_choice)
            if current_song == []:
                print("Invalid Value, Mixed song unchanged!!")
        # Title of current song
        elif user_choice.upper() == "T":
            print("♬" * 20)
            print(f"You are mixing the song: {current_song[1]}")
            print("♬" * 20)
        # Substitute a word
        elif user_choice.upper() == "S":
            old_word = str(input("What word do you want to replace? "))
            new_word = str(input("What word do you want to use? "))
            if substitute(current_song[0], old_word, new_word) is False:
                print(f"Sorry, I didn't find {old_word} in current song")
        # Playback your song
        elif user_choice.upper() == "P":
            print("♬" * 20)
            show_song(current_song[0])
            print("♬" * 20)
        # Reverse it!
        elif user_choice.upper() == "R":
            current_song[0] = reverse_it(current_song[0])
        # Reset to original song
        elif user_choice.upper() == "X":
            song_index = PLAYLIST.index(current_song[1])
            current_song[0] = copy_song[song_index]
        # Quit
        elif user_choice.upper() == "Q":
            print("You are the best!!!")
            break


if __name__ == "__main__":
    a = load_song(1)
    print(a)
