import pygame
import pygame_gui
import sys

from screen_base import ScreenBase


class PlayerSetupScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Who are you?", (320, 10, 125, 50))  # vraci label, ale neuklada se, protoze neni potreba
        self.add_label("Your name:", (300, 100, 100, 50))
        self.player_name_input = self.add_text_entry_line((400, 100, 100, 50))
        self.add_label("Your surname:", (280, 200, 120, 50))
        self.player_surname_input = self.add_text_entry_line((400, 200, 100, 50))
        self.add_button("Next", (350, 300, -1, -1),self._on_click_next)
        self.add_button("Back", (350, 400, -1, -1),
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

