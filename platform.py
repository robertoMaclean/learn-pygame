import pygame
from const import WIDTH, HEIGHT
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 10), 
                                                 random.randint(0, HEIGHT - 30)))

    def move(self):
        pass
