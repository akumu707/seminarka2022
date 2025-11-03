import pygame
import pygame_gui
import sys

from screen_base import ScreenBase


class PlayerSetupScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Who are you?", (1/3, 1/6, 1/6, 1/8))  # vraci label, ale neuklada se, protoze neni potreba
        self.add_label("Your name:", (1/3, 1/4, 1/6, 1/8))
        self.player_name_input = self.add_text_entry_line((1/2, 1/4, 1/6, 1/8))
        self.add_label("Your surname:", (1/2, 1/4, 1/5, 1/8))
        self.player_surname_input = self.add_text_entry_line((2/3, 1/4, 1/5, 1/8))
        self.add_button("Next", (1/2, 1/2, -1, -1),self._on_click_next)
        self.add_button("Back", (1/2, 1/2, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.welcome_screen))

        self.add_bg("resources/images/background.jpg")

        self.hide()

    def _on_click_next(self):
        if self.player_name_input.text == "":
            return
        else:
            self.game_settings.settings["player name"] = self.player_name_input.get_text()
        if self.player_surname_input.text == "":
            return
        else:
            self.game_settings.settings["player surname"] = self.player_surname_input.get_text()
        self.screen_options.show(self.screen_options.choice_screen)

