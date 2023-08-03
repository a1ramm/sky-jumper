import pygame

from .config import *

class Plataform(pygame.sprite.Sprite):
    def __init__(self, game, img, pos, scale=SCALE) -> None:
        super().__init__()
        self.game = game

        self.image = pygame.image.load(f"assets/images/plataforms/{img}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.y = pos[1]

