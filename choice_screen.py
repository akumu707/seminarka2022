import pygame
import pygame_gui
import sys

class ChoiceScreen:
    def __init__(self, screen_options, ui_manager, game_settings):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings

        self.choice_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((200, 10), (100, 50)),
                                                          html_text="Choose", manager=self.ui_manager)
        self.choice_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((200, 100), (200, 100)), manager=ui_manager, item_list = self.game_settings.file.keys())
        self.submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 200), (150, 50)),
                                                          text='Submit',
                                                          manager=self.ui_manager)
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 200), (150, 50)),
                                                          text='Start',
                                                          manager=self.ui_manager)
        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 300), (150, 50)),
                                                          text='Back',
                                                          manager=self.ui_manager)
        self.hide()

    def set_choice_list(self):
        if self.game_settings.chosen_story==None:
            self.choice_list.set_item_list(self.game_settings.file.keys())
        else:
            ep_names = []
            for ep in self.game_settings.this_tree:
                ep_names.append(ep["name"])
            self.choice_list.set_item_list(ep_names)

    def _on_click_submit(self):
        self.game_settings.chosen_story = self.choice_list.get_single_selection()
        if not self.game_settings.chosen_story==None:
            self.game_settings.find_this_tree(self.game_settings.chosen_story)
            self.set_choice_list()
            self.submit_button.hide()
            self.start_button.show()

    def _on_click_start(self):
        self.game_settings.chosen_ep = self.choice_list.get_single_selection()
        if not self.game_settings.chosen_ep == None:
            self.screen_options.episode_screen.set_episode(self.game_settings.chosen_ep)
            self.screen_options.show(self.screen_options.episode_screen)


    def _on_click_back(self):
        if self.game_settings.chosen_story == None:
            self.screen_options.show(self.screen_options.welcome_screen)
        else:
            self.game_settings.chosen_story = None
            self.set_choice_list()
            self.start_button.hide()
            self.submit_button.show()

    def hide(self):
        self.choice_text.hide()
        self.choice_list.hide()
        self.submit_button.hide()
        self.start_button.hide()
        self.back_button.hide()

    def show(self):
        pygame.display.set_caption("Choose")
        self.choice_text.show()
        self.set_choice_list()
        self.choice_list.show()
        self.back_button.show()
        if not self.game_settings.chosen_story==None:
            self.start_button.show()
        else:
            self.submit_button.show()

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.submit_button:
                self._on_click_submit()
            if event.ui_element == self.start_button:
                self._on_click_start()
            if event.ui_element == self.back_button:
                self._on_click_back()