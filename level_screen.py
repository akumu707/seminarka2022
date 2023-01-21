import random

from screen_base import ScreenBase
import pygame


class LevelScreen(ScreenBase):
    def __init__(self, screen_options, ui_manager, game_settings, background_surface):
        ScreenBase.__init__(self, screen_options, ui_manager, game_settings, background_surface)

        self.sprite = pygame.Rect(200, 200, 50, 50)
        self.add_bg("resources/images/universal.jpg")
        self.hide()

    def hide(self):
        for w in self.widgets:
            w[0].hide()

    def show(self):
        self.refresh()
        self.background_surface.blit(self.bg, (0, 0))
        for w in self.widgets:
            w[0].show()

    def _create_sprite(self, x, y):
        self.sprite = self.sprite_image.get_rect()
        self.sprite.x = x
        self.sprite.y = y
        self.background_surface.blit(self.sprite_image, self.sprite)

    def _create_exit(self, x, y):
        self.exit = self.exit_image.get_rect()
        self.exit.x = x
        self.sprite.y = y
        self.background_surface.blit(self.exit_image, self.exit)

    def start_level(self, char, location):
        self.screen_options.show(self.screen_options.level_screen)
        self.sprite_image = pygame.image.load("resources/images/" + self.game_settings.settings["people"][char][1]).convert_alpha()
        self.exit_image = pygame.image.load("resources/images/exit.png").convert_alpha()
        # Create a rect with the size of the image.
        self._create_sprite(200, 300)
        self.exit_x = random.randint(0, self.screen_options.resolution[0])
        self.exit_y = random.randint(0, self.screen_options.resolution[1])
        self._create_exit(self.exit_x, self.exit_y)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_exit(self.exit_x, self.exit_y)
                self._create_sprite(x - 50, y)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if event.key == pygame.K_RIGHT:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_exit(self.exit_x, self.exit_y)
                self._create_sprite(x + 50, y)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if event.key == pygame.K_DOWN:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_exit(self.exit_x, self.exit_y)
                self._create_sprite(x, y + 50)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if event.key == pygame.K_UP:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_exit(self.exit_x, self.exit_y)
                self._create_sprite(x, y - 50)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if self.sprite.colliderect(self.exit):
                self.screen_options.show(self.screen_options.exploration_screen)