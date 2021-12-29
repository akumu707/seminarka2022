import pygame
import constants

class Scene:
    def __init__(self, writer):
        self.story = {}
        self.writer = writer

    def run(self):
        for item in self.story:
            for key in item:
                if key == "background":
                    background = pygame.image.load(item[key]+".png")
                    constants.DISPLAYSURF.blit(background, (0,0), (0,0,1920, 1080))
                elif key == "Nothing":
                    self.writer.write_story_text(item[key])
                    pygame.time.wait(2000)
                else:
                    person = pygame.image.load(key+".png")
                    constants.DISPLAYSURF.blit(person, (0, 200), (0, 0, 500, 1201))
                    self.writer.write_dialogue((key,item[key]))
                    pygame.time.wait(2000)