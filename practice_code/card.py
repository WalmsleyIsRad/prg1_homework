from rank import rank
from suit import suit

class card():
    def __init__(self,p_suit,p_rank):
        r = rank()
        valid_rank = r.validate(p_rank)

        s = suit()
        valid_suit = s.validate(p_suit)

        if(valid_rank and valid_suit):
            self.suit = p_suit
            self.rank = p_rank
        else:
            raise ValueError("Invalid Rank or Suit")

    def display(self):
        print(self.rank + " of " + self.suit)
