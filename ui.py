import sys

import pygame
import constants

class UI:
    def __init__(self, writer):
        self.writer = writer


    def select_tree(self, tree_names):
        tree_string = "Příběhy: "
        for key in tree_names:
            tree_string+=key+" "
        self.writer.write(tree_string)
        while True:
            tree_name = input("Vyberte příběh: ")
            for key in tree_names:
                if key == tree_name:
                    return key

