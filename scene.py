import pygame
import sys
import utils
from constants import Constants


class Scene: #  This is the abstract class we base all other scenes upon.
    def __init__(self):
        pass
    def update(self, sm):
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
                    sm.push(FadeTransitionScene(self, None)) # We pass none as we are not transitiong to a *new* scene.

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
    def update(self, sm):
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

class SceneManager:
    def __init__(self):
        self.scenes = []

    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)

    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)

    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        pygame.display.update()

    def sceneExit(self):
        if len(self.scenes) > 0:
            self.scenes[-1].exit()

    def sceneEnter(self):
        if len(self.scenes) > 0:
            self.scenes[-1].enter()

    def pop(self):
        self.sceneExit()
        self.scenes.pop()
        self.sceneEnter()
        print(self.scenes)

    def push(self, scene):
        self.sceneExit()
        self.scenes.append(scene)
        self.sceneEnter()
        print(self.scenes)

    def set(self, scene):
        while len(self.scenes) > 0:
            self.pop()
        for s in scenes:
            self.push(s)