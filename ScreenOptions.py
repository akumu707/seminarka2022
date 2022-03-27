import pygame

class ScreenOptions:
    def __init__(self):
        self.monitor_screen = [pygame.display.Info().current_w,pygame.display.Info().current_h] #during init display isn`t set up so it takes info of the active monitor
        self.resolution = (800,600) #standartni rozliseni
        self.resizable = True
        self.fullscreen = False #jestli je na fullscreen
        self.active_screen = None #momentalne aktivni plocha

    def show(self, screen):
        if self.active_screen:
            self.active_screen.hide()
        self.active_screen = screen
        screen.show()
