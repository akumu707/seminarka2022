import sys

import pygame
import constants
from pgu import gui

class UI:
    def __init__(self, writer):
        self.writer = writer

    def _submit(value):
        return (value)

    def select(self, names):
        app=gui.Desktop()
        t = gui.Table()
        t.tr()
        t.td(gui.Label("Choose a story")) #haló, to nepodporuje češtinu q.q
        g = gui.Group()
        t.tr()
        t.td(gui.Tool(g, gui.Label("None"), value=None))
        for name in names:
            t.tr()
            t.td(gui.Tool(g, gui.Label(name), value=name))
        t.tr()
        submit = gui.Button("Submit")
        submit.connect(gui.CLICK,app.quit)
        t.td(submit)
        t.tr()
        app.run(t, constants.DISPLAYSURF)
        return g.value



