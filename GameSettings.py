import json
import os

class GameSettings:
    def __init__(self):
        with open(os.path.join("resources","data","scenes.json"), "r", encoding="utf-8") as file:
            self.file = json.load(file)
        with open(os.path.join("resources","data","game_settings.json"), "r", encoding="utf-8") as file:
            self.settings = json.load(file)
        self.this_tree = {}
        self.chosen_story = None

    def find_this_tree(self, tree_name):
        self.this_tree = self.file[tree_name]

    def load_existing_game(self, name):
        with open(os.path.join("Saved", name, "story.json"), "r", encoding="utf-8") as file:
            self.file = json.load(file)
        with open(os.path.join("Saved", name, "settings.json"), "r", encoding="utf-8") as file:
            self.settings = json.load(file)

    def save_game(self, name):
        os.makedirs(os.path.join("Saved",name), exist_ok=True)
        with open(os.path.join("Saved",name, "story.json"), "w", encoding="utf-8") as file:
            json.dump(self.file, file, ensure_ascii=False, indent=4)
        with open(os.path.join("Saved", name,"settings.json"), "w", encoding="utf-8") as file:
            json.dump(self.settings, file, ensure_ascii=False, indent=4)