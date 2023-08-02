import pygame
import sys

from os import getcwd, listdir

from .config import *
from .player import Player
from .spritesheet import Spritesheet
from .animation import Animation
from .plataform import Plataform

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption("Dungeon Warriors")
        
        self.clock = pygame.time.Clock()
        self.running = True

    def new_game(self):
        self.running = True

        self.plataform_group = pygame.sprite.Group()

        self.plataform = Plataform(self, "assets/images/plataforms/big.png", (SCREEN_X/2, SCREEN_Y - 100), scale=3)
        self.plataform_group.add(self.plataform)

        self.bg = self.__load_bg()
        self.__load_player()

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

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_bg()
        self.plataform_group.draw(self.screen)
        self.player.draw(self.screen)
    
    def update(self):
        self.player.update()
        pygame.display.flip()

    def __load_player(self):
        player_idle_spritesheet = Spritesheet("assets/images/player/idle", 180, SCALE)
        player_walk_spritesheet = Spritesheet("assets/images/player/walk", 100, SCALE)

        player_anim = Animation()
        player_anim.add(PLAYER_IDLE, player_idle_spritesheet)
        player_anim.add(PLAYER_WALK, player_walk_spritesheet)

        self.player = Player(game=self, anim=player_anim, pos=(SCREEN_X / 2, SCREEN_Y - 50), speed=4, image_path="assets/images/player/idle/1.png")

    def __load_bg(self):
        bg_image = pygame.image.load(f"{getcwd()}/assets/images/background/island_background.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (SCREEN_X, SCREEN_Y + 200))
        return bg_image


    def draw_bg(self):
        self.screen.blit(self.bg, (0, -100))