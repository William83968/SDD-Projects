from deck import Deck
from player import Player
import random
import time
import os

deck = Deck()
random.seed(int(time.time()))
player = Player()

class Game():
    def __init__(self):
        self.player = []
        self.dealer = []
        self.values = []
        self.standing = False
        self.first_hand = True
        self.player_score = 0
        self.dealer_score = 0
        self.player_values = 0
        self.dealer_values = 0
        # keeping record of what round
        self.rounds = 0
        # make sure there's enough time for the player to read the outcome
        self.sleep_time = 1.0

    def shuffle(self):
        deck.sampling(deck.cards)

    def dealing(self):
        self.player.append(deck.cards.pop())
        self.dealer.append(deck.cards.pop())
        self.player.append(deck.cards.pop())
        self.dealer.append(deck.cards.pop())
        print(self.player)
        print(self.dealer)

    def reset(self, result):
        deck.new()
        player.reset()
        self.player = []
        self.dealer = []
        self.values = []
        self.first_hand = True
        self.standing = False
        if result == 'Lost':
            player.lose()
        elif result == 'Win':
            player.win()

        
    def calc_hand(self, hand, auto_ace):
        sum = 0
        for i in range(len(hand)):
            value = list(hand[i])[-1]
            if value == '0':
                value = '10'
            self.values.append(value)

        non_aces = [card for card in self.values if card != 'A']
        aces = [card for card in self.values if card == 'A']
        contain_ace = False

        if aces:
            contain_ace = True

        for card in non_aces:
            if card in 'JQK':
                sum += 10
            else:
                sum += int(card)

        for card in aces:
            if sum <= 10:
                sum += 11
            else:
                sum += 1

        self.values = []
        return sum

# g = Game()
# for i in range(10):
#     g.shuffle()
#     g.dealing()
#     g.calc_hand(g.player, True)
#     g.reset()

# if __name__ == '__main__':
#     g = Game()
#     player = Player()
#     # round_num = 0
#     for i in range(10):
#         while True:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print(deck.cards)
#             g.shuffle()
#             if g.first_hand:
#                 g.dealing()

#             g.player_score = g.calc_hand(g.player, True)
#             g.dealer_score = g.calc_hand(g.dealer, True)

#             if g.standing:
#                 print('Dealer Cards: [{}] ({})'.format(']['.join(g.dealer), g.dealer_score))
#             else:
#                 print('Dealer Cards: [{}][?]'.format(g.dealer[0]))

#             print('Your Cards:   [{}] ({})'.format(']['.join(g.player), g.player_score))

#             adjusted_score = g.calc_hand(g.player, False)
#             if adjusted_score != g.player_score:
#                 print('Your adjusted score: ({})'.format(g.player_score))
#             print('')

#             if g.standing:
#                 if g.dealer_score > 21:
#                     print('Dealer busted, you win!')
#                     player.win()
#                     player.show_bet()
#                 elif g.player_score == g.dealer_score:
#                     print('Push, nobody wins')
#                     player.show_bet()
#                 elif g.player_score > g.dealer_score:
#                     print('You beat the dealer, you win!')
#                     player.win()
#                     player.show_bet()
#                 else:
#                     player.lose()
#                     player.show_bet()
#                     print('You lose :(')

#                 print('')
#                 time.sleep(g.sleep_time)
#                 break

#             if g.first_hand and g.player_score == 21:
#                 print('Blackjack! Nice!')
#                 print('')
#                 player.win()
#                 player.show_bet()
#                 time.sleep(g.sleep_time)
#                 break

#             if g.player_score > 21:
#                 print('You busted!')
#                 print('')
#                 player.lose()
#                 player.show_bet()
#                 time.sleep(g.sleep_time)
#                 break

#             print('What would you like to do?')
#             print(' [1] Hit')
#             print(' [2] Stand')

#             print('')
#             choice = input('Your choice: ')
#             print('')

#             if g.first_hand:
#                 bet_choice = input("Increase your bet? [1] for YES and [2] for NO\n")
#                 if bet_choice == '1':
#                     chip_choice = input("Raise chip worth or add more chips? [1] for RAISE and [2] for ADD\n")
#                     if chip_choice == '1':
#                         percentage = input("In what percentage? (Enter a integer e.g 20)\n")
#                         player.incease_chip_worth(percentage)
#                     else:
#                         amount = input("How many chips do you want to add?(Enter a integer e.g 1)\n")
#                         player.add_chips(amount)
#                 player.show_bet()
#                 time.sleep(g.sleep_time)

#             g.first_hand = False

#             if choice == '1':
#                 g.player.append(deck.cards.pop())
#             elif choice == '2':
#                 g.standing = True
#                 while g.calc_hand(g.dealer, True) <= 16:
#                     g.dealer.append(deck.cards.pop())
#         g.reset()

            
        
