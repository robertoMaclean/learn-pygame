from platforms.platform import Platform
import pygame
from const import WIDTH, HEIGHT
from const_entities import all_sprites, platforms
import random

class PlatformGeneration:
    
    def __init__(self):
        platform = Platform(WIDTH, 20)
        platform.moving = False
        platform.point = False
        # platform.surf = pygame.Surface((WIDTH, 20))
        # platform.surf.fill((255, 0, 0))
        platform.rect = platform.surf.get_rect(center= (WIDTH / 2, HEIGHT - 10))
        self.all_sprites = all_sprites
        self.all_sprites.add(platform)
        self.platforms = platforms
        self.platforms.add(platform)
        self.initial_platforms()

    def initial_platforms(self):
        for x in range(random.randint(5, 6)):
            self.platform_creator(True)

    def plat_gen(self):
        while len(self.platforms) < 6:
            self.platform_creator()

    def platform_creator(self, first=False):
        width = random.randrange(50,100)
        p = Platform()             
        c = True
        while c:
            p = Platform()
            if not first:
                p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
            c = self.check(p, self.platforms)
        p.generate_coin()
        self.platforms.add(p)
        self.all_sprites.add(p)

    def check(self, platform, groupies):
        if pygame.sprite.spritecollideany(platform,groupies):
            return True
        else:
            for entity in groupies:
                if entity == platform:
                    continue
                if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
                    return True
            return False
