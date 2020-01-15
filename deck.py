from random import *

class Deck:
    def __init__(self,deck):
        self.deck = deck
    #function to append a single card into a specific list and removing the card from the deck
    def deal_card(self,slot):
        rand_card = randint(0, len(self.deck) -1)
        slot.append(self.deck[rand_card])
        self.deck.pop(rand_card)
    #function to deal 2 cards immediately at the start of the game
    def initial_deal(self, playercards):
        for i in range(2):
            self.deal_card(playercards)