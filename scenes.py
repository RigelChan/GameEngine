import pygame
import sys
import utils
from constants import Constants
from entity import Player


class Scene: #  This is the abstract class we base all other scenes upon.
    def __init__(self):
        pass
    def update(self, sm, dt):
        pass
    def enter(self):
        pass
    def exit(self):
        pass
    def input(self, sm):
        pass
    def draw(self, sm, screen):
        pass

class MainMenu(Scene):
    def __init__(self):
        self.c = Constants()

    def draw(self, sm, screen): # We pass in sm referring to its instance within the scene manager.
        screen.fill(self.c.black)
        utils.draw_text(screen, "Main Menu")
        utils.draw_text(screen, "Click [G] for Game", pos=(20, 300))  # Choosing which parameter we want to customize.
        utils.draw_text(screen, "Click [S] for Settings", pos=(20, 550))
        utils.draw_text(screen, "Click [Q] to Quit", pos=(20, 800))
        
    def update(self, sm, dt):
        pass
        

    def input(self, sm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    sm.push(FadeTransitionScene(self, Game()))
                if event.key == pygame.K_s:
                    sm.push(FadeTransitionScene(self, SettingsMenu()))
                if event.key == pygame.K_q:
                    sys.exit(0)
                    
    def exit(self):
        print("Leaving Main Menu.")
        
    def enter(self):
        print("Entering Main Menu.")

class Game(Scene):
    def __init__(self):
        self.c = Constants()
        self.player = Player(self.c.screen_width/2, self.c.screen_height/2, 300)

    def draw(self, sm, screen):
        screen.fill(self.c.black)
        utils.draw_text(screen, "Game: [M] to Menu")
        self.player.draw(screen)

    def input(self, sm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    sm.pop()
                    sm.push(FadeTransitionScene(self, None)) # We pass none as we are not transitiong to a *new* scene.
                if event.key == pygame.K_w:
                    self.player.moving_up = True
                if event.key == pygame.K_s:
                    self.player.moving_down = True
                if event.key == pygame.K_a:
                    self.player.moving_left = True
                if event.key == pygame.K_d:
                    self.player.moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.moving_up = False
                if event.key == pygame.K_s:
                    self.player.moving_down = False
                if event.key == pygame.K_a:
                    self.player.moving_left = False
                if event.key == pygame.K_d:
                    self.player.moving_right = False
                                
    def update(self, sm, dt):
        self.player.update(dt)

    def exit(self):
        print("Leaving Game.")
    
    def enter(self):
        print("Entering Game.")

class SettingsMenu(Scene):
    def __init__(self):
        self.c = Constants()
        
    def draw(self, sm, screen):
        screen.fill(self.c.black)
        utils.draw_text(screen, "Game: [M] to Menu")
        
    def input(self, sm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    sm.pop()
                    sm.push(FadeTransitionScene(self, None)) 
                    
    def exit(self):
        print("Leaving Settings.")
    
    def enter(self):
        print("Entering Settings.")

class TransitionScene(Scene):
    def __init__(self, fromScene, toScene):
        self.c = Constants()
        self.currentPercentage = 0
        self.fromScene = fromScene
        self.toScene = toScene
    def update(self, sm, dt):
        self.currentPercentage += 4
        if self.currentPercentage >= 100:
            sm.pop() # Pops itself when the transition is finished.
            if self.toScene is not None:
                sm.push(self.toScene) # Pushes the next scene onto the stack and displays it.
                
    def exit(self):
        print("Leaving Transition.")
    
    def enter(self):
        print("Entering Transition.")

class FadeTransitionScene(TransitionScene):
    def draw(self, sm, screen):
        if self.currentPercentage < 50:
            self.fromScene.draw(sm, screen) # Draw the old scene while transition is only half way complete.
        else:
            if self.toScene is None:
                sm.scenes[-2].draw(sm, screen)
            else:
                self.toScene.draw(sm, screen)
        
        alpha = int(abs((255-(255/50)*self.currentPercentage))) # Subtact 510 from 255, and then return an abs value.
        overlay = pygame.Surface((self.c.screen_width, self.c.screen_height))
        overlay.set_alpha(255 - alpha)
        overlay.fill(self.c.black)
        screen.blit(overlay, (0,0))

