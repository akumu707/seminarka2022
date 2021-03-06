import pygame
import pygame_gui
from pygame_gui.core import ObjectID

from screen_base import ScreenBase


class StoryChoiceScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Choose", (350, 100, -1, -1,))
        self.choice_list = self.add_selection_list((350, 200, 100, 100), self.game_settings.file.keys(), ObjectID(class_id='@selection_list_item'))
        self.add_button('Submit', (350, 300, -1, -1), self._on_click_submit)
        self.add_button('Back', (200, 400, -1, -1), self._on_click_back)
        self.add_button('Save', (600, 400, -1, -1),
                        lambda: self.screen_options.show(self.screen_options.save_screen))
        self.add_bg("resources/images/background-choice.jpg")
        self.hide()

    def set_choice_list(self):
        no_id_item_list = []
        if self.game_settings.chosen_story is None:
            no_id_item_list=(self.game_settings.file.keys())
        else:
            for ep in self.game_settings.this_tree:
                for key in ep["requirements"]:
                    if key == "relationship":
                        if self.game_settings.settings["relationship"][ep["requirements"][key][0]]<ep["requirements"][key][1]:
                            no_id_item_list.append((ep["name"], "#locked"))
                    else:
                        for listed_episode in self.game_settings.file[key]:
                            if listed_episode["name"] == ep["requirements"][key] and listed_episode["to read"]:
                                no_id_item_list.append((ep["name"], "#locked"))
                if not (ep["name"], "#locked") in no_id_item_list:
                    no_id_item_list.append(ep["name"])
        self.choice_list.set_item_list(no_id_item_list)

    def _on_click_submit(self):
        chosen_option = self.choice_list.get_single_selection()
        if chosen_option is not None:
            if chosen_option in self.game_settings.file.keys():
                self.game_settings.chosen_story = chosen_option
                self.game_settings.find_this_tree(chosen_option)
                self.set_choice_list()
            else:
                self.game_settings.chosen_ep = chosen_option
                for ep in self.choice_list.item_list:
                    if ep["text"] == self.game_settings.chosen_ep and ep["object_id"] == "#locked":
                        return
                self.screen_options.episode_screen.set_episode(self.game_settings.chosen_ep)
                self.screen_options.show(self.screen_options.episode_screen)

    def _on_click_back(self):
        if self.game_settings.chosen_story is None:
            self.screen_options.show(self.screen_options.choice_screen)
        else:
            self.game_settings.chosen_story = None
            self.set_choice_list()
            self.refresh()

