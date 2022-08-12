import pygame
from pygame.sprite import AbstractGroup
from const import ACC, FRIC, WIDTH

class Player(pygame.sprite.Sprite):

    def __init__(self, collide_platforms):
        self.collide_platforms = collide_platforms
        self.vec = pygame.math.Vector2  # 2 for two dimensional
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.pos = self.vec((10,360))
        self.vel = self.vec(0,0)
        self.acc = self.vec(0,0)
        self.jumping = False

    def move(self):
        self.acc = self.vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos

    def update(self):
        hits = self.__hits()
        if self.vel.y > 0: 
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
                self.jumping = False

    def jump(self):
        if self.__hits() and not self.jumping:
            self.jumping = True
            self.vel.y = -15
    
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def __hits(self):
        hits = pygame.sprite.spritecollide(self, self.collide_platforms, False)
        return hits
