import pygame
from pygame.locals import *
from const import WIDTH, HEIGHT, FPS 
from platform import Platform
from player import Player
import sys
import random

pygame.init()
 
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

def plat_gen():
    while len(platforms) < 6:
        width = random.randrange(50,100)
        p = Platform()             
        C = True
        while C:
            p = Platform()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
            C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
                return True
        return False

platform = Platform()
platform.surf = pygame.Surface((WIDTH, 20))
platform.surf.fill((255, 0, 0))
platform.rect = platform.surf.get_rect(center= (WIDTH / 2, HEIGHT - 10))
all_sprites = pygame.sprite.Group()
all_sprites.add(platform)
platforms = pygame.sprite.Group()
platforms.add(platform)
player = Player(platforms)
all_sprites.add(player)

for x in range(random.randint(5, 6)):
    C = True
    platform = Platform()
    while C:
        platform = Platform()
        C = check(platform, platforms)
    platforms.add(platform)
    all_sprites.add(platform)

while True:
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

    if player.rect.top <= HEIGHT / 3:
        player.pos.y += abs(player.vel.y)
        for plat in platforms:
            plat.rect.y += abs(player.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()
 
    plat_gen()
    displaysurface.fill((0,0,0))
    player.update()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    FramePerSec.tick(FPS)
