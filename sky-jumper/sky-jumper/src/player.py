import pygame
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, anim, pos, speed, image_path, scale=SCALE) -> None:
        self.game = game

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.animation = anim
        self.speed = speed
        self.direction = pygame.math.Vector2(0, 0)

        self.is_running = False
        self.is_junping = False
        self.is_falling = False

        self.invert_sprite = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.invert_sprite = False
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.invert_sprite = True
        else:
            self.direction.x = 0

    def move(self):
        self.is_running = False
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            self.is_running = True
        self.rect.x += self.direction.x * self.speed

    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_WALK)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.animation_control()
        self.input()
        self.move()