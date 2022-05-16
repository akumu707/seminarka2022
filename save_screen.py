import pygame
import pygame_gui


class SaveScreen:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface

        self.bg = (pygame.transform.scale(pygame.image.load("background.jpg"), self.screen_options.resolution))
        self.content = []

    def refresh(self):
        pass

    def hide(self):
        for element in self.content:
            element.hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        pygame.display.set_caption("Choose")
        for element in self.content:
            element.show()
        self.refresh()


    def process_event(self, event):
        pass