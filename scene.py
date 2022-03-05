import pygame
import constants
from pgu import gui

import guiStuff
from guiStuff import LogDialog

class Scene:
    def __init__(self, writer):
        self.story = {}
        self.writer = writer

    def run(self):
        app = gui.App()
        t=gui.Table()
        td_style = {'padding_left': 1800, 'padding_down':1500} #for next buttons
        app.connect(gui.CLICK, app.quit, None)
        #quit=gui.Button("Quit")
        #quit.connect(gui.CLICK, pygame.quit, None) #needs to be changed, if the system doesnt open new pygame window for every scene
        #t.td(quit, style=td_style)
        log = gui.Button("Log")
        log_app = gui.App()
        log_t = gui.Table()
        log_dialog = guiStuff.LogDialog(self.story)
        log_t.tr()
        log_t.td(log_dialog)

        log.connect(gui.CLICK, log_app.run, log_t)
        close = gui.Button("Close")
        close.connect(gui.CLICK, log_app.quit)
        log_t.tr()
        log_t.td(close)
        t.tr()
        t.td(log)
        for item in self.story:
            for key in item:
                if key == "background":
                    background = pygame.image.load(item[key]+".png")
                    constants.DISPLAYSURF.blit(background, (0,0), (0,0,1920, 1080))
                elif key == "Nothing":
                    self.writer.write_story_text(item[key])
                else:
                    #person = pygame.image.load(key+".png")
                    #constants.DISPLAYSURF.blit(person, (0, 200), (0, 0, 500, 1201))
                    self.writer.write_dialogue((key,item[key]))
            app.run(t,constants.DISPLAYSURF)



