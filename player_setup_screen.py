import pygame
import pygame_gui
import sys


class PlayerSetupScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.welcome_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 10), (125, 50)),
                                                         text="Who are you?", manager=self.ui_manager)
        self.name_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (100, 50)),
                                                         text="Your name:", manager=self.ui_manager)
        self.player_name_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 100), (100, 50)), manager=self.ui_manager)

        self.surname_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((80, 200), (120, 50)),
                                                         text="Your surname:", manager=self.ui_manager)
        self.player_surname_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 200), (100, 50)), manager=self.ui_manager)

        self.next_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 300), (150, 50)),
                                                                  text='Next', manager=self.ui_manager)
        self.bg = (pygame.transform.scale(pygame.image.load("background.jpg"), self.screen_options.resolution))
        #self.player_surname_input.text = self.game_settings.player_surname
        self.content = [[self.welcome_text], [self.name_text, self.player_name_input],
                        [self.surname_text, self.player_surname_input], [self.next_button]]
        self.hide()

    def refresh(self):
        for index, line_list in enumerate(self.content):
            if len(line_list) == 1:
                line_list[0].relative_rect.centerx = self.screen_options.resolution[0] / 2
                line_list[0].relative_rect.y = self.screen_options.resolution[1] * ((index + 1) / len(self.content))
                line_list[0].rebuild()
            else:
                for i, line_element in enumerate(line_list):
                    line_element.relative_rect.centerx = self.screen_options.resolution[0] * ((i + 1) / 4)
                    line_element.relative_rect.y = self.screen_options.resolution[1] * ((index + 1) / len(self.content))
                    line_element.rebuild()

    def hide(self):
        for line_list in self.content:
            for item in line_list:
                item.hide()

    def show(self):
        self.refresh()
        self.background_surface.blit(self.bg, (0, 0))
        pygame.display.set_caption("Your name")
        for line_list in self.content:
            for item in line_list:
                item.show()

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


    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_button:
                self._on_click_next()
