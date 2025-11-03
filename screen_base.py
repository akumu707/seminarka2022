import pygame
import pygame_gui


class ScreenBase:
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        self.screen_options = screen_options
        self.ui_manager = ui_manager
        self.game_settings = game_settings
        self.background_surface = background_surface
        self.buttons = []
        self.other_widgets = []
        self.w_rects = []

    def add_button(self, text, rect, on_click):
        rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        button = pygame_gui.elements.UIButton(relative_rect=rect,
                                              text=text,
                                              manager=self.ui_manager)
        self.buttons.append((button, on_click))
        self.w_rects.append(rect)

    def add_label(self, text, rect):
        rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        label = pygame_gui.elements.UILabel(relative_rect=rect,
                                            text=text,
                                            manager=self.ui_manager)
        self.other_widgets.append(label)
        self.w_rects.append(rect)
        return label

    def add_text_entry_line(self, rect):
        text_entry_line = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(rect[0], rect[1], rect[2], rect[3]), manager=self.ui_manager)
        self.other_widgets.append(text_entry_line)
        self.w_rects.append(rect)
        return text_entry_line

    def add_selection_list(self, rect, item_list, object_id=None):
        if object_id is None:
            selection_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect
            (rect[0], rect[1], rect[2], rect[3]),
                                                                 manager=self.ui_manager, item_list=item_list,
                                                                 starting_height=150)
        else:
            selection_list = pygame_gui.elements.UISelectionList(
                relative_rect=pygame.Rect(rect[0], rect[1], rect[2], rect[3]),
                manager=self.ui_manager, item_list=item_list, object_id=object_id)
        self.other_widgets.append(selection_list)
        return selection_list

    def add_bg(self, bg_path):
        self.bg = (pygame.transform.scale(pygame.image.load(bg_path),
                                          self.screen_options.resolution))

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for (button, todo) in self.buttons:
                if event.ui_element == button:
                    todo()

    def hide(self):
        for b, _ in self.buttons:
            b.hide()
        for w in self.other_widgets:
            w.hide()

    def show(self):
        self.refresh()
        self.background_surface.blit(self.bg, (0, 0))
        for b, _ in self.buttons:
            b.show()
        for w in self.other_widgets:
            w.show()

    def refresh(self):
        pass

