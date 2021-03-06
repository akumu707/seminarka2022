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
        self.next_line_number = 0
        self.background_surface = background_surface

        self.person_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 450), (100, 50)), #make a percentage for fullscreen
                                                          text="", manager=self.ui_manager, object_id=ObjectID(object_id='#episode_label'))
        self.line_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 500, 800, 100),
                                                         text="", manager=self.ui_manager, object_id=ObjectID(object_id='#episode_label'))
        self.relationship_update = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (300, 300)),
                                                               # make a percentage for fullscreen
                                                               text="",
                                                               manager=self.ui_manager,
                                                               object_id=ObjectID(object_id='#episode_label'))

        self.content = [self.person_name, self.line_text]
        self.choice_buttons = []
        self.option_lines = []
        self.refresh()
        self.hide()

    def refresh(self):
        self.line_text.relative_rect.y = ((self.screen_options.resolution[1])/6)*5
        self.line_text.rebuild()

    def set_elements_for_new_line(self, line: dict):
        self.relationship_update.hide()
        keys = line.keys()
        if len(keys)==1 or "relationship" in keys:
            for key in keys:
                if key == "background":
                    self.bg = (pygame.transform.scale(pygame.image.load(os.path.join("resources","images",line[key]+".jpg")), self.screen_options.resolution))
                elif key == "relationship":
                    self.game_settings.settings["relationship"][line[key][0]]+=line[key][1]
                    #self.relationship_update.text = "Relationship with " + line[key][0] + " improved by " + str(line[key][1])
                    #self.relationship_update.rebuild()
                    #self.relationship_update.show()
                elif key == "Nothing":
                    self.person_name.text = ""
                    self.line_text.text = line[key]
                elif key == "Player":
                    self.person_name.text = self.game_settings.settings["player name"]
                    self.line_text.text = line[key]
                else:
                    self.person_name.text = key
                    self.line_text.text = line[key]
            self.person_name.rebuild()
            self.line_text.rebuild()
        else:
            self.reset_line()
            for i, key in enumerate(line.keys()):
                self.choice_buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.screen_options.resolution[0]/(len(line.keys())+1)*(i+1), 530, -1, -1),
                                                                    text=key,
                                                                    manager=self.ui_manager, object_id=ObjectID(object_id='#episode_button')))

    def reset_line(self):
        self.person_name.text = ""
        self.line_text.text = ""
        # self.person_name.rebuild()
        # self.line_text.rebuild()

    def set_episode(self, episode_name):  #Zat??m bez kontroly dostupnosti
        for ep in self.game_settings.this_tree:
            if ep["name"] == episode_name:
                self.episode = ep["story"]
                break
        self.set_elements_for_new_line(self.episode[self.next_line_number])

    def hide(self):
        self.person_name.hide()
        self.line_text.hide()
        self.relationship_update.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        self.person_name.show()
        self.line_text.show()


    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.choice_buttons==[]:
            self.relationship_update.kill()
            if self.option_lines == []:
                self.next_line_number += 1
                if not self.next_line_number == len(self.episode):
                    self.set_elements_for_new_line(self.episode[self.next_line_number])
                    self.show()
                else:
                    self.next_line_number = 0
                    self.episode = []
                    self.reset_line()
                    for i, ep in enumerate(self.game_settings.file[self.game_settings.chosen_story]):
                        if ep["name"] == self.game_settings.chosen_ep:
                            ep["to read"] = False
                    self.game_settings.chosen_ep = None
                    self.screen_options.show(self.screen_options.choice_screen)
            else:
                line = self.option_lines[0]
                self.option_lines.remove(line)
                self.set_elements_for_new_line(line)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button in self.choice_buttons:
                if event.ui_element == button:
                    for i in self.choice_buttons:
                        i.kill()
                    self.choice_buttons=[]
                    self.option_lines = self.episode[self.next_line_number][button.text]
                    line = self.option_lines[0]
                    self.option_lines.remove(line)
                    self.set_elements_for_new_line(line)