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
        self.exit.y = y
        self.background_surface.blit(self.exit_image, self.exit)

    def _create_wall(self, x, y):
        self.wall = self.wall_image.get_rect()
        self.wall.x = x
        self.wall.y = y
        self.background_surface.blit(self.wall_image, self.wall)

    def _create_level(self, sprite = True):
        for i, line in enumerate(self.level):
            for j, char in enumerate(line):
                if char == "w":
                    self._create_wall(self.screen_options.resolution[0]/16*j, self.screen_options.resolution[1]/12*i)
                if char == "s" and sprite:
                    self._create_sprite(self.screen_options.resolution[0]//16*j, self.screen_options.resolution[1]//12*i)
                if char == "e":
                    self._create_exit(self.screen_options.resolution[0]/16*j, self.screen_options.resolution[1]/12*i)

    def start_level(self, sp, location):
        self.screen_options.show(self.screen_options.level_screen)
        self.sprite_image = pygame.image.load(
            "resources/images/" + self.game_settings.settings["people"][sp][1]).convert_alpha()
        self.exit_image = pygame.image.load("resources/images/exit.png").convert_alpha()
        self.wall_image = pygame.image.load("resources/images/wall.png").convert_alpha()
        for i, level in enumerate(self.game_settings.progress["levels"][location]): # TODO: add opening new locations
            if not level:
                self.location = location
                self.level_number = i
                self.level = self.game_settings.levels[location][i]
                break
        self._create_level()

        # Create a rect with the size of the image.

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_level(False)
                if not self.level[y//50][x//50 - 1] == "w":
                    self._create_sprite(x - 50, y)
                else:
                    self._create_sprite(x, y)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if event.key == pygame.K_RIGHT:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_level(False)
                if not self.level[y//50][x // 50 + 1] == "w":
                    self._create_sprite(x + 50, y)
                else:
                    self._create_sprite(x, y)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if event.key == pygame.K_DOWN:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_level(False)
                if not self.level[y // 50 + 1][x // 50] == "w":
                    self._create_sprite(x, y+50)
                else:
                    self._create_sprite(x, y)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if event.key == pygame.K_UP:
                x = self.sprite.x
                y = self.sprite.y
                self.background_surface.blit(self.bg, (0, 0))
                self._create_level(False)
                if not self.level[y // 50 - 1][x // 50] == "w":
                    self._create_sprite(x, y - 50)
                else:
                    self._create_sprite(x, y)
                self.background_surface.blit(self.sprite_image, self.sprite)
            if self.sprite.colliderect(self.exit):
                self.game_settings.progress["levels"][self.location][self.level_number] = True
                self.screen_options.show(self.screen_options.exploration_screen)