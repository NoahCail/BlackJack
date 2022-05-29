# TODO: Add in functionality for doubling down and splitting on pairs
# TODO: Add in functionality for there to be a player and a balance. Also can decide how much to bet each hand
#
# def dealer_turn(player_cards, computer_cards):
#     x = sum(player_cards)
#     if sum(computer_cards) > x and sum(computer_cards) < 22:
#         print(declaration(player_cards, computer_cards) + 'The computer has a higher score than you. You lose.')
#     elif sum(computer_cards) >= 17 and sum(computer_cards) == x:
#         print(declaration(player_cards, computer_cards) + 'You have the same score as the dealer. You tied.')
#     elif sum(computer_cards) >= 17:
#         print(declaration(player_cards, computer_cards) + 'You have a higher score than the computer. You win!')
#     elif sum(computer_cards) < 17:
#         new_computer_cards = list(computer_cards)
#         new_computer_cards.append(r.choice(cards))
#         return dealer_turn(player_cards, new_computer_cards)
#
# def more_cards(player_cards, computer_cards):
#     decision = input('Type "y" for another card, type "n" to stand: ')
#     if decision == 'y':
#         new_player_cards = list(player_cards)
#         new_player_cards.append(r.choice(cards))
#         return help_me(new_player_cards, computer_cards)
#     elif decision == 'n':
#         return dealer_turn(player_cards, computer_cards)
#
#
# def help_me(player_cards, computer_cards):
#     if sum(player_cards) > 21:
#         if 11 not in player_cards:
#             print(declaration(player_cards, computer_cards) + 'You went over. You lose.')
#         else:
#             x = player_cards.index(11)
#             new_player_cards = list(player_cards)
#             new_player_cards[x] = 1
#             return help_me(new_player_cards, computer_cards)
#     elif sum(player_cards) == 21:
#         if sum(computer_cards) == 21:
#             print(declaration(player_cards, computer_cards) + 'You both got 21. You tied')
#         elif sum(computer_cards) >= 17:
#             print(declaration(player_cards, computer_cards) + 'You have a higher score than the dealer. You win!')
#         elif sum(computer_cards) < 17:
#             new_computer_cards = list(computer_cards)
#             new_computer_cards.append(r.choice(cards))
#             return help_me(player_cards, new_computer_cards)
#     elif sum(player_cards) < 21:
#         print(f'Your current hand: {player_cards}, Your current score: {sum(player_cards)} \n \
#         Computer\'s first card: {computer_cards[0]} \n')
#         more_cards(player_cards, computer_cards)
#
# switcher = True
# counter = 0


#  ----------------------------------------------- Real Code --------------------------------------------------
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
        Computer\'s current hand: {comp_hand}, Current score: {sum(comp_hand)} \n'


def deal_cards():
    """Returns the initial hands of both the player and the """

    pc1, pc2 = r.choice(cards), r.choice(cards)
    cc1, cc2 = r.choice(cards), r.choice(cards)
    p_cards = [pc1, pc2]
    c_cards = [cc1, cc2]

    return [p_cards, c_cards]



def card_q(player_hand):
    """Transitions the player into another question or the end of the game"""

    more_cards = input('Would you like to Hit or Stand? Type "Hit" or "Stand": ')

    if more_cards.upper() == 'HIT':
        player_hand.append(r.choice(cards))


def calculate_score(player_hand, comp_hand):
    """Calculates the players score to see if they have gone over 21 and lost"""

    if sum(player_hand) > 21:
        if 11 in player_hand:
            x = player_hand.index(11)
            player_hand[x] = 1
            calculate_score(player_hand)
        else:
            print('You went over 21 and lost')
            print(declaration(player_hand, comp_hand, True))
            start_game(False)
    elif player_hand == 21:
        print(declaration(player_hand, comp_hand, False))
        dealer_q(player_hand, comp_hand)


def dealer_q(player_hand, comp_hand):
    """Handles the dealers turn once the player is at 21 or has chosen to stand and returns the results of the game"""






def start_game(first):
    answer = input('Would you like to play a game of Black Jack? Type "y" for Yes and "n" for No: ')
    if answer == 'y':
        if first:
            print(logo)
            p_hand, c_hand = deal_cards()
            print(declaration(p_hand, c_hand, False))
            card_q()
        else:
            p_hand, c_hand = deal_cards()
            print(declaration(p_hand, c_hand, False))
            card_q()
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



#  ----------------------------------------------- Real Code --------------------------------------------------

#
# while switcher == True:
#
#     play_game = input('Do you want to play a game of Black Jack? Type "y" or "n" : ')
#
#     if play_game == 'y':
#         if counter < 1:
#             counter += 1
#             print(logo)
#             pc1, pc2 = r.choice(gf.cards), r.choice(gf.cards)
#             cc1, cc2 = r.choice(gf.cards), r.choice(gf.cards)
#             p_cards = [pc1, pc2]
#             c_cards = [cc1, cc2]
#             print(gf.help_me(p_cards, c_cards))
#         else:
#             pc1, pc2 = r.choice(gf.cards), r.choice(gf.cards)
#             cc1, cc2 = r.choice(gf.cards), r.choice(gf.cards)
#             p_cards = [pc1, pc2]
#             c_cards = [cc1, cc2]
#             print(gf.help_me(p_cards, c_cards))
#     elif play_game == 'n':
#         print('Then why did you run the program?')
#         switcher = False
#     else:
#         print('Isn\'t typing "y" or "n" so hard?')
