import sys
import constants
from pgu import gui

import pygame
from pygame.locals import *

class Game:
    def __init__(self, ui, tree, scene):
        self.ui = ui
        self.tree = tree
        self.scene = scene

    def start(self):
        while True:
            app = gui.App()
            background = pygame.image.load("background.jpg")
            constants.DISPLAYSURF.blit(background, (0, 0), (0, 0, 1920, 1080))
            t = gui.Table()
            begin = gui.Button("Start")
            begin.connect(gui.CLICK, self.go_trough_story)
            t.add(begin)
            end = gui.Button("End")
            end.connect(gui.CLICK, pygame.quit, None) #háže error, ale je to tu, abych to nemusela vypínat manuálně
            t.add(end)
            app.run(t, constants.DISPLAYSURF)
        pygame.quit()
        sys.exit()

    def go_trough_story(self):
        while True:
            tree_name = self.ui.select(self.tree.file.keys())
            if not tree_name==None:
                self.tree.find_this_tree(tree_name)
                self.create_environment()
                ep_names = []
                for ep in self.tree.this_tree:
                    ep_names.append(ep["name"])
                scene = self.ui.select(ep_names)
                for ep in self.tree.this_tree:
                    if ep["name"] == scene and bool(ep["to read"]):
                        self.scene.story = ep["story"]
                        self.scene.run()
            else:
                return
                #for event in pygame.event.get():
                    #if event.type == QUIT:

    def create_environment(self):
        constants.DISPLAYSURF.fill(constants.WHITE)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.STORY_TEXT_RECT)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.NAME_RECT)
        pygame.display.update()
