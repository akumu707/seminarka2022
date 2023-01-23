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
            self.location_buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100*(i+1), 200, -1, -1),
                                                                      text=location[0],
                                                                      manager=self.ui_manager))
        self.people_buttons = []
        for i, person in enumerate(self.game_settings.settings["people"]):
            self.people_buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100*(i+1), 200, -1, -1),
                                                          text=person,
                                                          manager=self.ui_manager))
        self.people_selection_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect(200, 100, 100, 100),
                                                                         manager=ui_manager, item_list=[],
                                                                         object_id=ObjectID(class_id='@selection_list_item'))
        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100, 300, -1, -1),
                                                          text="Back",
                                                          manager=self.ui_manager)
        self.bg = pygame.transform.scale(pygame.image.load("resources/images/background-choice.jpg"),
                                         self.screen_options.resolution)
        self.hide()

    def refresh(self):
        for i, location in enumerate(self.game_settings["locations"]):
            self.location_buttons.append(
                pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100 * (i + 1), 200, -1, -1),
                                             text=location[0],
                                             manager=self.ui_manager))

    def hide(self):
        self.people_selection_list.hide()
        for button in self.location_buttons:
            button.hide()
        for button in self.people_buttons:
            button.hide()
        self.back_button.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        for button in self.location_buttons:
            button.show()
        self.back_button.show()

    def _on_click_location(self):
        for button in self.location_buttons:
            button.hide()
        for button in self.people_buttons:
            button.show()

    def _on_click_person(self):
        self.screen_options.level_screen.start_level(self.chosen_person, self.chosen_location)

    def _on_click_back(self):
        self.screen_options.show(self.screen_options.choice_screen)

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button in self.location_buttons:
                if event.ui_element == button:
                    self.chosen_location = button.text
                    self._on_click_location()
            for button in self.people_buttons:
                if event.ui_element == button:
                    self.chosen_person = button.text
                    self._on_click_person()
            if event.ui_element == self.back_button:
                self._on_click_back()