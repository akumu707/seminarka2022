import pygame
import pygame_gui
import os

from screen_base import ScreenBase


class LoadScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Choose a file:", (1/3, 1/4, -1, -1, ))

        self.choice_list = self.add_selection_list((1/3, 1/4, 1/3, 1/2), [])
        self.add_button('Continue', (2/3, 1/2, -1, -1), self._on_click_continue)

        self.add_button('Back', (5/6, 3/4, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.welcome_screen))
        self.add_bg("resources/images/background.jpg")

        self.hide()

    def refresh(self):
        item_list = []
        for f in os.listdir(os.path.join("Saved")):
            item_list.append(f)
        self.choice_list.set_item_list(item_list)
        self.choice_list.rebuild()

    def _on_click_continue(self):
        if not self.choice_list.get_single_selection()==None:
            self.game_settings.load_existing_game(self.choice_list.get_single_selection())
            self.screen_options.show(self.screen_options.choice_screen)

