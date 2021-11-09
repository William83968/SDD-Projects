import random

class Deck():
    def __init__(self):
        self.shuffled = False
        self.suits = ['clubs', 'spades', 'diamonds', 'hearts']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(suit + rank)

    def sampling(self, cards):
        shuffled_deck = random.sample(cards, len(cards))
        self.cards = shuffled_deck

    def new(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(suit + rank)
        self.sampling(self.cards)
        
# self.cards = [
#             'clubs2', 'clubs3', 'clubs4', 'clubs5', 'clubs6', 'clubs7', 'clubs8', 'clubs9', 'clubs10', 'clubsJ', 'clubsQ', 'clubsK', 'clubsA',
#             'diamonds2', 'diamonds3', 'diamonds4', 'diamonds5', 'diamonds6', 'diamonds7', 'diamonds8', 'diamonds9', 'diamonds10', 'diamondsJ', 'diamondsQ', 'diamondsK', 'diamondsA',
#             'hearts2', 'hearts3', 'hearts4', 'hearts5', 'hearts6', 'hearts7', 'hearts8', 'hearts9', 'hearts10', 'heartsJ', 'heartsQ', 'heartsK', 'heartsA',
#             'spades2', 'spades3', 'spades4', 'spades5', 'spades6', 'spades7', 'spades8', 'spades9', 'spades10', 'spadesJ', 'spadesQ', 'spadesK', 'spadesA'
#         ]
            
        