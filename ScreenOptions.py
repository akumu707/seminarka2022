class ScreenOptions:
    def __init__(self):
        self.resolution = (800,600) #standartni rozliseni
        self.fullscreen = False #jestli je na fullscreen
        self.active_screen = None #momentalne aktivni plocha

    def show(self, screen):
        if self.active_screen:
            self.active_screen.hide()
        self.active_screen = screen
        screen.show()
