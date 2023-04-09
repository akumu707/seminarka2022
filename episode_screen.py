import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import os

class EpisodeScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.episode = []
        self.line_path = [0]
        self.background_surface = background_surface

        self.person_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 450), (100, 50)), #make a percentage for fullscreen
                                                          text="", manager=self.ui_manager, object_id=ObjectID(object_id='#episode_label'))
        #self.line_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 500, 800, 100),
                                                       #  text="", manager=self.ui_manager, object_id=ObjectID(object_id='#episode_label'))
        self.line_labels = []
        self.end_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(300, 200, 500, 500),
                                                    text="", manager=self.ui_manager,
                                                    object_id=ObjectID(object_id='#end_text_label'))
        self.end_context = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(200, 300, 100, 100),
                                                       text="", manager=self.ui_manager,
                                                       object_id=ObjectID(object_id='#end_context_label'))
        self.relationship_update = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(400, 0, -1, -1),
                                                               # make a percentage for fullscreen
                                                               text="Tamara",
                                                               manager=self.ui_manager,
                                                               object_id=ObjectID(object_id='#episode_label'))

        self.choice_buttons = []
        self.option_lines = []
        self.END_EVENT = pygame.USEREVENT + 1
        self.hide()


    def line_split(self, line):
        last_y = 480
        one_line = ""
        line_words = line.split()
        self.line_labels = []
        for word in line_words:
            if len(one_line)+len(word)<100:
                one_line+=" "+word
            else:
                self.line_labels.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, last_y+20, 800, 100),
                                                             text=one_line, manager=self.ui_manager,
                                                             object_id=ObjectID(object_id='#episode_label')))
                one_line = word
                last_y+=20
        if one_line != "":
            self.line_labels.append(pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, last_y + 20, 800, 100),
                                                                text=one_line, manager=self.ui_manager,
                                                                object_id=ObjectID(object_id='#episode_label')))
        for label in self.line_labels:
            label.show()

    def set_elements_for_new_line(self, line: dict):
        self.person_name.hide()
        self.relationship_update.hide()
        for line_label in self.line_labels:
            line_label.kill()
        keys = line.keys()
        if len(keys) == 1 and type(line[list(keys)[0]]) == str or "relationship" in keys or "End" in keys or "unlock" in keys:
            for key in keys:
                if key == "unlock":
                    self.game_settings.settings["people"][line[key]][0] = True
                elif key == "background":
                    self.bg = (pygame.transform.scale(pygame.image.load(os.path.join("resources","images",line[key]+".jpg")), self.screen_options.resolution))
                elif key == "relationship":
                    if not self.game_settings.progress["scenes"][self.game_settings.chosen_story][self.game_settings.chosen_ep]:
                        self.game_settings.settings["relationship"][line[key][0]] += line[key][1]
                        self.relationship_update.text = "Relationship with " + line[key][0] + " improved by " + str(line[key][1])
                        self.relationship_update.rebuild()
                        self.relationship_update.show()
                elif key == "Nothing":
                    self.person_name.text = ""
                    self.line_split(line[key])
                elif key == "Player":
                    self.person_name.text = self.game_settings.settings["player name"]
                    self.line_split(line[key])
                elif key == "End":
                    self.background_surface.fill(self.ui_manager.get_theme().get_colour('dark_bg'))
                    self.person_name.hide()
                    for line_label in self.line_labels:
                        line_label.kill()
                    self.end_text.text = line[key][0]
                    self.end_context.text = line[key][1]
                    self.end_text.rebuild()
                    self.end_context.rebuild()
                    self.end_text.show()
                    self.end_context.show()
                else:
                    self.person_name.text = key
                    self.line_split(line[key])
            self.person_name.rebuild()
            if self.person_name.text != "":
                self.person_name.show()
            for line_label in self.line_labels:
                line_label.show()
        else:
            self.reset_line()
            if "Locked" in keys:
                added = False
                for key in line["Locked"]["Requirements"]:
                    if key == "relationship":
                        if self.game_settings.settings["relationship"][line["Locked"]["Requirements"][key][0]] < \
                                line["Locked"]["Requirements"][key][1]:
                            added = True
                            self.line_path.append("other")
                            self.line_path.append(0)
                            self.set_elements_for_new_line(self._get_line())
                            break
                    elif key == "level":
                        if not self.game_settings.progress["levels"][line["Locked"]["Requirements"][key][0]][
                         line["Locked"]["Requirements"][key][1]]:
                            added = True
                            self.line_path.append("other")
                            self.line_path.append(0)
                            self.set_elements_for_new_line(self._get_line())
                            break
                    else:
                        for k in self.game_settings.progress["scenes"][key].keys():
                            if k == line["Locked"]["Requirements"][key] and not self.game_settings.progress["scenes"][key][k]:
                                added = True
                                self.line_path.append("other")
                                self.line_path.append(0)
                                self.set_elements_for_new_line(self._get_line())
                                break
                if not added:
                    self.line_path.append("Locked")
                    self.line_path.append("story")
                    self.line_path.append(0)
                    self.set_elements_for_new_line(self._get_line())

            else:
                if self.game_settings.progress["choices"][self.game_settings.chosen_story][self.game_settings.chosen_ep]:
                    for key in line.keys():
                        if key in self.game_settings.progress["choices"][self.game_settings.chosen_story][self.game_settings.chosen_ep]:
                            self.choice_buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                self.screen_options.resolution[0] / 2, 530, -1, -1),
                                                                                    text=key,
                                                                                    manager=self.ui_manager,
                                                                                    object_id=ObjectID(
                                                                                        object_id='#episode_button')))
                if not self.choice_buttons:
                    for i, key in enumerate(line.keys()):
                        self.choice_buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            self.screen_options.resolution[0]/(len(line.keys())+1)*(i+1), 530, -1, -1),
                                                                                text=key,
                                                                                manager=self.ui_manager,
                                                                                object_id=ObjectID(
                                                                                    object_id='#episode_button')))

    def reset_line(self):
        self.person_name.text = ""
        for line_label in self.line_labels:
            line_label.show()
        # self.person_name.rebuild()
        # self.line_text.rebuild()

    def _get_line(self):
        line = self.episode
        for path_part in self.line_path:
            line = line[path_part]
        return line

    def _get_button_path(self):
        button_path = line = self.episode
        for i, path_part in enumerate(self.line_path):
            if i+1 == len(self.line_path):
                pass
            else:
                button_path = button_path[path_part]
        return button_path

    def set_episode(self, episode_name):  # Zatím bez kontroly dostupnosti
        for ep in self.game_settings.this_tree:
            if ep["name"] == episode_name:
                self.episode = ep["story"]
                break
        self.set_elements_for_new_line(self._get_line())

    def hide(self):
        self.person_name.hide()
        for label in self.line_labels:
            label.kill()
        self.relationship_update.hide()
        self.end_text.hide()
        self.end_context.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.choice_buttons == []:
            self.relationship_update.hide()
            if len(self.line_path) == 1:
                self.line_path[0] += 1
                if not self.line_path[0] == len(self.episode):
                    self.set_elements_for_new_line(self._get_line())
                    self.show()
                else:
                    self.line_path[0] = 0
                    self.episode = []
                    self.reset_line()
                    for key in self.game_settings.progress["scenes"][self.game_settings.chosen_story].keys():
                        if key == self.game_settings.chosen_ep:
                            self.game_settings.progress["scenes"][self.game_settings.chosen_story][key] = True
                    self.game_settings.chosen_ep = None
                    self.screen_options.show(self.screen_options.story_choice_screen)
            else:
                self.line_path[-1]+=1
                if not self.line_path[-1] == len(self._get_button_path()):
                    self.set_elements_for_new_line(self._get_line())
                    self.show()
                else:
                    self.line_path.pop()
                    self.line_path.pop()
                    if type(self.line_path[-1]) == str:
                        self.line_path.pop()
                    #TODO: event raise

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button in self.choice_buttons:
                if event.ui_element == button:
                    if not button.text in self.game_settings.progress["choices"][self.game_settings.chosen_story][self.game_settings.chosen_ep]:
                        self.game_settings.progress["choices"][self.game_settings.chosen_story][self.game_settings.chosen_ep].append(button.text)
                    for i in self.choice_buttons:
                        i.kill()
                    self.choice_buttons = []
                    self.line_path.append(button.text)
                    self.line_path.append(0)
                    self.set_elements_for_new_line(self._get_line())