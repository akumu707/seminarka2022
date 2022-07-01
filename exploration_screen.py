import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class ExplorationScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.location_buttons = []
        for i, location in enumerate(self.game_settings.settings["locations"]):
            self.location_buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50*(i+1), 200, -1, -1),
                                                          text=location[0],
                                                          manager=self.ui_manager))
        self.hide()

    def refresh(self):
        for i, location in enumerate(self.game_settings["locations"]):
            self.location_buttons.append(
                pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50 * (i + 1), 200, -1, -1),
                                             text=location[0],
                                             manager=self.ui_manager))

    def hide(self):
        for button in self.location_buttons:
            button.hide()

    def show(self):
        for button in self.location_buttons:
            button.show()

    def process_event(self, event):
        pass