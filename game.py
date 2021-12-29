import sys
import constants

import pygame
from pygame.locals import *

class Game:
    def __init__(self, ui, tree, scene):
        self.ui = ui
        self.tree = tree
        self.scene = scene

    def start(self):

        #
        self.go_trough_story()

    def go_trough_story(self):
        while True:
            #tree_name = self.ui.select_tree(self.tree.file.keys())
            self.tree.find_this_tree("Test story")
            self.create_environment()
            for scene in self.tree.this_tree:
                if bool(scene["to read"]):
                    self.scene.story = scene["story"]
                    self.scene.run()
                #for event in pygame.event.get():
                    #if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def create_environment(self):
        constants.DISPLAYSURF.fill(constants.WHITE)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.STORY_TEXT_RECT)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.NAME_RECT)
        pygame.display.update()
