import pygame
import pygame_gui
import sys


class PlayerSetupScreen:
    def __init__(self, screen_options, ui_manager, game_settings):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings

        self.welcome_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((200, 10), (125, 50)),
                                                         html_text="Who are you?", manager=self.ui_manager)
        self.name_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((100, 100), (100, 50)),
                                                         html_text="Your name:", manager=self.ui_manager)
        self.player_name_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 100), (100, 50)), manager=self.ui_manager)
        self.player_name_submit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 100), (150, 50)),text='Submit', manager=self.ui_manager)

        self.surname_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((80, 200), (120, 50)),
                                                         html_text="Your surname:", manager=self.ui_manager)
        self.player_surname_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 200), (100, 50)), manager=self.ui_manager)
        self.player_surname_submit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 200), (150, 50)),
                                                               text='Submit', manager=self.ui_manager)

        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 300), (150, 50)),
                                                                  text='Back', manager=self.ui_manager)
        #self.player_surname_input.text = self.game_settings.player_surname

        self.hide()

    def hide(self):
        self.welcome_text.hide()
        self.name_text.hide()
        self.player_name_input.hide()
        self.player_name_submit.hide()
        self.surname_text.hide()
        self.player_surname_input.hide()
        self.player_surname_submit.hide()
        self.back_button.hide()

    def show(self):
        self.welcome_text.show()
        self.name_text.show()
        self.player_name_input.show()
        self.player_name_submit.show()
        self.surname_text.show()
        self.player_surname_input.show()
        self.player_surname_submit.show()
        self.back_button.show()

    def _on_click_name_submit(self):
        if self.player_name_input.text == "":
            pass
        else:
            self.game_settings.player_name = self.player_name_input.get_text()

    def _on_click_surname_submit(self):
        if self.player_surname_input.text == "":
            pass
        else:
            self.game_settings.player_surname = self.player_surname_input.get_text()

    def _on_click_back(self):
        self.screen_options.show(self.screen_options.welcome_screen)

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.player_name_submit:
                self._on_click_name_submit()
            if event.ui_element == self.player_surname_submit:
                self._on_click_surname_submit()
            if event.ui_element == self.back_button:
                self._on_click_back()
