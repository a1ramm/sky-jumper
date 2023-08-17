import pygame
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, anim, pos, speed, image_path, scale=SCALE) -> None:
        super().__init__()
        self.game = game

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.animation = anim

        # player movement
        self.speed = speed
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = -16

        self.is_running = False
        self.is_junping = False
        self.is_falling = False

        self.invert_sprite = False
        self.update_time = pygame.time.get_ticks()

        self.coins = 0

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
        if self.direction.x != 0:
            #self.direction = self.direction.normalize()
            self.is_running = True
        
        self.horizontal_collision()
        self.vertical_collision()

    def apply_gravity(self):
        if self.direction.y > 0:
            self.is_falling = True
        else:
            self.is_falling = False

        self.direction.y += GRAVITY
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.is_junping = True

    def horizontal_collision(self):
        self.rect.x += self.direction.x * self.speed

        for platform in self.game.platform_group:
            if platform.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = platform.rect.right
                elif self.direction.x > 0:
                    self.rect.right = platform.rect.left
    
    def vertical_collision(self):
        self.apply_gravity()

        for platform in self.game.platform_group:
            if platform.rect.colliderect(self.rect):
                if self.direction.y < 0:
                    self.rect.top = platform.rect.bottom
                    self.direction.y = 0
                elif self.direction.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.direction.y = 0
                    self.is_junping = False
                    self.is_falling = False

    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running and not self.is_junping:
            self.animation.select(PLAYER_WALK)
        if self.is_junping and not self.is_falling:
            self.animation.select(PLAYER_JUMP)
        if self.is_falling:
            self.animation.select(PLAYER_FALL)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)

    def coin_collide(self):
        for coin in pygame.sprite.spritecollide(self, self.game.coin_group, True):
            self.coins += coin.value

    def update(self):
        self.input()
        self.move()
        self.animation_control()
        self.coin_collide()