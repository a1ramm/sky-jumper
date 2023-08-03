import pygame
import sys

from os import getcwd, listdir
from random import randint, choice

from .config import *
from .player import Player
from .spritesheet import Spritesheet
from .animation import Animation
from .plataform import Plataform
from .camera import Camera

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption("Dungeon Warriors")
        
        self.clock = pygame.time.Clock()
        self.running = True

    def new_game(self):
        self.running = True

        self.__load_groups()
        self.__load_plataforms()
        self.bg = self.__load_bg()
        self.__load_player()

        self.camera = Camera(self.player, SCREEN_X, SCREEN_Y)

        self.run()
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.check_events()
            self.draw()
            self.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_bg()

        for sprite in self.player_group:
            self.screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

        for sprite in self.plataform_group:
            self.screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

    def update(self):
        self.player_group.update()
        self.camera.scroll()
        pygame.display.flip()


    def __load_player(self):
        player_idle_spritesheet = Spritesheet("assets/images/player/idle", 180, SCALE)
        player_walk_spritesheet = Spritesheet("assets/images/player/walk", 100, SCALE)
        player_jump_spritesheet = Spritesheet("assets/images/player/jump", 999, SCALE)
        player_fall_spritesheet = Spritesheet("assets/images/player/fall", 999, SCALE)

        player_anim = Animation()
        player_anim.add(PLAYER_IDLE, player_idle_spritesheet)
        player_anim.add(PLAYER_WALK, player_walk_spritesheet)
        player_anim.add(PLAYER_JUMP, player_jump_spritesheet)
        player_anim.add(PLAYER_FALL, player_fall_spritesheet)

        self.player = Player(game=self, anim=player_anim, pos=(SCREEN_X / 2, SCREEN_Y - 120), speed=4, image_path="assets/images/player/idle/1.png")
        self.player_group.add(self.player)

    def __load_bg(self):
        bg_image = pygame.image.load(f"{getcwd()}/assets/images/background/island_background.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (SCREEN_X, SCREEN_Y + 200))
        return bg_image
    
    def __load_groups(self):
        self.player_group = pygame.sprite.GroupSingle()
        self.plataform_group = pygame.sprite.Group()

    def __load_plataforms(self):
        self.main_plataform = Plataform(self, "big", (SCREEN_X/2, SCREEN_Y - 100), scale=3)
        self.plataform_group.add(self.main_plataform)

        for i in range(10):
            p = Plataform(self, "medium", (randint(0, SCREEN_X), 400 + i * -300))
            self.plataform_group.add(p)


    def draw_bg(self):
        self.screen.blit(self.bg, (0, -100))