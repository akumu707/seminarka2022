import pygame
from game import Game
from ui import UI
from writer import Writer
from tree import Tree
from scene import Scene

pygame.init()
FPS = pygame.time.Clock()
FPS.tick(60)

tree = Tree()
writer = Writer()
ui = UI(writer)
scene = Scene(writer)
game = Game(ui, tree, scene)
game.start()