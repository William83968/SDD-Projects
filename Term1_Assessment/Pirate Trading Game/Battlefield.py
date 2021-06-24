import pygame
import sys

# Basics
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1000, 706
win = pygame.display.set_mode((screen_width, screen_height))

# Importing images
FIELD = pygame.image.load("atlantic.png")
SHIP = pygame.image.load("pirate-ship.png")
BOMB = pygame.image.load("bomb.png")
NAVY = pygame.image.load("navy.png")

# Player initilisation
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.image = SHIP
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.center = (self.x, self.y)
    
    def create_bullet(self):
        return Bullet(self.x, self.y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.image = BOMB
        self.rect = self.image.get_rect(center = (self.x, self.y+20))
    
    def update(self):
        self.rect.x += 10
        
        if self.rect.x >= screen_width + 200:
            self.kill()

player = Player(200, 100, 5)
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

# Game Loop
while True:
    win.blit(FIELD, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_group.add(player.create_bullet())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.y >= 64:
        player_group.update(0, -10)
    if keys[pygame.K_DOWN] and player.y <= 642:
        player_group.update(0, 10)
    if keys[pygame.K_LEFT] and player.x >= 136:
        player_group.update(-10, 0)
    if keys[pygame.K_RIGHT] and player.x <= 336:
        player_group.update(10, 0)
    
    # Drawing
    player_group.draw(win)
    bullet_group.draw(win)
    bullet_group.update()
    pygame.display.flip()
    clock.tick(120)