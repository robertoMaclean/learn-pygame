import pygame
from const_entities import player

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('./sprites/coin.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.player = player 
 
    def update(self):
        if self.rect.colliderect(self.player.rect):
            self.player.score += 5
            self.kill()
