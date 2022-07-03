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
        self.people_selection_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect(200, 100, 100, 100), manager=ui_manager, item_list = [], object_id=ObjectID(class_id='@selection_list_item'))
        self.hide()

    def refresh(self):
        for i, location in enumerate(self.game_settings["locations"]):
            self.location_buttons.append(
                pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50 * (i + 1), 200, -1, -1),
                                             text=location[0],
                                             manager=self.ui_manager))

    def hide(self):
        self.people_selection_list.hide()
        for button in self.location_buttons:
            button.hide()

    def show(self):
        for button in self.location_buttons:
            button.show()

    def _on_click_location(self):
        self.people_selection_list.set_item_list(self.game_settings.settings["people"].keys())
        self.people_selection_list.rebuild()
        self.people_selection_list.show()

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button in self.location_buttons:
                if event.ui_element == button:
                    self.chosen_location = button.text
                    self._on_click_location()
