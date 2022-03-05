from pgu import gui

class Select_button(gui.Button):
    def __init__(self, value):
        self.value = value

class LogDialog(gui.Dialog):
    def __init__(self, paragraphs):
        title = gui.Label("Log")

        width = 400
        height = 200
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")
        for i in paragraphs:
            doc.block(align=-1)
            for word in str(i):
                doc.add(gui.Label(word))
                doc.space(space)
            doc.br(space[1])
        gui.Dialog.__init__(self,title,gui.ScrollArea(doc,width,height))

