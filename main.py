import pygame
import sys
import time
import ctypes
from constants import Constants
from scene import SceneManager, MainMenu

ctypes.windll.user32.SetProcessDPIAware() # Makes the window the correct size irrelevant of Windows 10 scale settings.


class Game:
    def __init__(self):
        self.c = Constants()
        self.sm = SceneManager()
        self.mm = MainMenu()
        self.sm.push(self.mm)
        pygame.init()
        pygame.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=312)

        self.screen = pygame.display.set_mode((self.c.screen_width, self.c.screen_height))
        pygame.display.set_caption("Game")
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.last_time = time.time()

    def draw_screen(self):
        self.sm.draw(self.screen)

    def check_events(self):
        self.sm.input()

    def update(self):
        self.sm.update()

    def run(self):
        dt = 0
        while True:
            self.check_events()
            self.draw_screen()
            self.update()
            dt = self.clock.tick(60)/1000

if __name__ == "__main__":
    g = Game()
    g.run()