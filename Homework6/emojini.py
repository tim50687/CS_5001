"""
    CS 5001
    2022 Fall
    Jen Ting Huang
    Homework 6: Program 1 - Emojini 
"""


def sort_data(emoji_file):
    """
    Function --
        Open the file, sort the data to dictionary.
        Ex. {"Metadata": [emoji set]}
    Parameter --
        emoji_file: Metadata file
    Return --
        Dictionary
    """
    try:
        emoji_list = []  # store the emoji in to a list
        with open(emoji_file, "r", encoding="utf-8") as f:
            # Get the metadata
            read_file = f.readline().split()[1:]
            # remember current position (after read metadata)
            cur_position = f.tell()
            length = len(f.readlines())
            # Go back to the position where metadata ends
            f.seek(cur_position)
            for i in range(length):
                data = f.readline().split()
                for j in range(len(data)):
                    if i == 0:
                        emoji_list.append(data[j].split())
                    else:
                        emoji_list[j].append(data[j])
            # Create dictionary
            sort_dict = dict(zip(read_file, emoji_list))
        return sort_dict
    except FileNotFoundError:
        print("Error: Could not find your file!")
    except PermissionError:
        print("Oops you don't have the access right to this file!")


def replace_word(emoji_file_name, file1, file2, emojis, new_emojis):
    """
    Function --
        Replace all emojis in file1 with new_emoji,
        and create a new file2 with the new content.
    Parameters --
        emoji_file_name: Emoji mapping file
        file1: File you want to change emojis
        file2: File with new content after replacement
        emojis: List of emojis you want to change in file1
        new_emojis: List of emojis you want to replace
                    old emojis in file1
    Return --
        None
    """
    try:
        sort_dict = sort_data(emoji_file_name)
        # check if the transformation involved English
        list_E = sort_dict["ENGLISH"]
        # list of each line after replacement
        replace_line = []
        with open(file1, "r", encoding="utf-8") as f:
            for line in f:
                list = line.strip("\n").split()
                # Change each line in every loop.
                # Three cases:
                for i in range(len(list)):
                    # One: Replace emojis to English
                    if list[i] in emojis and list_E == new_emojis:
                        one_index = emojis.index(list[i])
                        list[i] = new_emojis[one_index].lower()
                    # Two: Replace English to other emojis
                    elif list[i].capitalize() in emojis and list_E == emojis:
                        sec_index = emojis.index(list[i].capitalize())
                        list[i] = new_emojis[sec_index]
                    # Three: emojis to emojis
                    elif list[i] in emojis:
                        third_index = emojis.index(list[i])
                        list[i] = new_emojis[third_index]

                replace_line.append(list)
        # Write the new content to new file
        with open(file2, "w", encoding="utf-8") as f:
            for i in replace_line:
                f.write(" ".join(i) + "\n")
        return None
    except FileNotFoundError:
        print("Error: Could not find your file!")
    except PermissionError:
        print("Oops you don't have the access right to this file!")


def batch_translate(emoji_file_name, directives_file_name):
    """
    Function --
        Replace the emojis in file by the instruction
        in the directive file.
    Parameters --
        emoji_file_name: Emoji mapping file
        directives_file_name: File which gives instruction
        for the type of transformation to run, and also
        orchestrates the process of converting the text
        as specified.
    Return --
        None
    """
    try:
        sort_dict = sort_data(emoji_file_name)
        with open(directives_file_name, "r", encoding="utf-8") as f:
            for line in f:
                # Get each instruction
                instruction = line.strip("\n").split()
                old_emoji = instruction[0]  # emoji be replaced
                new_emoji = instruction[1]  # emoji want to replace with
                source_file = instruction[2]  # input file
                new_file = instruction[3]  # output file

                replace_word(
                    emoji_file_name,
                    source_file,
                    new_file,
                    sort_dict[old_emoji.upper()],
                    sort_dict[new_emoji.upper()],
                )

    except FileNotFoundError:
        print("Error: Could not find your file!")
    except PermissionError:
        print("Oops you don't have the access right to this file!")


def main():
    pass


if __name__ == "__main__":
    main()
