import random
players = {}

print("Please enter in your name, player1")
player1 = input(">")
players[player1] = 0

print("Please enter in your name, player2")
player2 = input(">")
players[player2] = 0

print(player1 + "please roll")
rollp1 = random.randint(1,6)
print("Your roll is" + str(rollp1))

print(player2 + "please roll")
rollp2 = random.randint(1,6)
print("Your roll is " + str(rollp2))
if (rollp1 > rollp2):
    players[player1] +=1
    print("Player1 won the round")
elif (rollp2 > rollp1):
    players[player2] +=1
    print("Player2 won the round")
elif (rollp1 == rollp2):
    print("It's a tie, roll again")

