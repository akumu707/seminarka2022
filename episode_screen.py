import pygame
import pygame_gui

class EpisodeScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.episode = []
        self.line_number = 0
        self.background_surface = background_surface

        #self.background = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((0, 0), (800, 600)),
                                                   #   image_surface=background_surface, manager=self.ui_manager)
        self.person_name = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, 450), (100, 50)), #make a percentage for fullscreen
                                                          html_text="", manager=self.ui_manager)
        self.line_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, 500), (800, 100)),
                                                         html_text="", manager=self.ui_manager)

        self.hide()

    def set_elements_for_new_line(self, line: dict):
        keys = line.keys()
        for key in keys:
            if key == "background":
                self.bg = (pygame.transform.scale(pygame.image.load(line[key]+".png"), self.screen_options.resolution))
            elif key == "Nothing":
                self.person_name.html_text = ""
                self.line_text.html_text = line[key]
            elif key == "Player":
                self.person_name.html_text = self.game_settings.player_name
                self.line_text.html_text = line[key]
            else:
                self.person_name.html_text = key
                self.line_text.html_text = line[key]
        self.person_name.rebuild()
        self.line_text.rebuild()


    def set_episode(self, episode_name):  #Zatím bez kontroly dostupnosti
        for ep in self.game_settings.this_tree:
            if ep["name"] == episode_name:
                self.episode = ep["story"]
                break
        self.set_elements_for_new_line(self.episode[self.line_number])

    def hide(self):
        self.person_name.hide()
        self.line_text.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        self.person_name.show()
        self.line_text.show()


    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.line_number+=1
            if not self.line_number==len(self.episode):
                self.set_elements_for_new_line(self.episode[self.line_number])
                self.show()
            else:
                self.line_number=0
                self.episode = []
                self.game_settings.chosen_ep = None
                self.screen_options.show(self.screen_options.choice_screen)