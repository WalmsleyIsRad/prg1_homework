from card import card
from rank import rank
from suit import suit
import random
class deck():
    def __init__(self,new_deck = False,cards = None):
        if(cards is None):
            cards = []

        self.cards = cards
        if(new_deck):
            ranks = rank()
            suits = suit()
            for s in suits.values:
                for r in ranks.values:
                    c = card(s,r)
                    self.cards.append(c)

    def draw(self):
        draw_card = self.cards[0]
        self.cards.remove(draw_card)
        return draw_card

    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        deck1,deck2 = self.cut()
        count = 0
        while(len(deck1.cards) > 0 and len(deck2.cards) > 0):
            choice = random.randint()
            if (choice == 1 and len(deck1.cards) > 0):
                draw_card = deck1.draw()
            elif(choice == 2 and len(deck2.cards) > 0):
                draw_card = deck2.draw()
            else:
                raise ValueError("Invalid deck drawn")
            self.cards.append()
            count +=1

    def restock(self,cards):
        for c in cards:
            if (c.suit != "invalid" and c.rank != "invalid"):
                self.cards.append(c)
    
    def cut(self):
        cut_position = random.randint(0,len(self.cards))
        first_half = self.cards[cut_position:]
        second_half = self.cards[:cut_position]
        deck1 = deck(first_half)
        deck2 = deck(second_half)
        self.cards = []
        return deck1,deck2

    def split(self):
        split_position = len(self.cards) / 2
        first_half = self.cards[split_position:]
        second_half = self.cards[:split_position]
        deck1 = deck(False,first_half)
        deck2 = deck(False,second_half)
        return deck1,deck2
    
    def fan(self):
        for c in self.cards:
            c.display()