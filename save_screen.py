import pygame
import pygame_gui
import os


class SaveScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.file_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(100, 200, -1, -1, ),
                                                       text="Name your saved game:", manager=self.ui_manager)
        self.file_name_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 200, 100, 100),
                                                               manager=self.ui_manager)
        self.continue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(400, 300, -1, -1),
                                                            text='Continue',
                                                            manager=self.ui_manager)
        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(400, 400, -1, -1),
                                                            text='Back',
                                                            manager=self.ui_manager)
        self.bg = (pygame.transform.scale(pygame.image.load("resources/images/background.jpg"), self.screen_options.resolution))
        self.content = [self.file_text, self.file_name_input, self.continue_button, self.back_button]
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
        input_text = self.file_name_input.text
        item_list = []
        for f in os.listdir(os.path.join("Saved")):
            item_list.append(f)
        if not input_text == None:
            if input_text in item_list:
                self.confirm = pygame_gui.windows.UIConfirmationDialog(rect=pygame.Rect(300, 300, 100, 100),
                                                                       manager=self.ui_manager,
                                                                       action_long_desc="This action will rewrite currently saved game. Do you wish to proceed?",
                                                                       action_short_name="Rewrite",
                                                                       window_title="Rewrite?", blocking=True,
                                                                       visible=1)
                self.confirm.on_moved_to_front()
            else:
                self.game_settings.save_game(self.file_name_input.text)
                self.screen_options.show(self.screen_options.welcome_screen)

    def _on_click_confirm(self):
        self.game_settings.save_game(self.file_name_input.text)
        self.screen_options.show(self.screen_options.welcome_screen)

    def _on_click_back(self):
        self.screen_options.show(self.screen_options.choice_screen)


    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.continue_button:
                self._on_click_continue()
            elif event.ui_element == self.back_button:
                self._on_click_back()
            else:
                self.confirm.process_event(event)
        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            self._on_click_confirm()