import sys
import constants

import pygame
from pygame.locals import *

class Game:
    def __init__(self, ui, tree, scene):
        self.ui = ui
        self.tree = tree
        self.scene = scene
        self.text_rect = pygame.Rect(constants.TEXT_RECT_START_POINT, constants.TEXT_RECT_HEIGHT_WIDTH)
        self.name_rect = pygame.Rect(constants.NAME_RECT_START_POINT, constants.NAME_RECT_HEIGHT_WIDTH)

    def start(self):
        self.create_environment()
        #tree_name = self.ui.select_tree(self.tree.file.keys())
        #self.tree.find_this_tree(tree_name)
        self.go_trough_story()

    def go_trough_story(self):
        for scene in self.tree.this_tree:
            if bool(scene["to read"]):
                self.scene.story = scene["story"]
                self.scene.run()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def create_environment(self):
        constants.DISPLAYSURF.fill(constants.WHITE)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, self.text_rect)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, self.name_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()