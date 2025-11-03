import pygame
import pygame_gui

from screen_base import ScreenBase


class WelcomeScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Welcome", (1/4, 1/4, -1, -1,))
        self.add_button('Start new game', (1/3, 1/4, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.player_setup_screen))
        self.add_button('Load game', (1/3, 1/4, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.load_screen))
        self.add_button('End', (1/3, 1/4, -1, -1), self._on_click_end)
        self.add_bg("resources/images/background.jpg")

        self.hide()

    def _on_click_end(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))


