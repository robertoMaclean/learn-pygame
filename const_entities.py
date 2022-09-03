import pygame
from characters.player import Player
from const import WIDTH, HEIGHT

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()
player = Player(platforms) 
all_sprites.add(player)
