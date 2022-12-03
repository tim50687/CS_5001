"""
    CS 5001
    Fall 2022
    Jen Ting Huang
    Homework4: Programming #2
"""
import random


def create_deck():
    """
    Function --
        Create a deck of 52 cards
    Return --
        A list of cards, not shuffled
    """
    value = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]
    suit = ["s", "h", "d", "c"]
    original_deck = []  # Create unshuffled deck
    # Combine value and suit and append them to list
    for i in range(len(suit)):
        for j in range(len(value)):
            original_deck.append(str(value[j]) + suit[i])
    return original_deck


def shuffle(cards):
    """
    Function --
        Shuffle 52 new cards in a new list
    Return --
        New list with shuffle cards
    """
    shuffle_deck = []
    # Create a copy of original deck
    copy = []
    for i in range(52):
        copy.append(cards[i])
    # Shuffle cards
    a = 51
    for i in range(52):
        # Pick a random number which means index of cards
        x = random.randint(0, a)
        # Append element located at index x in copy list
        # to shuffle_deck list
        shuffle_deck.append(copy[x])
        # In copy list,
        # pop the element located at index of x variable
        copy.pop(x)
        a -= 1
    return shuffle_deck


def deal(number_of_hands, number_of_cards, cards):
    """
    Function --
        Take the number of hands, number of cards per hand,
        and deal card to players
    Parameters --
        number_of_hands: players number
        number_of_cards: number of cards per player
        cards: already shuffled deck
    Return --
        A lists of hands which each hand itself
        is a list of cards dealt for player
    """
    # Precondition
    if number_of_cards > 13 or number_of_cards < 0:
        return "the input value should be 0~13(included)"
    elif number_of_hands < 1 or number_of_hands > 4:
        return "the input value should be 1~4(included)"
    # If deal 0 cards
    elif number_of_cards == 0:
        return [[]] * number_of_hands
    card_dealt = []
    # Deal cards
    for i in range(number_of_cards):
        for j in range(number_of_hands):
            if i < 1:  # Create nth based of number of hands
                card_dealt.append([])
            card_dealt[j].append(cards[0])
            cards.pop(0)

    return card_dealt


# Test
original_deck = create_deck()
shuffle_deck = shuffle(original_deck)
print("Deal one round for 4 player \n", deal(4, 5, shuffle_deck))

# Cards left in deck
cards_left = []
for i in range(len(original_deck)):
    if original_deck[i] in shuffle_deck:
        cards_left.append(original_deck[i])
print("\nCards left in deck \n", cards_left)
