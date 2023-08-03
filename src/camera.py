import pygame
from pygame.math import Vector2

class Camera:
    def __init__(self, target, width, height):
        self.width = width
        self.height = height
        self.camera = Vector2(target.rect.centerx, target.rect.centery)
        self.target = target
        self.offset = Vector2(0,0)

    def scroll(self):
        self.pointTarget = self.target.rect.center - self.camera
        self.camera.y += self.pointTarget.y
        self.offset = -self.camera + Vector2(self.width / 2, 500)