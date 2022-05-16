import json

class GameSettings:
    def __init__(self):
        with open("scenes.json", "r", encoding="utf-8") as file:
            self.file = json.load(file)
        self.this_tree = {}
        self.chosen_story = None
        self.player_name = "Diana"
        self.player_surname = "Falmenová"

    def find_this_tree(self, tree_name):
        self.this_tree = self.file[tree_name]

    def load_existing_game(self, file_name):
        with open(r"Saved/"+file_name, "r", encoding="utf-8") as file:
            self.file = json.load(file)

    def save_game(self, file_name):
        with open(r"Saved/"+file_name, "w", encoding="utf-8") as file:
            json.dump(self.file, file, ensure_ascii=False, indent=4)