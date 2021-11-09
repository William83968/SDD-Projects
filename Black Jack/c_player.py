from deck import Deck
from game import Game

class AI():
    def __init__(self, cards):
        self.choice = 'stand'
        self.chip_worth = 500
        self.chip_num = 2
        self.bet = self.chip_num * self.chip_worth
        self.winning = False
        self.l_times = 0
        self.w_times = 0
    
    def calc_sum(self, cards):
        for i in cards:
            if i in 'JQK':
                cards[i] = 10
                

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

    

    
        
    # def make_choice(self):
            

