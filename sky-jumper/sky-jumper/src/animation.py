import pygame

DELAY = "delay"
ANIMATION = "animation"


class Animation:
    def __init__(self, repeat=True):
        self.repeat = repeat

        self.anims = {}
        self.sequence = []

        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0

    def add(self, id, spritesheet):
        self.anims[id] = {ANIMATION: spritesheet.list, DELAY: spritesheet.delay}

    def select(self, id):
        self.sequence = self.anims[id]

    def update_animation(self):
        if pygame.time.get_ticks() - self.update_time > self.sequence[DELAY]:
            self.update_time = pygame.time.get_ticks()
            if self.frame_index < len(self.sequence[ANIMATION]):
                self.frame_index += 1
        if self.frame_index >= len(self.sequence[ANIMATION]):
            self.frame_index = 0

        return self.sequence[ANIMATION][self.frame_index]