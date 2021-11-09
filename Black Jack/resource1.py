import random

def get_shuffled_deck():
    # suits = ['♣', '♠', '♦', '♥']
    suits = ['clubs', 'spades', 'diamonds', 'hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(suit + ' ' + rank)
    random.shuffle(deck)
    return deck

def deal_card(deck, participant):
    card = deck.pop()
    participant.append(card)
    return card

def compute_total(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8':8, \
               '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    result = 0
    numAces = 0

    for card in hand:
        result += values[card[:-1]]
        if card[2] == 'A':
            numAces += 1
    
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1
    return result

def print_hand(hand):
    for card in hand:
        print(card, end = '')
    print()

# def blackjack():
#     deck = get_shuffled_deck()
#     house = []
#     player = []

#     for i in range(2):
#         deal_card(deck, player)
#         deal_card(deck, house)

#     print('Dealer card:', end = ''); print_hand(house)
#     print('Player card:', end = ''); print_hand(player)

#     answer = input('Hit? [Y] for Yes and [N] for No ')
#     print('Default: Yes')
#     while answer in ('', 'y', 'Y'):
#         card = deal_card(deck, player)
#         print('Player cards: ', end = ''); print_hand(player)
#         if compute_total(player) > 21:
#             print('Busted! Player Lose!')
#             return
#         answer = input('Hit? [Y] for Yes and [N] for No ')

#     while compute_total(house) < 17:
#         card = deal_card(deck, house)
#         print('Dealer cards: ', end = ''); print_hand(house)
#         if compute_total(house) > 21:
#             print('Busted! Player Lose!')
#             return

#     houseTotal, playerTotal = compute_total(house), compute_total(player)
#     if houseTotal > playerTotal:
#         print('Dealer Win!')
#     elif houseTotal < playerTotal:
#         print('Player Win! ')
#     elif houseTotal == 21 and 2 == len(house) < len(player):
#         print('Dealer Win!')
#     elif playerTotal == 21 and 2 == len(player) < len(house):
#         print('Player Win!')
#     else:
#         print('Draw!')

if __name__ == '__main__':
    # blackjack()
    pass

    