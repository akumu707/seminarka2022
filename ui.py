import sys

import pygame
import constants
from pgu import gui

class UI:
    def __init__(self, writer):
        self.writer = writer

    def _submit(value):
        return (value)

    def select_tree(self, tree_names):
        #tree_string = "Příběhy: "
        #for key in tree_names:
            #tree_string+=key+" "
        #self.writer.write(tree_string)
        #while True:
            #tree_name = input("Vyberte příběh: ")
            #for key in tree_names:
                #if key == tree_name:
                    #return key
        app=gui.Desktop()
        t = gui.Table()
        t.tr()
        t.td(gui.Label("Choose a story")) #haló, to nepodporuje češtinu q.q
        g = gui.Group()
        for name in tree_names:
            t.tr()
            t.td(gui.Tool(g, gui.Label(name), value=name))
        t.tr()
        submit = gui.Button("Submit")
        submit.connect(gui.CLICK, self._submit, g.value) #somehow nefunguje
        t.td(submit)
        t.tr()
        exit = gui.Button("Exit")
        exit.connect(gui.CLICK,app.quit, None) #pada kvuli pygame, vyresit
        t.td(exit)
        app.run(t, constants.DISPLAYSURF)



