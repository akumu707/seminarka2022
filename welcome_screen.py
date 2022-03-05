import pygame
import pygame_gui
import sys


class WelcomeScreen:
    def __init__(self, screen_options, ui_manager, game_settings):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings


        self.welcome_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((200, 10), (100, 50)), html_text="Welcome", manager=self.ui_manager)
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 100), (100, 50)), #smh nadesignovat
                                                           text='Start',
                                                           manager=self.ui_manager)
        self.player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 200), (150, 50)),
                                                                 text='Player Info',
                                                                 manager=self.ui_manager)

        self.end_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 300),(150,50)),
                                                                text='End',
                                                                manager=self.ui_manager)

        self.hide()

    def hide(self):
        self.welcome_text.hide()
        self.start_button.hide()
        self.player_button.hide()
        self.end_button.hide()

    def show(self):
        pygame.display.set_caption("Welcome")
        self.welcome_text.show()
        self.start_button.show()
        self.player_button.show()
        self.end_button.show()


    def _on_click_start(self):
        self.screen_options.show(self.screen_options.choice_screen)


    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_button:
                self._on_click_start()
            if event.ui_element == self.player_button:
                pass#self._on_single_player_click()
            if event.ui_element == self.end_button:
                pass#find a way to kill it finally lmao



