from deck import Deck

class AI():
    def __init__(self):
        self.choice = 'stand'
        self.status = 'neutral'
        self.number = 0
        self.cards = []
        self.ranks = []
        self.value = 0
    
    def calc_hand(self, hand):
        sum = 0
        for i in range(len(hand)):
            self.rank = list(hand[i])[-1]
            if self.rank == '0':
                self.ranks.append('10')
            else:
                self.ranks.append(self.rank)


        non_aces = [card for card in self.ranks if card != 'A']
        aces = [card for card in self.ranks if card == 'A']

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

        self.ranks = []
        return sum


    def make_choice(self):
        self.value = self.calc_hand(self.cards)
        if self.value > 17:
            self.choice = 'Stand'
        else:
            self.choice = 'Hit'
        return self.choice
    
    def check_win(self, dealer, first_hand):
        if self.value == 21 and first_hand == True:
            self.status = 'Blackjack'

        if not first_hand:
            if self.value < dealer:
                self.status = 'Lose'
            elif self.value > dealer:
                self.status = 'Win'
            else:
                self.status = 'Draw'

        return self.status

    


    # def sort(self, arr):
    #     while True:
    #         corrected = False
    #         for i in range(0, len(arr) - 1):
    #             if arr[i] > arr[i+1]:
    #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #                 corrected = True
    #         if not corrected:
    #             return arr

    # def binary_search(self, target):
    #     arr = self.sort(self.cards)
    #     if len(arr) == 0:
    #         return - 1
    #     left, right = 0, len(arr) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target:
    #             return mid
    #         elif arr[mid] > target:
    #             left += 1
    #         elif arr[mid] < target:
    #             right += 1
    #     return - 1
    
    
        

