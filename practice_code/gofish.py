from deck import deck
from player import player

discard_pile = deck(True)
draw_pile = deck(True)

draw_pile.fan()
discard_pile.fan()

playercount = int(input("how many people are playing?"))
players = {}
for current_player in range(playercount):
    players[input("enter your name")] = player()

for current_player in players:
    print("It is your turn " + current_player)
    print("Which player would you like to ask?")
    print(players)
    their_pick = input(">")
    if their_pick != current_player:
        print("What card would you like ask for")
    else:
        print("You can't pick yourself you idiot")
        
