'''Program for playing BlackJack/21 using Python'''

import random as r
import game_funcs as gf

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

switcher = True
counter = 0

while switcher == True:

    play_game = input('Do you want to play a game of Black Jack? Type "y" or "n" : ')

    if play_game == 'y':
        if counter < 1:
            counter += 1
            print(logo)
            pc1, pc2 = r.choice(gf.cards), r.choice(gf.cards)
            cc1, cc2 = r.choice(gf.cards), r.choice(gf.cards)
            p_cards = [pc1, pc2]
            c_cards = [cc1, cc2]
            print(gf.help_me(p_cards, c_cards))
        else:
            pc1, pc2 = r.choice(gf.cards), r.choice(gf.cards)
            cc1, cc2 = r.choice(gf.cards), r.choice(gf.cards)
            p_cards = [pc1, pc2]
            c_cards = [cc1, cc2]
            print(gf.help_me(p_cards, c_cards))
    elif play_game == 'n':
        print('Then why did you run the program?')
        switcher = False
    else:
        print('Isn\'t typing "y" or "n" so hard?')