#!/usr/bin/python3
"""
Desktop interface for Project01
"""

from tkinter import Frame

from loginscreen import LoginScreen
from boxesscreen import BoxesScreen
from mainmenu import MainMenu

class Application(Frame): # pylint: disable=too-many-ancestors
    """ Main App class """
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Add main menu
        MainMenu(self.master)

        self.master.title("Project01")

        self.frames = {}
        for frm in (LoginScreen, BoxesScreen):
            frame = frm(self.master, self)
            frame.grid(row=0, column=0)
            self.frames[frm] = frame

        self.show_frame(LoginScreen)

    def show_frame(self, cls):
        """ Use this function from one of the screens to change the current screens """

        self.frames[cls].tkraise()


APP = Application()
APP.mainloop()
