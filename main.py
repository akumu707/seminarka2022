import pygame
from game import GameApp
from ui import UI
from writer import Writer
from GameSettings import GameSettings
from scene import Scene


#tree = Tree()
#writer = Writer()
#ui = UI(writer)
#scene = Scene(writer)

#if __name__ == '__main__':
 #   app = Game()
   # app.run()
#game = Game(ui, tree, scene)
#game.run()

app = GameApp()
app.run()