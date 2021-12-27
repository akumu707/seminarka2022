import json

class Tree:
    def __init__(self):
        with open("scenes.json", "r", encoding="utf-8") as file:
            self.file = json.load(file)
        self.this_tree = {}

    def find_this_tree(self, tree_name):
        self.this_tree = self.file[tree_name]