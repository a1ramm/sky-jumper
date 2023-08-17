import pygame
from .config import *


class Coin(pygame.sprite.Sprite):
    def __init__(self, anim, pos, scale=SCALE) -> None:
        super().__init__()

        self.image = pygame.image.load("assets/images/coin/1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.animation = anim
        self.value = 1

    def update(self):
        self.animation_control()

    def animation_control(self):
        self.animation.select(COIN_DEFAULT)
        self.image = self.animation.update_animation()