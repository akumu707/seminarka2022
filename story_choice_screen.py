import pygame
import pygame_gui
from pygame_gui.core import ObjectID

from screen_base import ScreenBase


class StoryChoiceScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.add_label("Choose", (350, 100, -1, -1,))
        self.choice_list = self.add_selection_list((320, 200, 120, 200), self.game_settings.file.keys(), ObjectID(class_id='@selection_list_item'))
        self.add_button('Submit', (350, 350, -1, -1), self._on_click_submit)
        self.add_button('Back', (290, 350, -1, -1), self._on_click_back)
        self.add_button('Save', (430, 350, -1, -1), self._on_click_save)
        self.add_bg("resources/images/background-choice.jpg")
        self.hide()

    def _locked_eps(self):
        ep_dict = {}
        for ep in self.game_settings.this_tree:
            if not (ep["name"]) in ep_dict.keys():
                ep_dict[ep["name"]] = []
                for key in ep["requirements"]:
                    if key == "relationship":
                        if self.game_settings.settings["relationship"][ep["requirements"][key][0]] < \
                                ep["requirements"][key][1]:
                            ep_dict[ep["name"]].append((ep["requirements"][key][0], ep["requirements"][key][1]))
                    elif key == "level":
                        if not self.game_settings.progress["levels"][ep["requirements"][key][0]][
                         ep["requirements"][key][1]]:
                            ep_dict[ep["name"]].append((ep["requirements"][key][0], ep["requirements"][key][1]))
                    else:
                        for k in self.game_settings.progress["scenes"][key].keys():
                            if k == ep["requirements"][key] and not self.game_settings.progress["scenes"][key][k]:
                                ep_dict[ep["name"]].append((key, k))
        return ep_dict

    def set_choice_list(self):
        no_id_item_list = []
        if self.game_settings.chosen_story is None:
            no_id_item_list=(self.game_settings.file.keys())
        else:
            self.locked_eps = self._locked_eps()
            for ep in self.game_settings.this_tree:
                if len(self.locked_eps[ep["name"]]) ==0:
                    no_id_item_list.append(ep["name"])
                else:
                    no_id_item_list.append((ep["name"], "#locked"))
        self.choice_list.set_item_list(no_id_item_list)

    def _on_click_save(self):
        self.game_settings.chosen_story = None
        self.screen_options.show(self.screen_options.save_screen)

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
                        requirements_string = ""
                        for req in self.locked_eps[ep["text"]]:
                            requirements_string += str(req[0]) + " - "+str(req[1])+"\n"
                        self.confirm = pygame_gui.windows.UIConfirmationDialog(rect=pygame.Rect(300, 300, -1, -1),
                                                                               manager=self.ui_manager,
                                                                               action_long_desc= "This episode is locked. The following actions are needed to proceed: \n" +requirements_string,
                                                                               action_short_name="Ok",
                                                                               window_title="Locked", blocking=False,
                                                                               visible=1)
                        self.confirm.on_moved_to_front()
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

    def show(self):
        self.refresh()
        self.background_surface.blit(self.bg, (0, 0))
        self.set_choice_list()
        for w in self.widgets:
            w[0].show()