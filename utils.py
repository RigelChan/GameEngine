import pygame


def draw_text(screen, text, colour, font, size, xpos, ypos):
    font = pygame.font.SysFont(font, size)
    x = font.render(str(text), True, colour)
    screen.blit(x, (xpos, ypos))