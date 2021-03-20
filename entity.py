import pygame


class Entity:
    def __init__(self, x ,y, sprite):
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blit(self, screen):
        screen.blit(self, (self.rect))
