import pygame

class Chip():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, win):
        win.screen.blit(self.img, self.rect)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.rect.width:
            if pos[1] > self.y and pos[1] < self.y + self.rect.height:
                return True
        return False
