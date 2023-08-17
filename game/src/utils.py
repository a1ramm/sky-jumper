import pygame
from .config import *

def draw_text(screen, text, size, color, x, y, style=PIXEL_FONT, topleft=False):
    fonte = pygame.font.Font(style, size)
    text_obj = fonte.render(text, False, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)

    if topleft:
        text_rect.topleft = (x, y)
        
    screen.blit(text_obj, text_rect)
