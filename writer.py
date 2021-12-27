import pygame
import constants

class Writer:
    def __init__(self):
        self.story_font = pygame.font.SysFont('arial', 50)
        self.name_font = pygame.font.SysFont('arial', 50)

    def write_story_text(self, text):
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.NAME_RECT)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.STORY_TEXT_RECT)
        story_text = self.story_font.render(text,True, constants.WHITE)
        constants.DISPLAYSURF.blit(story_text, constants.STORY_TEXT_POINT)
        pygame.display.flip()

    def write_dialogue(self, dialogue):
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.NAME_RECT)
        pygame.draw.rect(constants.DISPLAYSURF, constants.BLACK, constants.STORY_TEXT_RECT)
        name_text = self.name_font.render(dialogue[0], True, constants.WHITE)
        constants.DISPLAYSURF.blit(name_text, constants.NAME_TEXT_POINT)
        story_text = self.story_font.render(dialogue[1], True, constants.WHITE)
        constants.DISPLAYSURF.blit(story_text, constants.STORY_TEXT_POINT)
        pygame.display.flip()