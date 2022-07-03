import json
import os

class GameSettings:
    def __init__(self):
        with open("resources/data/scenes.json", "r", encoding="utf-8") as file:
            self.file = json.load(file)
        with open("resources/data/game_settings.json", "r", encoding="utf-8") as file:
            self.settings = json.load(file)
        self.this_tree = {}
        self.chosen_story = None

    def find_this_tree(self, tree_name):
        self.this_tree = self.file[tree_name]

    def load_existing_game(self, name):
        with open(r"Saved/"+name+"/"+name+"_story.json", "r", encoding="utf-8") as file:
            self.file = json.load(file)
        with open(r"Saved/"+name+"/"+name+"_settings.json", "r", encoding="utf-8") as file:
            self.settings = json.load(file)

    def save_game(self, name):
        os.makedirs(r"Saved/"+name, exist_ok=True)
        with open(r"Saved/"+name+"/"+name+"_story.json", "w", encoding="utf-8") as file:
            json.dump(self.file, file, ensure_ascii=False, indent=4)
        with open(r"Saved/"+name+"/"+name+"_settings.json", "w", encoding="utf-8") as file:
            json.dump(self.settings, file, ensure_ascii=False, indent=4)