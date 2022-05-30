import pygame
import pygame_gui
import os



class LoadScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.choice_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(100, 200, -1, -1, ),
                                                       text="Choose a file:", manager=self.ui_manager)
        self.choice_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect(100, 200, 100, 100),
                                                               manager=ui_manager, item_list=[])
        self.continue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(400, 300, -1, -1),
                                                            text='Continue',
                                                            manager=self.ui_manager)
        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100, 200, -1, -1),
                                                        text='Back',
                                                        manager=self.ui_manager)
        self.bg = (pygame.transform.scale(pygame.image.load("background.jpg"), self.screen_options.resolution))
        self.content = [self.choice_text, self.choice_list, self.continue_button, self.back_button]
        self.hide()

    def refresh(self):
        item_list = []
        for f in os.listdir(r"Saved"):
            item_list.append(f)  # i v save screen
        self.choice_list.set_item_list(item_list)
        self.choice_list.rebuild()

    def hide(self):
        for element in self.content:
            element.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        pygame.display.set_caption("Choose")
        self.refresh()
        for element in self.content:
            element.show()

    def _on_click_continue(self):
        if not self.choice_list.get_single_selection()==None:
            self.game_settings.load_existing_game(self.choice_list.get_single_selection())
            self.screen_options.show(self.screen_options.choice_screen)

    def _on_click_back(self):
        self.screen_options.show(self.screen_options.welcome_screen)

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.continue_button:
                self._on_click_continue()
            if event.ui_element == self.back_button:
                self._on_click_back()