import pygame
import pygame_gui
import os

from screen_base import ScreenBase


class SaveScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Name your saved game:", (1/4, 1/3, -1, -1))
        self.file_name_input = self.add_text_entry_line((1/2, 190/600, 1/8, 5/60))
        self.add_button('Continue', (25/80, 25/60, -1, -1), self._on_click_continue)
        self.add_button('Back', (35/80, 25/60, -1, -1),
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
        super().process_event(event)
        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            self._on_click_confirm()