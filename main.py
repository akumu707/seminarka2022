import pygame
from game import Game
from ui import UI
from writer import Writer
from tree import Tree
from scene import Scene

import json
pygame.init()
FPS = pygame.time.Clock()
FPS.tick(60)
#screen = pygame.display.set_mode((800, 600))
#pygame.draw.circle(screen, (0, 0, 255), (400, 300), 150)
#pygame.display.flip()

#game = Game()
#game.start()

tree = Tree()
writer = Writer()
ui = UI(writer)
scene = Scene(writer)
game = Game(ui, tree, scene)
game.start()