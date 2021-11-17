from deck import Deck
from player import Player
import c_player
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
        self.c_players = []
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
        for i in range(2):
            self.player.append(deck.cards.pop())
            self.dealer.append(deck.cards.pop())

    def setup_players(self, num):
        for _ in range(num):
            self.c_players.append(c_player.AI())

        for i in range(len(self.c_players)):
            self.c_players[i].number = i+1


    def c_player_dealing(self):
        for c_player in self.c_players:
            for i in range(2):
                c_player.cards.append(deck.cards.pop())
            
    def c_choices(self):
        for i in self.c_players:
            choice = i.make_choice()
            

    def reset(self, result):
        deck.new()
        self.player = []
        self.dealer = []
        self.values = []
        self.first_hand = True
        self.standing = False
        if result == 'Lost':
            player.lose()
        elif result == 'Win':
            player.win()
        for i in self.c_players:
            i.cards = []

        
    def calc_hand(self, hand):
        sum = 0
        for i in range(len(hand)):
            value = list(hand[i])[-1]
            if value == '0':
                value = '10'
            self.values.append(value)

        non_aces = [card for card in self.values if card != 'A']
        aces = [card for card in self.values if card == 'A']

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

if __name__ == '__main__':
    g = Game()
    player = Player()
    g.setup_players(2)
    # round_num = 0
    for i in range(10):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            g.shuffle()
            if g.first_hand:
                g.dealing()
                g.c_player_dealing()

            g.player_value = g.calc_hand(g.player)
            g.dealer_value = g.calc_hand(g.dealer)

            if g.standing:
                print('Dealer Cards: [{}] ({})'.format(']['.join(g.dealer), g.dealer_value))
            else:
                print('Dealer Cards: [{}][?]'.format(g.dealer[0]))

            print('Your Cards:   [{}] ({})'.format(']['.join(g.player), g.player_value))
            for i in g.c_players:
                print('Computer Player {}: [{}]'.format(i.number, ']['.join(i.cards)))

            adjusted_score = g.calc_hand(g.player)
            if adjusted_score != g.player_value:
                print('Your adjusted score: ({})'.format(g.player_value))
            print('')

            if g.standing:
                if g.dealer_value > 21:
                    print('Dealer busted, you win!')
                    player.win()
                    player.show_bet()
                elif g.player_value == g.dealer_value:
                    print('Push, nobody wins')
                    player.show_bet()
                elif g.player_value > g.dealer_value:
                    print('You beat the dealer, you win!')
                    player.win()
                    player.show_bet()
                else:
                    player.lose()
                    player.show_bet()
                    print('You lose :(')

                print('')
                time.sleep(g.sleep_time)
                break

            if g.first_hand and g.player_value == 21:
                print('Blackjack! Nice!')
                print('')
                player.win()
                player.show_bet()
                time.sleep(g.sleep_time)
                break

            if g.player_value > 21:
                print('You busted!')
                print('')
                player.lose()
                player.show_bet()
                time.sleep(g.sleep_time)
                break

            g.c_choices()
            for c_player in g.c_players:
                print('Computer Player {}: {}'.format(c_player.number, c_player.choice))
            print('')

            print('What would you like to do?')
            print(' [1] Hit')
            print(' [2] Stand')

            print('')
            choice = input('Your choice: ')
            print('')

            # if g.first_hand:
            #     bet_choice = input("Increase your bet? [1] for YES and [2] for NO\n")
            #     if bet_choice == '1':
            #         chip_choice = input("Raise chip worth or add more chips? [1] for RAISE and [2] for ADD\n")
            #         if chip_choice == '1':
            #             percentage = input("In what percentage? (Enter a integer e.g 20)\n")
            #             player.incease_chip_worth(percentage)
            #         else:
            #             amount = input("How many chips do you want to add?(Enter a integer e.g 1)\n")
            #             player.add_chips(amount)
            #     player.show_bet()
            #     time.sleep(g.sleep_time)

            g.first_hand = False

            if choice == '1':
                g.player.append(deck.cards.pop())
            elif choice == '2':
                g.standing = True
                while g.calc_hand(g.dealer) <= 16:
                    g.dealer.append(deck.cards.pop())

            for c_player in g.c_players:
                if c_player.choice == 'Hit':
                    c_player.cards.append(deck.cards.pop())
            
            for c_player in g.c_players:
                c_result = c_player.check_win(g.dealer_value, g.first_hand)
                print("Computer Player{}'s result: {}".format(c_player.number, c_player.status))
            time.sleep(g.sleep_time)

        g.reset('0')

            
        
