import pygame
from os import listdir

class Spritesheet:
    def __init__(self, path, delay, scale=1, rotation=0) -> None:
        self.path = path
        self.delay = delay
        self.scale = scale
        self.rotation = rotation

        self.list = self.create_spritesheet()

    def create_spritesheet(self):
        img_list = []
        num_of_frames = len(listdir(self.path))

        for i in range(1, num_of_frames+1):
            image = pygame.image.load(f"{self.path}/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))
            image = pygame.transform.rotate(image, self.rotation)

            img_list.append(image)
        return img_list