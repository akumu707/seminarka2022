import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class ChoiceScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.exploration_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, 200, -1, -1),
                                                          text="Exploration",
                                                          manager=self.ui_manager)
        self.story_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(600, 200, -1, -1),
                                                          text="Story",
                                                          manager=self.ui_manager)

        self.hide()

    def hide(self):
        self.exploration_button.hide()
        self.story_button.hide()

    def show(self):
        self.exploration_button.show()
        self.story_button.show()

    def refresh(self):
        pass

    def _on_click_exploration(self):
        self.screen_options.show(self.screen_options.exploration_screen)

    def _on_click_story(self):
        self.screen_options.show(self.screen_options.story_choice_screen)

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.exploration_button:
                self._on_click_exploration()
            if event.ui_element == self.story_button:
                self._on_click_story()