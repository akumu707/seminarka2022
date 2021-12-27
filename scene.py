class Scene:
    def __init__(self, writer):
        self.story = {}
        self.writer = writer

    def run(self):
        for item in self.story:
            for key in item:
                if not key == "text":
                    if key == "Nothing":
                        self.writer.write(item[key])
                    else:
                        self.writer.write(key+": "+item[key])