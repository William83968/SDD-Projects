import sys
import pygame 
from os import path
from data import *
from game import *
from chip import *
pygame.init()

# BUTTON CLASS from TechWithTim
class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.on_hover = True

    def draw(self,win,font_size,outline=None,font_data=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            if font_data:
                font = pygame.font.Font(font_data, font_size)
            else:
                font = pygame.font.SysFont('comicsans', font_size)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

# Initialising fonts
pygame.font.init()

base_font = pygame.font.SysFont(BASE_FONT, FONT_SIZE)
title_font = pygame.font.SysFont(BASE_FONT, FONT_SIZE+10)

# Logistics of the game
g = Game()

def setup(win):
    if win.playing:
        if g.first_hand:
            g.shuffle()
            g.dealing()
            g.first_hand = False
        g.player_values = g.calc_hand(g.player, True)
        g.dealer_values = g.calc_hand(g.dealer, True)
    
def check_result(win):
    if win.playing:
        if g.player_values == 21:
            player.incease_chip_worth(200)
            g.reset('Win')
        if g.player_values > 21:
            g.reset('Lost')
        elif g.dealer_values > 21:
            g.reset('Win')

def deal_cards(win):
    if win.playing:
        if g.standing == False:
            if g.player_values <= 21:
                g.player.append(deck.cards.pop())
                win.draw()
                setup(win)
                check_result(win)
            setup(win)
            check_result(win)

        elif g.standing == True:
            if g.dealer_values > 18:
                g.reset("Draw")
                setup(win)
                check_result(win)
            while g.dealer_values <= 18:
                g.dealer.append(deck.cards.pop())
                win.draw()
                time.sleep(0.5)
                setup(win)
            setup(win)
            check_result(win)


def blit_p_cards(cards, y_pos, win):
    for i, card in enumerate(cards):
        win.screen.blit(win.imgs[card], (i*30+WIDTH//2-190, y_pos))

def blit_d_cards(cards, y_pos, reveal, win):
    if cards == []:
        g.dealing()
    win.screen.blit(win.imgs[cards[0]], (WIDTH//2-190, y_pos))
    if reveal:
        pass
    else:
        for i in range(len(cards)-1):
            win.screen.blit(win.down_card, ((i+1)*30+WIDTH//2-190, y_pos))

def render_text(font, text, pos, win):
    text = font.render(text, 1, WHITE)
    win.screen.blit(text, pos)

def button_animation(button, pos, color_a, color_b):
    if button.isOver(pos):
        button.color = color_a
    else:
        button.color = color_b

def placing_bets(win, chip_worth):
    player.place_bets(chip_worth)
    g.reset('draw')
    setup(win)
    win.playing = True

# Creating the buttons
Hit_button = Button(LIGHTBLUE, WIDTH-400, 800, 100, 50, 'Hit')
Stand_button = Button(LIGHTRED, WIDTH-400, 850, 100, 50, 'Stand')

class Window():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.state = 'Main'
        self.running = True
        self.playing = False

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def load(self):
        # importing images
        self.game_folder = path.dirname(__file__)
        self.cards_folder = path.join(self.game_folder, 'cards')
        self.chips_folder = path.join(self.game_folder, 'chips')
        self.imgs = {}
        for x in SUITS:
            for y in ORDER:
                card_name = y+'_of_'+x
                self.imgs[x+y] = pygame.image.load(path.join(self.cards_folder, card_name+'.png'))
        self.down_card = pygame.image.load(path.join(self.cards_folder, 'down.png'))
        self.chips_img = {}
        for i in CHIPS:
            self.chips_img[i] = pygame.image.load(path.join(self.chips_folder, i+'.png'))

        self.blackjack = pygame.image.load(path.join(self.game_folder, 'blackjack.png'))

        self.chip_50 = Chip(WIDTH - 200, 800, self.chips_img['chip_50'])
        self.chip_100 = Chip(WIDTH - 200, 900, self.chips_img['chip_100'])

    def arranging_borders(self):
        pygame.draw.line(self.screen, WHITE, (0, 750), (1200, 750), LINE_WIDTH)
        pygame.draw.line(self.screen, WHITE, (0, 220), (1200, 220), LINE_WIDTH)
        pygame.draw.line(self.screen, WHITE, (250, 220), (250, 750), LINE_WIDTH)
        pygame.draw.line(self.screen, WHITE, (950, 220), (950, 750), LINE_WIDTH)

    def render_text(self):
        render_text(title_font, 'Player', (100, 760), self)
        render_text(base_font, 'points:{}'.format(g.player_values), (100, 800), self)
        render_text(base_font, 'OnTable: ${}'.format(player.bet), (100, 950), self)
        render_text(title_font, 'Dealer', (100, 10), self)
        render_text(base_font, 'points:{}'.format(g.dealer_values), (100, 50), self)
        render_text(base_font, 'Player 3', (40, 230), self)
        render_text(base_font, 'Player 4', (990, 230), self)

    def bliting_text(self):
        blit_d_cards(g.dealer, 10, False, self)
        blit_p_cards(g.player, 760, self)

    def draw_buttons(self):
        Hit_button.draw(self.screen, 32, WHITE)
        Stand_button.draw(self.screen, 32,WHITE)

    def draw_chips(self):
        self.chip_50.draw(self)
        self.chip_100.draw(self)

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.blackjack, (WIDTH//2-200, 230))
        self.arranging_borders()
        self.render_text()
        self.bliting_text()
        self.draw_buttons()
        self.draw_chips()
        pygame.display.update()

    def update(self):
        pass

    def main(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.chip_50.isOver(mouse_pos):
                    placing_bets(self, 50)
                elif self.chip_100.isOver(mouse_pos):
                    placing_bets(self, 100)
                elif Hit_button.isOver(mouse_pos):
                    g.standing = False
                    deal_cards(self)
                elif Stand_button.isOver(mouse_pos):
                    g.standing = True
                    deal_cards(self)

        self.draw()
        self.update()
        button_animation(Hit_button, mouse_pos, BLUE, LIGHTBLUE)
        button_animation(Stand_button, mouse_pos, RED, LIGHTRED)
    
    def state_manager(self):
        if self.state == 'Main':
            self.main()

w = Window()
w.load()
while w.running:
    w.state_manager()
