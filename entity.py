import pygame
from graphics import Graphics


class Entity:
    def __init__(self):
        pass

    def draw(self, screen):
        pass
        
    def update(self, dt=1):  # Default to dt to 1 so you don't need it, but can implement it if you want.
        pass
    
    def input(self):
        pass
    
class Player(Entity):
    def __init__(self, x, y, speed):
        self.g = Graphics()
        self.x = x
        self.y = y
        self.speed = speed
        
        self.sprite = pygame.image.load(self.g.player)
        self.player_rect = self.sprite.get_rect(center=(x, y))
        
        self.moving_up = False
        self.moving_left = False
        self.moving_right = False
        self.moving_down = False
        
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
        
    def update(self, dt=1):
        if self.moving_up:
            self.y -= self.speed * dt
        if self.moving_left:
            self.x -= self.speed * dt
        if self.moving_down:
            self.y += self.speed * dt
        if self.moving_right:
            self.x += self.speed * dt
        