import pygame
import pygame_gui


class ScreenBase:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface
        self.widgets = []

    def add_button(self, text, rect, on_click):
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(rect[0], rect[1], rect[2], rect[3]),
                                              text=text,
                                              manager=self.ui_manager)
        self.widgets.append((button, on_click))

    def add_label(self, text, rect):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(rect[0], rect[1], rect[2], rect[3]),
                                              text=text,
                                              manager=self.ui_manager)
        self.widgets.append((label, None)) #to je hnus, velebnosti
        return label

    def add_text_entry_line(self, rect):
        text_entry_line = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(rect[0], rect[1], rect[2], rect[3]), manager=self.ui_manager)
        self.widgets.append((text_entry_line, None))  # to je hnus, velebnosti podruhe
        return text_entry_line

    def add_bg(self, bg_path):
        self.bg = (pygame.transform.scale(pygame.image.load(bg_path),
                                          self.screen_options.resolution))

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for (ui_element, todo) in self.widgets:
                if event.ui_element == ui_element:
                    todo()

    def hide(self):
        for w in self.widgets:
            w[0].hide()

    def show(self):
        self.background_surface.blit(self.bg, (0, 0))
        for w in self.widgets:
            w[0].show()

    def refresh(self):
        pass

