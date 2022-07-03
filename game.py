import sys

import pygame
from pygame.locals import *
from ScreenOptions import ScreenOptions
from pygame_gui import UIManager, PackageResource

from load_screen import LoadScreen
from save_screen import SaveScreen
from welcome_screen import WelcomeScreen
from story_choice_screen import StoryChoiceScreen
from GameSettings import GameSettings
from episode_screen import EpisodeScreen
from player_setup_screen import PlayerSetupScreen
from exploration_screen import ExplorationScreen
from choice_screen import ChoiceScreen

class GameApp:
    def __init__(self):
        pygame.init()
        self.screen_options = ScreenOptions()
        self.game_settings = GameSettings()

        if self.screen_options.fullscreen: #vytvoreni surface
            self.window_surface = pygame.display.set_mode(self.screen_options.monitor_screen,pygame.FULLSCREEN)
        elif self.screen_options.resizable:
            self.window_surface = pygame.display.set_mode(self.screen_options.resolution, pygame.RESIZABLE)
        else:
            self.window_surface = pygame.display.set_mode(self.screen_options.resolution)

        self.ui_manager = UIManager(self.screen_options.resolution, "theme.json") #zalozeni managera

        self.background_surface = pygame.Surface(self.screen_options.resolution)
        self.background_surface.fill(self.ui_manager.get_theme().get_colour('dark_bg')) #pozadi

        self.screen_options.welcome_screen = WelcomeScreen(self.screen_options, self.ui_manager, self.game_settings, self.background_surface)
        self.screen_options.story_choice_screen = StoryChoiceScreen(self.screen_options, self.ui_manager, self.game_settings, self.background_surface)
        self.screen_options.episode_screen = EpisodeScreen(self.screen_options, self.ui_manager, self.game_settings, self.background_surface)
        self.screen_options.player_setup_screen = PlayerSetupScreen(self.screen_options, self.ui_manager, self.game_settings, self.background_surface)
        self.screen_options.load_screen = LoadScreen(self.screen_options, self.ui_manager,
                                                                    self.game_settings, self.background_surface)
        self.screen_options.save_screen = SaveScreen(self.screen_options, self.ui_manager,
                                                                    self.game_settings, self.background_surface)
        self.screen_options.exploration_screen = ExplorationScreen(self.screen_options, self.ui_manager,
                                                     self.game_settings, self.background_surface)
        self.screen_options.choice_screen = ChoiceScreen(self.screen_options, self.ui_manager,
                                                                   self.game_settings, self.background_surface)
        self.screen_options.show(self.screen_options.welcome_screen)

    def run(self):
        is_running = True
        clock = pygame.time.Clock()
        while is_running:    #game loop
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.VIDEORESIZE:
                    self.screen_options.resolution = (event.w, event.h)
                    self.window_surface = pygame.display.set_mode(self.screen_options.resolution, pygame.RESIZABLE)
                    self.screen_options.active_screen.refresh()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        is_running = False
                self.screen_options.active_screen.process_event(event)
                self.ui_manager.process_events(event)

            self.window_surface.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.window_surface)

            self.ui_manager.update(time_delta)
            pygame.display.update()



