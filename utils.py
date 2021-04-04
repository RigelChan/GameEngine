import pygame


def draw_text(screen, text, colour=(255,255,255), font=None, size=50, pos=(20,20)): #  Default parameters :D!
    font = pygame.font.SysFont(font, size)
    x = font.render(text, True, colour)
    screen.blit(x, pos)
    
class SceneManager:
    def __init__(self):
        self.scenes = []

    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)

    def update(self, dt):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, dt)

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