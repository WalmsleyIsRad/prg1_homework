import random
#problem 1

class Dice():
    def __init__(self,max_sides):
        print("How many sides would you like on your dice?")
        self.sides = int(input(">"))

        if(len(sides) > 10 and len(sides) < 4):
            print("Too many sides, try again")
        else:
            print("We can use this dice")
        list_of_dice = [self.sides]
        
        self.max_values = list(self.sides)
        count = 0
        self.current_value = self.max_values[0]
        for x in self.max_values:
            if(x < current_value):
                x = current_value
        self.current_value = side_up

        self.side_up = max_sides
    
    def roll(self,max_sides):
        self.random_number = random.randint(0,max_sides)
        self.side_up = self.random_number

#problem 2
class Player():
    def __init__(self):
        print("Please enter in your name")
        self.new_player = input(">")
        players = {}
        self.new_players = players.append(self.new_player = "0")

    def display_status(self):
        print(players)

    def take_turn(self,max_sides):
        roll(sides) = list(sum_of_sides_up)

        count = 0
        self.sides = sum_of_sides_up[0]
        for self.sides in sum_of_sides_up:
            if(count < sides):
                self.sides += 1
                count +=1
        return sides

#problem 3
class Game():
    def __init__(self):
        max_score = 3
        Dice()

        



        
        
