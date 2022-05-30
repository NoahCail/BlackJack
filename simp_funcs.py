"""Python Module containing all the main functions needed for the overall BlackJack program"""

# TODO: Add in functionality for doubling down and splitting on pairs
# TODO: Add in functionality for there to be a player and a balance. Also can decide how much to bet each hand
# TODO: Build in functionality to be able to see the cards drawn by the dealer
import random as r

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
logo_counter = 0

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def declaration(player_hand, comp_hand, final):
    """Returns the current or final player and computer hands as well as their current or final scores"""

    if final:
        return f'Your final hand: {player_hand}, Final score: {sum(player_hand)} \n \
        Computer\'s final hand: {comp_hand}, Final score: {sum(comp_hand)} \n'
    else:
        return f'Your current hand: {player_hand}, Current score: {sum(player_hand)} \n \
        Computer\'s current hand: {comp_hand[1:]}, Current score: ? \n'


def deal_cards():
    """Returns the initial hands of both the player and the """

    pc1, pc2 = r.choice(cards), r.choice(cards)
    cc1, cc2 = r.choice(cards), r.choice(cards)
    p_cards = [pc1, pc2]
    c_cards = [cc1, cc2]

    return [p_cards, c_cards]


def start_game(first):
    """Starts the black jack game and is reused to also restart the game after the initial play"""

    answer = input('Would you like to play a game of Black Jack? Type "y" for Yes and "n" for No: ')
    if answer == 'y':
        if first:
            print(logo)
            p_hand, c_hand = deal_cards()
            print(declaration(p_hand, c_hand, False))
            card_q(p_hand, c_hand)
        else:
            p_hand, c_hand = deal_cards()
            print(declaration(p_hand, c_hand, False))
            card_q(p_hand, c_hand)
    elif answer == 'n':
        if first:
            print('Then why did you start the program in the first place?')
        else:
            print('Thanks for playing!')
    else:
        if first:
            print('Isn\'t it so tough to type a y or an n, no but seriously figure it out')
            start_game(True)
        else:
            print('Isn\'t it so tough to type a y or an n, no but seriously figure it out')
            start_game(False)


def dealer_q(player_hand, comp_hand):
    """Handles the dealers turn once the player is at 21 or has chosen to stand and returns the results of the game"""
    x, y = sum(player_hand), sum(comp_hand)

    if x > 21:
        print('You went over 21. You lose.')
        print(declaration(player_hand, comp_hand, True))
        start_game(False)
    elif y > 21:
        if 11 in comp_hand and y < 31:
            x = comp_hand.index(11)
            comp_hand[x] = 1
            dealer_q(player_hand, comp_hand)
        else:
            print('The computer went over. You win!')
            print(declaration(player_hand, comp_hand, True))
            start_game(False)
    elif y > x:
        print('The dealer has a higher score than you. You lose.')
        print(declaration(player_hand, comp_hand, True))
        start_game(False)
    elif y < 17:
        comp_hand.append(r.choice(cards))
        dealer_q(player_hand, comp_hand)
    elif y == x:
        print('You got the same score as the dealer. You draw.')
        print(declaration(player_hand, comp_hand, True))
    else:
        print('You have a higher score than the dealer. You win!')
        print(declaration(player_hand, comp_hand, True))
        start_game(False)


def calculate_score(player_hand, comp_hand):
    """Calculates the players score to see if they have gone over 21 and lost"""

    if sum(player_hand) > 21:
        if 11 in player_hand:
            x = player_hand.index(11)
            player_hand[x] = 1
            calculate_score(player_hand, comp_hand)
        else:
            print('You went over 21 and lost')
            print(declaration(player_hand, comp_hand, True))
            start_game(False)
    elif player_hand == 21:
        print(declaration(player_hand, comp_hand, False))
        dealer_q(player_hand, comp_hand)
    else:
        print(declaration(player_hand, comp_hand, False))
        card_q(player_hand, comp_hand)


def card_q(player_hand, comp_hand):
    """Transitions the player into another question or the end of the game"""

    more_cards = input('Would you like to Hit or Stand? Type "Hit" or "Stand": ')

    if more_cards.upper() == 'HIT':
        player_hand.append(r.choice(cards))
        calculate_score(player_hand, comp_hand)
    elif more_cards.upper() == 'STAND':
        dealer_q(player_hand, comp_hand)
    else:
        print('Please enter "Hit" or "Stand"')
        card_q(player_hand, comp_hand)
