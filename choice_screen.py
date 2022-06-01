import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class ChoiceScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.choice_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(100, 200, -1, -1,),
                                                          text="Choose", manager=self.ui_manager)
        self.choice_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect(-500, -600, 100, 100), manager=ui_manager, item_list = self.game_settings.file.keys(), object_id=ObjectID(class_id='@selection_list_item'))
        self.submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100, 200, -1, -1),
                                                          text='Submit',
                                                          manager=self.ui_manager)
        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100, 200, -1, -1),
                                                          text='Back',
                                                          manager=self.ui_manager)
        self.save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(100, 200, -1, -1),
                                                        text='Save',
                                                        manager=self.ui_manager)
        self.bg = (pygame.transform.scale(pygame.image.load("background-choice.jpg"), self.screen_options.resolution))

        self.content = [self.choice_text, self.choice_list, self.submit_button, self.back_button, self.save_button]
        self.refresh()
        self.hide()

    def refresh(self):
        self.set_choice_list()
        center_x = self.screen_options.resolution[0] / 2
        if not self.game_settings.chosen_story==None:
            self.submit_button.text = "Start"
        else:
            self.submit_button.text = "Submit"
        for index, element in enumerate(self.content):
            element.relative_rect.centerx = center_x
            element.relative_rect.y = (self.screen_options.resolution[1] / 8) * (index+1)
            element.rebuild()

    def set_choice_list(self):
        no_id_item_list = []
        if self.game_settings.chosen_story==None:
            no_id_item_list=(self.game_settings.file.keys())
        else:
            for ep in self.game_settings.this_tree:
                for key in ep["requirements"]:
                    for listed_episode in self.game_settings.file[key]:
                        if (listed_episode["name"] == ep["requirements"][key] and listed_episode["to read"]): #lidi to je hnus tohle....
                            no_id_item_list.append((ep["name"], "#locked"))
                if not (ep["name"], "#locked")in no_id_item_list:
                    no_id_item_list.append(ep["name"])
        self.choice_list.set_item_list(no_id_item_list)

    def _on_click_submit(self):
        if self.submit_button.text == "Submit":
            self.game_settings.chosen_story = self.choice_list.get_single_selection()
            if not self.game_settings.chosen_story==None:
                self.game_settings.find_this_tree(self.game_settings.chosen_story)
                self.refresh()
        else:
            self.game_settings.chosen_ep = self.choice_list.get_single_selection()
            for ep in self.choice_list.item_list:
                if ep["text"] == self.game_settings.chosen_ep and ep["object_id"] == "#locked":
                    return
            if not self.game_settings.chosen_ep == None:
                self.screen_options.episode_screen.set_episode(self.game_settings.chosen_ep)
                self.screen_options.show(self.screen_options.episode_screen)

    def _on_click_back(self): #add warning
        if self.game_settings.chosen_story == None:
            self.screen_options.show(self.screen_options.welcome_screen)
        else:
            self.game_settings.chosen_story = None
            self.set_choice_list()
            self.refresh()

    def _on_click_save(self):
        self.screen_options.show(self.screen_options.save_screen)

    def hide(self):
        for element in self.content:
            element.hide()

    def show(self):
        self.set_choice_list()
        self.background_surface.blit(self.bg, (0, 0))
        pygame.display.set_caption("Choose")
        for element in self.content:
            element.show()
        self.refresh()

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.submit_button:
                self._on_click_submit()
            if event.ui_element == self.back_button:
                self._on_click_back()
            if event.ui_element == self.save_button:
                self._on_click_save()