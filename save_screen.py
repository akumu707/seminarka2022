import pygame
import pygame_gui
import os

from screen_base import ScreenBase


class SaveScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Name your saved game:", (100, 200, -1, -1))
        self.file_name_input = self.add_text_entry_line((300, 200, 100, 100))
        self.add_button('Continue', (400, 300, -1, -1), self._on_click_continue)
        self.add_button('Back', (400, 400, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.choice_screen))
        self.add_bg("resources/images/background.jpg")

        self.hide()

    def _on_click_continue(self):
        input_text = self.file_name_input.text
        item_list = []
        for f in os.listdir(os.path.join("Saved")):
            item_list.append(f)
        if input_text is not None:
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