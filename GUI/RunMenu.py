import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui import UIManager

BASE_WINDOW_SIZE = (800,600)
BLACK = pygame.Color('#000000')
FPS = 60


class StartMenu:
    def __init__(self, manager : UIManager):
        self.manager = manager
        self.background = pygame.Surface(BASE_WINDOW_SIZE)
        self.background.fill(BLACK)
        self.is_running=True

    def run(self):
        pass
    def quit(self):
        pass

def draw_start_menu():
    pygame.display.set_caption('Tetris GA')
    window_surface = pygame.display.set_mode(BASE_WINDOW_SIZE)

    background = pygame.Surface(BASE_WINDOW_SIZE)
    background.fill(BLACK)

    manager = UIManager(BASE_WINDOW_SIZE)

    run_button = UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text="Run", manager=manager)

    quit_button = UIButton(relative_rect=pygame.Rect((350, 175), (100, 50)), text="quit", manager=manager)

    clock = pygame.time.Clock()
