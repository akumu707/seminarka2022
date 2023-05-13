from screen_base import ScreenBase


class ChoiceScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_button("Exploration", (350, 200, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.exploration_screen))
        self.add_button("Story", (370, 250, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.story_choice_screen))
        self.add_button("Back", (370, 300, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.welcome_screen))
        self.add_bg("resources/images/background-choice.jpg")
        self.hide()
