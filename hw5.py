import random
players = {}

print("Please enter in your name, player1")
player1 = input(">")
players[player1] = 0

print("Please enter in your name, player2")
player2 = input(">")
players[player2] = 0

max_score = 2
while(players[player1] < max_score and players[player2] < max_score):
    print(player1 + " please roll by pressing enter")
    rollp1 = input("")
    rollp1 = random.randint(1,6)
    print("Your roll is " + str(rollp1))

    print(player2 + " please roll by pressing enter")
    rollp2 = input("")
    rollp2 = random.randint(1,6)
    print("Your roll is " + str(rollp2))

    if (rollp1 > rollp2):
        players[player1] +=1
        print(str(player1) + " won the round")
        print("Your score is " + str(players[player1]))
    elif (rollp2 > rollp1):
        players[player2] +=1
        print(str(player2) + " won the round")
        print("Your score is " + str(players[player2]))
    else:
        print("It's a tie, roll again")
    
    if(players[player1] < max_score and players[player2] < max_score):
        print(str(player1) + " please decide if you want to continue playing. Input 1 for yes and 2 for no")
        pgp1 = int(input(""))
        print(str(player2) + " please decide if you want to continue playing. Input 1 for yes and 2 for no")
        pgp2 = int(input(""))
        if(pgp1 == 1 and pgp2 == 1):
            max_score = max_score + 2



