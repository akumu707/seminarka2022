import pygame
import pygame_gui


class SaveScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.file_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(100, 200, -1, -1, ),
                                                       text="Name your saved game:", manager=self.ui_manager)
        self.file_name_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 200, 100, 100),
                                                               manager=ui_manager)
        self.continue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(400, 300, -1, -1),
                                                            text='Continue',
                                                            manager=self.ui_manager)
        self.bg = (pygame.transform.scale(pygame.image.load("background.jpg"), self.screen_options.resolution))
        self.content = [self.file_text, self.file_name_input, self.continue_button]
        self.hide()

    def refresh(self):
        pass

    def hide(self):
        for element in self.content:
            element.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        pygame.display.set_caption("Choose")
        for element in self.content:
            element.show()
        self.refresh()

    def _on_click_continue(self):
        if not self.file_name_input.text == None:
            self.game_settings.save_game(self.file_name_input.text)
            self.screen_options.show(self.screen_options.welcome_screen)


    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.continue_button:
                self._on_click_continue()