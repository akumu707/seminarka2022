import pygame
import pygame_gui


class WelcomeScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface


        self.welcome_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(100, self.screen_options.resolution[1]/8, -1, -1,), text="Welcome", manager=self.ui_manager)
        self.start_new_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, (self.screen_options.resolution[1]/8)*2, -1, -1),
                                                           text='Start new game',
                                                           manager=self.ui_manager)
        self.load_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, (self.screen_options.resolution[1]/8)*3, -1, -1),
                                                                 text='Load game',
                                                                 manager=self.ui_manager)

        self.end_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(400, self.screen_options.resolution[1]*(4/8),-1,-1),
                                                                text='End',
                                                                manager=self.ui_manager)
        self.bg = (pygame.transform.scale(pygame.image.load("resources/images/background.jpg"), self.screen_options.resolution))

        self.content = [self.welcome_text, self.start_new_button, self.load_button, self.end_button]
        self.refresh()
        self.hide()

    def refresh(self):
        center_x = self.screen_options.resolution[0] / 2
        for index, element in enumerate(self.content):
            element.relative_rect.centerx = center_x
            element.relative_rect.y = (self.screen_options.resolution[1]/8)*(index+1)
            element.rebuild()

    def hide(self):
        for element in self.content:
            element.hide()


    def show(self):
        pygame.display.set_caption("Welcome")
        self.refresh()
        for element in self.content:
            element.show()
        self.background_surface.blit(self.bg, (0, 0))


    def _on_click_start(self):
        self.screen_options.show(self.screen_options.player_setup_screen)

    def _on_click_load(self):
        self.screen_options.show(self.screen_options.load_screen)


    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_new_button:
                self._on_click_start()
            if event.ui_element == self.load_button:
                self._on_click_load()
            if event.ui_element == self.end_button:
                #MY_QUIT = pygame.event.Event(pygame.USEREVENT+1)
                #pygame.event.post(MY_QUIT)
                pass




