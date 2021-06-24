import pygame
import time
import random
import sys
pygame.font.init()
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("MAIN MENU")
win = pygame.display.set_mode((1000, 706))

# Make background 
win.fill((255, 255, 255))
MAP = pygame.image.load("Treasure_map.jpg")
BLACK_PEARL = pygame.image.load("082018BP.jpg")


# Importing images
DOLLAR = pygame.image.load("dollar.png")
ANCHOR = pygame.image.load("anchor.png")
SKULL = pygame.image.load("skull.png")
TRUST_BALL = pygame.image.load("trust_ball.png")
MESSAGEPAPER = pygame.image.load("message_paper.png")
TECH = pygame.image.load("tech.png")
STAMP = pygame.image.load("stamp.png")
TEAM = pygame.image.load("teamwork.png")

menu_buttons = []
destroy_buttons = []

# Importing music
bg_music1 = pygame.mixer.Sound("The Sailor's Tale.wav")
bg_music1.set_volume(0.2)

bg_music2 = pygame.mixer.Sound("DMTN.ogg")
bg_music2.set_volume(0.4)

# BUTTON CLASS from TechWithTim
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

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

# Creating Buttons
startButton = button((0, 110, 255), 40, 550, 170, 80, 'START GAME')
quitButton = button((255, 128, 0), 250, 550, 170, 80, 'QUIT')
info_button = button((102, 153, 153), 10, 10, 60, 30, 'Info')
destroy_button1 = button((128,0,0), 570, 50, 32, 32, 'X')
continue_button = button((71, 71, 107), 10, 655, 140, 40, "Continue")

# coordinates
coordinates = [(352, 494), (380, 444), (335, 380), (512, 307), (588, 222), (533, 146), (611, 155)]

# Class to contain all the player property
class Player():
    def __init__(self):
        self.gold_coin = 0
        self.underworld_power = 0
        self.ethical_value = -100
        self.official_power = 0
        self.navy_power = 0
        self.technological_power = 0
        self.social_power = 0

class Numeral_input():
    def __init__(self, font_data, x, y):
        self.base_font = pygame.font.Font(font_data, 32)
        self.x = x
        self.y = y
        self.input_rect = pygame.Rect(self.x, self.y, 140, 32)
        self.color_active = pygame.Color((178,34,34))
        self.color_passive = pygame.Color((192,192,192))
        self.input = ''
        self.color = None
        self.active = False

    def update_text(self, event, length=None):
        if self.active == True:
            if event.key == pygame.K_BACKSPACE:
                self.input = self.input[:-1]
            else:
                self.input += event.unicode

    def selection(self, pos):
        if self.input_rect.collidepoint(pos):
            self.active = True
        else:
            self.active = False
        
    def draw(self, surface):
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

        pygame.draw.rect(surface, self.color, self.input_rect, 2)

        self.text_surface = self.base_font.render(self.input, True, (255, 255, 255))
        if self.text_surface.get_width() <= self.input_rect.w:
            surface.blit(self.text_surface, (self.input_rect.x, self.input_rect.y))
        else: 
            self.input = ''
        
def render_text(font_data, size, text_data, color, position, length=None):
    font = pygame.font.SysFont(font_data, size)
    text = font.render(text_data, 1, color)
    win.blit(text, position)

def redrawWindow():
    win.fill((255, 255, 255))
    win.blit(MAP, (0, 0))

def show_value(win, image_data, image_pos, numeral_value):
    win.blit(image_data, image_pos)
    render_text(None, 30, numeral_value, (102, 102, 153), (image_pos[0]+60, image_pos[1]+5))
    
def button_animation(button, pos, color_a, color_b):
    if button.isOver(pos):
        button.color = color_a
    else:
        button.color = color_b


# Using a class to avoid python GIL lock down
class Game():
    def __init__(self):
        self.game_state = 'intro'
        self.clock = pygame.time.Clock()
        self.player_name = None
        self.input = ""
        self.input_active = False
        self.info_active = False
        self.popup_active = True
        self.input_rect = Numeral_input('dynalight.otf', 665, 655)
        self.message = "Hello, I'm your servant, Azuma the Screenship..."
        self.storyline_messages = open("storyline.txt")
        self.message_cursor = 0
        self.level = 0
        self.location_buttons = []
        self.randomize = False
        self.bgMusic_playing = False
        bg_music2.play()
        for i in range(7):
            self.location_buttons.append(button((51, 51, 77), coordinates[i][0], coordinates[i][1], 20, 20, ''))
        self.options = {
                       "Gold coin":100,
                       "Gunpowder":70,
                       "Vegetable Powder":500,
                       "Underworld money":700,
                       "Ticket to Soul Island":1100,
                       "Magical Spell":4500,
                       "Understandably strong shield":7000,
                       "Indescribable strong spear":11000,
                       }

    def info_menu(self, top, left):
        self.popupSurf = pygame.Surface((600, 400))
        self.popupSurf.fill((204, 153, 102))
        self.base_font = pygame.font.Font(None, 30)
        self.popupRect = self.popupSurf.get_rect()
        
        for option in self.options: 
            textSurf1 = self.base_font.render(option, 1, (165,42,42))
            textRect1 = textSurf1.get_rect()
            textRect1.top = top
            textRect1.left = left
            self.popupSurf.blit(textSurf1, textRect1)

            textSurf2 = self.base_font.render("$"+str(self.options[option]), 1, (165,42,42))
            textRect2 = textSurf1.get_rect()
            textRect2.top = top
            textRect2.left = left+450
            self.popupSurf.blit(textSurf2, textRect2)

            top += pygame.font.Font.get_linesize(self.base_font)+10

        pygame.draw.rect(self.popupSurf, (97, 31, 31), self.popupRect, 10)
        self.popupRect.x = 10
        self.popupRect.y = 50
        win.blit(self.popupSurf, self.popupRect)
        
        destroy_buttons.append(destroy_button1)
        destroy_button1.draw(win, 32)
    
    def make_popup(self, input_active):
        self.m_Surf = pygame.Surface((1000, 100))
        self.m_Surf.fill((255, 191, 128))
        self.m_Rect = self.m_Surf.get_rect()
        self.m_Rect.x = 10
        self.m_Rect.y = 600

        #Rendering stuff
        self.m_Font = pygame.font.Font('dynalight.otf', 32)
        self.t_Surf = self.m_Font.render(self.message, 1, (102, 0, 53))
        self.t_Rect = self.t_Surf.get_rect()
        self.t_Rect.x, self.t_Rect.y = 2, 5

        self.t_Surf2 = self.m_Font.render('Your response: ', 1, (102, 0, 53))
        self.t_Rect2 = self.t_Surf2.get_rect()
        self.t_Rect2.x, self.t_Rect2.y = 500, 50

        #Bliting all the stuff including the window
        if self.popup_active:
            self.m_Surf.blit(self.t_Surf, self.t_Rect)
            if input_active:
                self.m_Surf.blit(self.t_Surf2, self.t_Rect2)
            win.blit(self.m_Surf, self.m_Rect)

    def unlocking_locations(self, level):
        if self.bgMusic_playing == False:
                bg_music2.stop()
                bg_music1.play(-1)
                self.bgMusic_playing = True
        for i in range(7):
            if self.level == i+1:
                self.location_buttons[level-1].draw(win, 1, (0, 0, 0))
        
               
    def intro(self):
        redrawWindow()
        startButton.draw(win, 30, (0, 0, 128))
        quitButton.draw(win, 30, (170, 255, 128))
        render_text('comicsans', 100, "PIRATE TRADING GAME", (0, 255, 255), (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isOver(pos):
                    self.game_state = 'main'
                elif quitButton.isOver(pos):
                    sys.exit()

            button_animation(startButton, pos, (0, 0, 179), (0, 0, 128))
            button_animation(quitButton, pos, (204, 255, 179), (170, 255, 128))

    def main(self):
        redrawWindow()
        pygame.display.set_caption("ISLANDS")
        show_value(win, DOLLAR, (850, 10), str(player.gold_coin))
        show_value(win, ANCHOR, (850, 50), str(player.navy_power))
        show_value(win, SKULL, (850, 90), str(player.underworld_power))
        show_value(win, TRUST_BALL, (850, 140), str(player.ethical_value))
        if player.technological_power != 0:
            show_value(win, TECH, (850, 190), str(player.technological_power))
        if player.official_power != 0:
            show_value(win, TECH, (850, 240), str(player.official_power))

        #Drawing buttons
        menu_buttons.append(info_button)
        menu_buttons.append(continue_button)
        info_button.draw(win, 20, (102, 153, 153), 'Jaapokki-Regular.otf')
        if self.popup_active:
            self.make_popup(self.input_rect.active)
            continue_button.draw(win, 30, (71, 71, 107), 'dynalight.otf')

        # Additional images
        if self.message_cursor == 25:
            self.black_rect = BLACK_PEARL.get_rect()
            self.black_rect.x = 490
            self.black_rect.y = 320
            pygame.draw.rect(win, (102, 102, 153), self.black_rect, 10)
            win.blit(BLACK_PEARL, (490,320))

        if self.level == 0:
            Storyline_process0()
        elif self.level == 1:
            Storyline_process1()
        elif self.level == 2:
            Storyline_process2()
        elif self.level == 3:
            Storyline_process3()
        elif self.level == 4:
            Storyline_process4()
        elif self.level == 5:
            Storyline_process5()
        elif self.level == 6:
            Storyline_process6()
        elif self.level == 7:
            Storyline_process7()
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                open_info(info_button, pos)
                destroy_function(destroy_button1, pos)
                story_plot(continue_button, pos)
                for i in range(7):
                    story_plot(self.location_buttons[i], pos)          
                self.input_rect.selection(event.pos)

            if event.type == pygame.KEYDOWN:
                self.input_rect.update_text(event)

            button_animation(destroy_button1, pos, (255, 128, 128),(204, 0, 0))
            button_animation(info_button, pos, (102, 153, 153), (0, 128, 85))
            if self.popup_active:
                button_animation(continue_button, pos,(163, 163, 194),(71, 71, 107))
            for i in range(7):
                button_animation(self.location_buttons[i], pos, (92, 92, 138),(51, 51, 77))

        # for i in range(7):
        #     self.location_buttons[i].draw(win, 1, (0, 0, 0))
        self.unlocking_locations(self.level)

        if GAME.info_active:
            self.info_menu(10, 10)

        if self.input_active:
            self.input_rect.draw(win)

        pygame.display.update()

    def state_manager(self, rate):
        if self.game_state == 'intro':
            self.intro()
        if self.game_state == 'main':
            self.main()
        self.clock.tick(rate)

def destroy_function(button, pos):
    if button.isOver(pos):
        GAME.info_active = False

def open_info(button, pos):
    if button.isOver(pos):
        GAME.options["Vegetable Powder"] = random.randrange(200, 1000, 50)
        GAME.options["Magical Spell"] = random.randrange(4500, 6000, 100)
        GAME.info_active = True

def story_plot(button, pos):
    if button.isOver(pos):
        GAME.message_cursor += 1
    
def next_phase(level, r_cursor):
    if level == r_cursor:
        GAME.level += 1


player = Player()
def Storyline_process0():
    # PHASE 1
    if GAME.message_cursor == 1:
        GAME.message = "The world now is now divided between England and Ireland"
    if GAME.message_cursor == 2:
        GAME.message = "and your job is...ah...overloaded..."
        player.gold_coin = 2000
    if GAME.message_cursor == 3:
        GAME.message = "Hey, say no more and start trading!"
    if GAME.message_cursor == 4:
        GAME.message = ""
        next_phase(GAME.level, 0)

def Storyline_process1():
    # PHASE 2
    if GAME.message_cursor == 5:
        GAME.message = "(In East Lorent)"
    if GAME.message_cursor == 6:
        GAME.message = "May I please know your name?"
    if GAME.message_cursor == 7:
        GAME.message = "(Click the bottom left of this box and type in your name...)"
        GAME.input_active = True
    if GAME.message_cursor == 8 and GAME.input_rect.input != '$ ':
        GAME.input_active = False
        GAME.player_name = '$ '+GAME.input_rect.input+' $'
        GAME.message = GAME.player_name + " , shell we expel away the misfortune?"
    if GAME.message_cursor == 9:
        GAME.message = "You saw the witch over there?"
    if GAME.message_cursor == 10:
        GAME.message = "Go to that sacred widow and have an eye into heaven"
    if GAME.message_cursor == 11:
        GAME.message = "Witch: Oh, for god's sake finally..."
    if GAME.message_cursor == 12:
        GAME.message = "Witch: Listen, your future is as bright as the light on the ship Queen Elizabeth"
    if GAME.message_cursor == 13:
        GAME.message = "Witch: May the prayer of me follow you til the darkest end of the world..."
        player.navy_power = 10
    if GAME.message_cursor == 14:
        GAME.message = "Smuggler: Hey, you bastard! Did you know you just let go of my slave!"
    if GAME.message_cursor == 15:
        GAME.message = "Smuggler: How dare you little monsoon!"
    if GAME.message_cursor == 16:
        GAME.message = "Smuggler: I will curse for you for paying me with nothing!"
    if GAME.message_cursor == 17:
        GAME.message = "well...pay him something then..."
        GAME.input_active = True
    if GAME.message_cursor == 18 and GAME.input_rect.input != "":
        GAME.input_active = False
        player.gold_coin -= int(GAME.input_rect.input)
        player.technological_power = 1
        GAME.message = "Smuggler: Now I for that I am happy, I will give you my newest invention"
        time.sleep(0.4)
        GAME.message_cursor += 1
    if GAME.message_cursor == 19:
        GAME.message = "That's not new at all, let's get away from this fraud"
        next_phase(GAME.level, 1)
        
def Storyline_process2():
    # PHASE 3
    if GAME.message_cursor == 20:
        GAME.message = "(In Castle Town)"
    if GAME.message_cursor == 21:
        GAME.message = "Let's buy some ...SHUT UP..you begger!"
    if GAME.message_cursor == 22:
        GAME.message = "Treasure hunter: Not a begger, mate, I'm just eager to get the Black Pearl!"
    if GAME.message_cursor == 23:
        GAME.message = "Treasure hunter: How about you bring the Black Pearl to me..."
    if GAME.message_cursor == 24:
        GAME.message = "No need to be idiotic, let's go"
    if GAME.message_cursor == 25:
        GAME.message = "Treasure hunter: FINE! I will give you the image of black pearl"
    if GAME.message_cursor == 26 and GAME.input_rect.input != "":
        GAME.message = "This man has no cure..."
    if GAME.message_cursor == 27:
        GAME.message = "Weird boy: Oh, ghost, can you please forgive me..."
    if GAME.message_cursor == 28:
        GAME.message = "Weird boy: Echo my words along the side of hell!"
    if GAME.message_cursor == 29:
        GAME.message = "That's bizzare! Maybe it's time to buy some weapons."
    if GAME.message_cursor == 30:
        GAME.message = "Black smith: Hey you..I mean you...You WANT some swords?"
    if GAME.message_cursor == 31:
        GAME.input_active = True 
        GAME.message = "You want to buy some Iron Sword?(Click continue when you have enough..or...)"
    if GAME.message_cursor == 32 and GAME.input_rect.input:
        player.gold_coin -= int(GAME.input_rect.input)*10
        player.navy_power += int(GAME.input_rect.input)
        player.technological_power += int(GAME.input_rect.input)
        if player.gold_coin <= 1000:
            player.gold_coin = 1000
            player.ethical_value -= int(GAME.input_rect.input)
        GAME.message = "Black smith: My sword is steel-driven...DANG...I have done it way more than a hundred...DANG..."
    if GAME.message_cursor == 33:
        GAME.input_active = False
        GAME.message = "Okay, let's move on with the journey"
        next_phase(GAME.level, 2)

def Storyline_process3():
    # PHASE 4
    if GAME.message_cursor == 34:
        GAME.message = "(In West Lorent)"
    if GAME.message_cursor == 35:
        GAME.message = "Old man: YOU!Just RIGHT!"
    if GAME.message_cursor == 36:
        GAME.message = "Old man: You come with me, my son will need you..."
    if GAME.message_cursor == 37:
        GAME.message = "Weird boy: NONSENSE!NONSENSE!NONSENSE!They're devils from heaven!"
    if GAME.message_cursor == 38:
        GAME.message = "Old man: You want these devil-like ghost swelling all over you or do want it be fixed?"
    if GAME.message_cursor == 39:
        GAME.message = "Old man: You have just enough bad luck for me!"
        player.ethical_value += 100
        time.sleep(0.4)
        GAME.message_cursor += 1
    if GAME.message_cursor == 40:
        GAME.message = "Bishop: You have illegal presence here!"
    if GAME.message_cursor == 41:
        GAME.message = "You stupid bishop!Don't you see we're fixing this fellow citizen?"
    if GAME.message_cursor == 42:
        GAME.message = "Bishop: HE IS NOT CITIZEN!Disrespect to our great lord!"
    if GAME.message_cursor == 43:
        GAME.message = "Lord Melfern: HEY! Pay some respect to my guest!"
    if GAME.message_cursor == 44:
        GAME.message = "Lord Melfern: Would you like to trade with us?"
    if GAME.message_cursor == 45 and GAME.input_rect.input != "":
        player.gold_coin -= int(GAME.input_rect.input)*10
        player.official_power += int(GAME.input_rect.input)
        GAME.message = "That's a fair trade.."
        if player.gold_coin <= 0:
            GAME.message_cursor += 1
    
def Storyline_process4():
    pass

def Storyline_process5():
    pass

def Storyline_process6():
    pass

def Storyline_process7():
    pass

random.seed(2)
GAME = Game()
clock = pygame.time.Clock()


if __name__ == '__main__':
    while True:
        GAME.state_manager(30)
        
    



    



