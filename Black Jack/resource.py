import random
import time

cards = [
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
]


def player_if_ace(player_cards):#判断玩家/庄家手中是否有A牌
    if 11 in player_cards:#假设玩家拿到了A牌（之前我们将A预先设置成了11点）
        if sum(player_cards) > 21:#当玩家的所有手牌相加超过了21点，那自然就要把11点往下降变成1点，从而避免爆牌
            location = player_cards.index(11)#在list中找到玩家的11点所在的位置
            player_cards[location] = 1#找到list中的11点，并替换成1点
            return player_cards#将新的1点返回到玩家手牌中
        else:
            return player_cards#如果手牌相加并没有到21点，则A保持11点
    else:
        return player_cards#如果玩家并没有A，则保持现状


def dealer_control(dealer_cards,player_cards):#庄家的操作
    print('Dealer翻牌了，总和是' + str(sum(dealer_cards)))#显示dealer的手牌之和
    time.sleep(2)#增加体验感，空两秒等待发牌过程:)
    if sum(player_cards) > sum(dealer_cards):#如果开牌没有玩家的手牌之和大，才选择要牌
        while sum(dealer_cards) < 17:#在casino中，庄家在未拿到17点以上的牌时不可停止要牌
            dealer_cards.append(random.choice(cards))#给dealer加牌
            dealer_cards = player_if_ace(dealer_cards)#判断是否有A
            print('Dealer加牌了，拿到一张' + str(dealer_cards[-1]) + '当前Dealer总和是' + str(sum(dealer_cards)))
            time.sleep(2)
            return dealer_cards#返回最新值
    else:
        return dealer_cards#如果开牌直接比选手的大了，那还加啥牌，直接返回值


def add_card(player_cards, dealer_cards):#玩家选择是否要拍
    player_choice = input('是否要牌？Y/N')#玩家进行输入
    if 'y' in player_choice or 'Y' in player_choice: #如果选择要牌
        player_cards.append(random.choice(cards))#玩家牌池中再生成一张随机手牌
        player_cards = player_if_ace(player_cards)#再次判断是否有A
        return player_cards, dealer_cards, player_choice#返回值
    else:
        dealer_control(dealer_cards,player_cards)#如果玩家不要牌，直接进入庄家操作
        return player_cards, dealer_cards, player_choice#返回值


def blackjack(w, l, t):
    won = w
    lost = l
    tie = t

    player_cards = [random.choice(cards), random.choice(cards)]#玩家的两张手牌随机生成
    player_cards = player_if_ace(player_cards)#判断手牌中是否有A，再进行新的定义

    dealer_cards = [random.choice(cards), random.choice(cards)]#庄家的两张手牌随机生成
    dealer_cards = player_if_ace(dealer_cards)#判断手牌中是否有A，再进行新的定义

    print('******* 游戏开始，你的牌是：' + str(player_cards[0]) + '和'
          + str(player_cards[1]) + ' *******\n' + '总和是'
          + str(sum(player_cards)) + '\n' + 'Dealer的牌有一张是'
          + str(dealer_cards[0]) + '\n')

    player_cards, dealer_cards, player_choice = add_card(player_cards, dealer_cards)
    while player_choice == 'y' or player_choice == 'Y':#当玩家选择要牌时
        if sum(player_cards) > 21:#如果玩家手牌之后超过了21点，直接判输，并且终止游戏
            print('很遗憾，爆牌了，当前总和' + str(sum(player_cards)))
            lost += 1#给玩家判输
            games_played = int(won) + int(lost) + int(tie)
            chance = won / games_played * 100
            time.sleep(2)
            print('一共进行了' + str(games_played) + '局' + '\n' + '赢的概率是' + str(chance) + '%')
            return won, lost, tie#利用返回值跳出此次游戏

        else:#如果玩家手牌没有超过21点，继续询问是否需要加牌
            print('你拿到了一张' + str(player_cards[-1]) + '，当前总和' + str(sum(player_cards)))
            player_cards, dealer_cards, player_choice = add_card(player_cards, dealer_cards)

    time.sleep(2)
    if sum(dealer_cards) > 21:#如果庄家手牌大于21点，玩家赢
        print('Dealer爆牌，恭喜，你赢了')
        won += 1
    else:
        if sum(dealer_cards) > sum(player_cards):#如果庄家比玩家手牌要打，庄赢
            print('对不起，你输了')
            lost += 1
        elif sum(dealer_cards) == sum(player_cards):#点数一样，平局
            print('平局')
            tie += 1
        else:
            print('恭喜，你赢了')#玩家手牌比庄家大，玩家赢
            won += 1
            time.sleep(2)

    games_played = int(won) + int(lost) + int(tie)#用于算一共玩了几局
    chance = won / games_played * 100#用于计算胜率
    print('一共进行了' + str(games_played) + '局' + '\n' + '赢的概率是' + str(chance) + '%')
    return won, lost, tie


w = 0
l = 0
t = 0
while True:
    w, l, t = blackjack(w, l, t)