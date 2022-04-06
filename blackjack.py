'''Program for playing BlackJack/21 using Python'''

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

play_game = input('Do you want to play a game of Black Jack? Type "y" or "n" : ')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

new_card = r.choice(cards)

def declaration(player_cards, computer_cards):

   return f'Your final hand: {player_cards}, Final score: {sum(player_cards)} \n \
        Computer\'s final hand: {computer_cards}, Final score: {sum(computer_cards)} \n'

def dealer_turn(player_cards, computer_cards):
    x = sum(player_cards)
    if sum(computer_cards) > x:
        print(declaration(player_cards, computer_cards) + 'The computer has a higher score than you. You lose.')
    elif sum(computer_cards) >= 17 and sum(computer_cards) == x:
        print(declaration(player_cards, computer_cards) + 'You have the same score as the dealer. You tied.')
    elif sum(computer_cards) >= 17:
        print(declaration(player_cards, computer_cards) + 'You have a higher score than the computer. You win!')
    elif sum(computer_cards) < 17:
        new_computer_cards = list(computer_cards)
        new_computer_cards.append(r.choice(cards))
        return dealer_turn(player_cards, new_computer_cards)

def more_cards(player_cards, computer_cards):
    decision = input('Type "y" for another card, type "n" to stand: ')
    if decision == 'y':
        new_player_cards = list(player_cards)
        new_player_cards.append(r.choice(cards))
        return help_me(new_player_cards, computer_cards)
    elif decision == 'n':
        return dealer_turn(player_cards, computer_cards)


def help_me(player_cards, computer_cards):
    if sum(player_cards) > 21:
        if 11 not in player_cards:
            print(declaration(player_cards, computer_cards) + 'You went over. You lose.')
        else:
            x = player_cards.index(11)
            new_player_cards = list(player_cards)
            new_player_cards[x] = 1
            return help_me(new_player_cards, computer_cards)
    elif sum(player_cards) == 21:
        if sum(computer_cards) == 21:
            print(declaration(player_cards, computer_cards) + 'You both got 21. You tied')
        elif sum(computer_cards) >= 17:
            print(declaration(player_cards, computer_cards) + 'You have a higher score than the dealer. You win!')
        elif sum(computer_cards) < 17:
            new_computer_cards = list(computer_cards)
            new_computer_cards.append(r.choice(cards))
            return help_me(player_cards, new_computer_cards)
    elif sum(player_cards) < 21:
        print(f'Your current hand: {player_cards}, Your current score: {sum(player_cards)} \n \
        Computer\'s first card: {computer_cards[0]} \n')
        more_cards(player_cards, computer_cards)
        

if play_game == 'y':
    print(logo)
    pc1, pc2 = r.choice(cards), r.choice(cards)
    cc1, cc2 = r.choice(cards), r.choice(cards)
    p_cards = [pc1, pc2]
    c_cards = [cc1, cc2]
    print(help_me(p_cards, c_cards))
elif play_game == 'n':
    print('Then why did you run the program?')
else:
    print('Isn\'t typing "y" or "n" so hard?')