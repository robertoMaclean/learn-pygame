import pygame
from pygame.locals import QUIT
from const import WIDTH, HEIGHT, FPS
from const_entities import player, all_sprites, platforms, coins, displaysurface
from generators.platform_generation import PlatformGeneration
import sys
import time

pygame.init()
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Game")
platform_generation = PlatformGeneration()
background = pygame.image.load('background/background.png')
while True:
    player.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.cancel_jump()
    if player.rect and player.rect.top <= HEIGHT / 3:
        player.pos.y += abs(player.vel.y)
        for plat in platforms:
            plat.rect.y += abs(player.vel.y)
            if plat.rect and plat.rect.top >= HEIGHT:
                plat.kill()
    platform_generation.plat_gen()
    displaysurface.blit(background, (0,0))
    f = pygame.font.SysFont('Verdana', 20)
    g = f.render(str(player.score), True, (123,255,0))
    displaysurface.blit(g, (WIDTH/2, 10))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    for coin in coins:
        displaysurface.blit(coin.image, coin.rect)
        coin.update()
    pygame.display.update()
    FramePerSec.tick(FPS)
    if player.rect and player.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(0.3)
            displaysurface.fill((255,0,0))
            pygame.display.update()
            time.sleep(0.3)
            pygame.quit()
            sys.exit()
