import pygame
import constants

class Writer:
    def __init__(self):
        self.story_font = pygame.font.SysFont('arial', 15)
        self.name_font = pygame.font.SysFont('Helvetica', 20)

    def write_story_text(self, text):
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.NAME_RECT)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.STORY_TEXT_RECT)
        story_text = self.story_font.render(text,True, constants.WHITE)
        constants.DISPLAYSURF.blit(story_text, constants.STORY_TEXT_POINT)
        pygame.display.flip()