import pygame


def draw_text(screen, text, colour=(255,255,255), font=None, size=50, pos=(20,20)): #  Default parameters :D!
    font = pygame.font.SysFont(font, size)
    x = font.render(text, True, colour)
    screen.blit(x, pos)