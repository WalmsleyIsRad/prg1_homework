from deck import deck
from card import card
class player():
    def __init__(self):
        self.score = 0
        self.hand = deck()

    def draw_card(self,draw_pile,):
        card = draw_pile.draw()
        self.hand.add_card(card)

    def ask_card(self,opponent_deck,draw_pile,card):
        card_found = False
        for opponent_card in opponent_deck.cards:
            if(opponent_card == card):
                self.hand.add_card(opponent_card)
                opponent_deck.deck.remove(opponent_card)
                card_found = True
        if(card_found == False):
            self.draw_card(draw_pile)

    def increase_score(self,discard_deck):
        pass