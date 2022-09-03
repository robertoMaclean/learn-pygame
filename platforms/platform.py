import pygame
from const import WIDTH, HEIGHT
from const_entities import coins
import random
from characters.coin import Coin

class Platform(pygame.sprite.Sprite):

    def __init__(self, width = 0, height = 18):
        super().__init__()
        self.image = pygame.image.load('./sprites/platform.png')
        if width == 0: 
            width = random.randint(50, 120)
        self.surf = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 10), 
                                                 random.randint(0, HEIGHT - 30)))
        self.point = True
        self.speed = random.randint(-1, 1)
        self.moving = True
        self.coins = coins

    def move(self):
        if self.moving == True: 
            if self.rect:
                self.rect.move_ip(self.speed, 0)
                if self.speed > 0 and self.rect.left > WIDTH:
                    self.rect.right = 0
                if self.speed < 0 and self.rect.right < 0:
                    self.rect.left = WIDTH

    def generate_coin(self):
        if (self.speed == 0):
            coin = Coin((self.rect.centerx, self.rect.centery - 50))
            self.coins.add(coin)
