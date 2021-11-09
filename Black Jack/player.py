import random

class Player:
    def __init__(self):
        self.chip_worth = 50
        self.chip_num = 0
        self.max_chips = 10
        self.bet = 0
        self.status = 'Waiting'
        self.l_times = 0
        self.w_times = 0

    def place_bets(self, chip_worth):
        self.chip_num += 1
        self.chip_worth = chip_worth
        self.bet = self.chip_num * chip_worth

    def incease_chip_worth(self, increase_amount):
        increase_amount = int(increase_amount)
        if increase_amount > 0 and increase_amount <= 100:
            self.chip_worth *= int(increase_amount / 100)
        else:
            self.chip_worth = int(self.chip_worth * 0.5)
        self.bet = self.chip_num * self.chip_worth
    
    def add_chips(self, inc_num):
        inc_num = int(inc_num)
        if self.chip_num + int(inc_num) > self.max_chips:
            print("You can't have that many chips")
        else:
            self.chip_num += int(inc_num)
            self.bet = self.chip_num * self.chip_worth
    
    def reset(self):
        self.chip_num = 0
        self.chip_worth = 50
        self.bet = self.chip_num * self.chip_worth
        
    def lose(self):
        self.bet -= self.chip_worth * 3
        self.l_times += 1
        
    def win(self):
        won_amount = random.randint(2, 10)
        if self.bet <= 0:
            self.bet += won_amount * 500
        else:
            self.bet += won_amount * self.chip_worth
        self.w_times += 1

    # def show_bet(self):
    #     if self.bet > 0:
    #         print('Your current bet: ${}'.format(self.bet))
    #     else:
    #         print('Your current bet: -${}'.format(self.bet*-1))

    
    

    