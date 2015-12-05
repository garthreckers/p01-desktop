"""
Menus are built here
"""
from tkinter import Menu

class MainMenu(Menu): # pylint: disable=too-many-ancestors
    """ set up main menu """
    def __init__(self, master=None):
        Menu.__init__(self)

        self = Menu(master)

        filemenu = Menu(self, tearoff=False)
        filemenu.add_command(label="Open")
        self.add_cascade(menu=filemenu, label="File")

        windowmenu = Menu(self, name="window", tearoff=False)
        self.add_cascade(menu=windowmenu, label="Window")

        helpmenu = Menu(self, name="help", tearoff=False)
        self.add_cascade(menu=helpmenu, label="Help")

        master['menu'] = self

