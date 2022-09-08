"""Python Module containing all the main functions needed for the overall BlackJack program"""

# TODO: Add in functionality for doubling down and splitting on pairs & insurance on dealer aces
# TODO: Add in functionality for there to be a player and a balance. Also can decide how much to bet each hand
# TODO: Learn how to save players and their names and balances somewhere so that it can be recalled if someone wants to load an old game

import random as r
import money as m

LOGO = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Returns the current scores and hands
def current_dec(player_hand, comp_hand):
    """Returns the current player and computer hands as well as their current scores"""

    return f'Your current hand: {player_hand}, Current score: {sum(player_hand)} \n \
    Computer\'s current hand: {comp_hand[1:]}, Current score: ? \n'


# Returns the final scores and hands
def final_dec(player_hand, comp_hand, player, bet):
    """Returns the final player and computer hands as well as their final scores"""

    return f'Your final hand: {player_hand}, Final score: {sum(player_hand)} \n \
    Computer\'s final hand: {comp_hand}, Final score: {sum(comp_hand)} \n \
    Current Balance: ${player.balance}, Last Bet: ${bet}'

# Function that initially starts the game by producing the logo and requesting player info before kickogg
def start_game():
    """Starts the initial black jack game"""

    print(LOGO)

    player = m.player_setup()

    answer = input(f'Would you like to play a game of Black Jack, {player.name}? Type "y" for Yes and "n" for No: ')
    if answer.upper() == 'Y':
        bet = int(input(f'Balance: ${player.balance} \nHow much would you like to wager, {player.name}?: '))
        if bet > player.balance:
            print(f'You don\'t have that much in your balance. Please make a wager of {player.balance} or lower')
            restart_game(player)
        elif bet < 0.01:
            print(f'Well that just don\'t make no sense {player.name}. Please make a wager of $0.01 or more')
            restart_game(player)
        else:
            player.balance -= bet
            p_hand, c_hand = ([r.choice(CARDS), r.choice(CARDS)], [r.choice(CARDS), r.choice(CARDS)])
            print(current_dec(p_hand, c_hand))
            card_q(p_hand, c_hand, player, bet)
    elif answer.upper() == 'N':
        print(f'Then why did you start the program in the first place, {player.name}?')
    else:
        print(f'Isn\'t it so tough to type a y or an n, no but seriously figure it out {player.name}')
        restart_game(player)

# Function to restart the game and maintain the same player throughout
def restart_game(player):
    """Restarts the black jack game after one of the outcomes is reached"""

    answer = input(f'Would you like to play a game of Black Jack, {player.name}? Type "y" for Yes and "n" for No: ')
    if answer.upper() == 'Y':
        bet = int(input(f'Balance: ${player.balance} \nHow much would you like to wager, {player.name}?: '))
        if bet > player.balance:
            print(f'You don\'t have that much in your balance. Please make a wager of {player.balance} or lower')
            restart_game(player)
        elif bet < .01:
            print(f'Well that just don\'t make no sense {player.name}. Please make a wager of $0.01 or more')
            restart_game(player)
        else:
            player.balance -= bet
            p_hand, c_hand = ([r.choice(CARDS), r.choice(CARDS)], [r.choice(CARDS), r.choice(CARDS)])
            print(current_dec(p_hand, c_hand))
            card_q(p_hand, c_hand, player, bet)
    elif answer.upper() == 'N':
        print(f'Thanks for playing, {player.name}!')
    else:
        print(f'Isn\'t it so tough to type a y or an n, no but seriously figure it out {player.name}')
        restart_game(player)


def dealer_q(player_hand, comp_hand, player, bet):
    """Handles the dealers turn once the player is at 21 or has chosen to stand and returns the results of the game"""

    x, y = sum(player_hand), sum(comp_hand)

    if x > 21:
        print(f'You went over 21. You lose. \n {final_dec(player_hand, comp_hand, player, bet)}')
        restart_game(player)
    elif y > 21:
        if 11 in comp_hand and y < 31:
            x = comp_hand.index(11)
            comp_hand[x] = 1
            dealer_q(player_hand, comp_hand, player, bet)
        else:
            player.balance += (bet * 2)
            print(f'The computer went over. You win! \n {final_dec(player_hand, comp_hand, player, bet)}')
            restart_game(player)
    elif y > x:
        print(f'The dealer has a higher score than you. You lose. \n {final_dec(player_hand, comp_hand, player, bet)}')
        restart_game(player)
    elif y < 17:
        comp_hand.append(r.choice(CARDS))
        dealer_q(player_hand, comp_hand, player, bet)
    elif y == x:
        player.balance += bet
        print(f'You got the same score as the dealer. You draw. \n {final_dec(player_hand, comp_hand, player, bet)}')
        restart_game(player)
    else:
        player.balance += (bet * 2)
        print(f'You have a higher score than the dealer. You win! \n {final_dec(player_hand, comp_hand, player, bet)}')
        restart_game(player)


def calculate_score(player_hand, comp_hand, player, bet):
    """Calculates the players score to see if they have gone over 21 and lost"""

    if sum(player_hand) > 21:
        if 11 in player_hand and sum(player_hand) < 31:
            x = player_hand.index(11)
            player_hand[x] = 1
            calculate_score(player_hand, comp_hand, player, bet)
        else:
            print('You went over 21 and lost')
            print(final_dec(player_hand, comp_hand, player, bet))
            restart_game(player)
    elif player_hand == 21:
        print(current_dec(player_hand, comp_hand))
        dealer_q(player_hand, comp_hand, player, bet)
    else:
        print(current_dec(player_hand, comp_hand))
        card_q(player_hand, comp_hand, player, bet)


def card_q(player_hand, comp_hand, player, bet):
    """Transitions the player into another question or the end of the game"""

    more_cards = input('Would you like to Hit or Stand? Type "H" or "S": ')

    if more_cards.upper() == 'HIT':
        player_hand.append(r.choice(CARDS))
        calculate_score(player_hand, comp_hand, player, bet)
    elif more_cards.upper() == 'STAND':
        dealer_q(player_hand, comp_hand, player, bet)
    else:
        print('Please enter "Hit" or "Stand"')
        card_q(player_hand, comp_hand, player, bet)
