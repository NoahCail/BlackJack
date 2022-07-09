"""Python Module containing all the main functions needed for the overall BlackJack program"""

# TODO: Add in functionality for doubling down and splitting on pairs & insurance on dealer aces
# TODO: Add in functionality for there to be a player and a balance. Also can decide how much to bet each hand

import random as r
import money as m

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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Returns the current scores and hands
def current_dec(player_hand, comp_hand):
    """Returns the current player and computer hands as well as their current scores"""

    return f'Your current hand: {player_hand}, Current score: {sum(player_hand)} \n \
            Computer\'s current hand: {comp_hand[1:]}, Current score: ? \n'


# Returns the final scores and hands
def final_dec(player_hand, comp_hand):
    """Returns the final player and computer hands as well as their final scores"""

    return f'Your final hand: {player_hand}, Final score: {sum(player_hand)} \n \
    Computer\'s final hand: {comp_hand}, Final score: {sum(comp_hand)} \n'


def start_game(player):
    """Starts the initial black jack game"""

    answer = input('Would you like to play a game of Black Jack? Type "y" for Yes and "n" for No: ')
    if answer.upper() == 'Y':
        bet = input('How much would you like to wager?: ')
        if bet > player.balance:
            print(f'You don\'t that much in your balance. Please make a wager of {player.balance} or lower')
            start_game(player)
        else:
            p_hand, c_hand = ([r.choice(cards), r.choice(cards)], [r.choice(cards), r.choice(cards)])
            print(current_dec(p_hand, c_hand))
            card_q(p_hand, c_hand, player, bet)
    elif answer.upper() == 'N':
        print('Then why did you start the program in the first place?')
    else:
        print('Isn\'t it so tough to type a y or an n, no but seriously figure it out')
        start_game(player)


def restart_game():
    """Restarts the black jack game after one of the outcomes is reached"""

    answer = input('Would you like to play a game of Black Jack? Type "y" for Yes and "n" for No: ')
    if answer.upper() == 'Y':
        p_hand, c_hand = ([r.choice(cards), r.choice(cards)], [r.choice(cards), r.choice(cards)])
        print(current_dec(p_hand, c_hand))
        card_q(p_hand, c_hand)
    elif answer.upper() == 'N':
        print('Thanks for playing!')
    else:
        print('Isn\'t it so tough to type a y or an n, no but seriously figure it out')
        restart_game()


def dealer_q(player_hand, comp_hand):
    """Handles the dealers turn once the player is at 21 or has chosen to stand and returns the results of the game"""
    x, y = sum(player_hand), sum(comp_hand)

    if x > 21:
        print(f'You went over 21. You lose. \n {final_dec(player_hand, comp_hand)}')
        restart_game()
    elif y > 21:
        if 11 in comp_hand and y < 31:
            x = comp_hand.index(11)
            comp_hand[x] = 1
            dealer_q(player_hand, comp_hand)
        else:
            print(f'The computer went over. You win! \n {final_dec(player_hand, comp_hand)}')
            restart_game()
    elif y > x:
        print(f'The dealer has a higher score than you. You lose. \n {final_dec(player_hand, comp_hand)}')
        restart_game()
    elif y < 17:
        comp_hand.append(r.choice(cards))
        dealer_q(player_hand, comp_hand)
    elif y == x:
        print(f'You got the same score as the dealer. You draw. \n {final_dec(player_hand, comp_hand)}')
        restart_game()
    else:
        print(f'You have a higher score than the dealer. You win! \n {final_dec(player_hand, comp_hand)}')
        restart_game()


def calculate_score(player_hand, comp_hand, bet):
    """Calculates the players score to see if they have gone over 21 and lost"""

    if sum(player_hand) > 21:
        if 11 in player_hand:
            x = player_hand.index(11)
            player_hand[x] = 1
            calculate_score(player_hand, comp_hand, bet)
        else:
            print('You went over 21 and lost')
            print(final_dec(player_hand, comp_hand, bet))

            restart_game()
    elif player_hand == 21:
        print(current_dec(player_hand, comp_hand))
        dealer_q(player_hand, comp_hand)
    else:
        print(current_dec(player_hand, comp_hand))
        card_q(player_hand, comp_hand)


def card_q(player_hand, comp_hand, bet):
    """Transitions the player into another question or the end of the game"""

    more_cards = input('Would you like to Hit or Stand? Type "Hit" or "Stand": ')

    if more_cards.upper() == 'HIT':
        player_hand.append(r.choice(cards))
        calculate_score(player_hand, comp_hand, bet)
    elif more_cards.upper() == 'STAND':
        dealer_q(player_hand, comp_hand, bet)
    else:
        print('Please enter "Hit" or "Stand"')
        card_q(player_hand, comp_hand, bet)
