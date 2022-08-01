import pygame
import pygame_gui

from screen_base import ScreenBase


class WelcomeScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Welcome", (350, 100, -1, -1,))
        self.add_button('Start new game', (350, 200, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.player_setup_screen))
        self.add_button('Load game', (350, 300, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.load_screen))
        self.add_button('End', (350, 400, -1, -1), None)
        self.add_bg("resources/images/background.jpg")

        self.hide()



