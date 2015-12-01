#!/usr/bin/python3
"""
Desktop interface for Project01
"""

from tkinter import Frame, Tk

from loginscreen import LoginScreen
from boxesscreen import BoxesScreen
from mainmenu import MainMenu
from api import APICall

class Application(Frame): # pylint: disable=too-many-ancestors
    """ Main App class """
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Add main menu
        MainMenu(self.master)

        self.master.title("Project01")

        self.frames = {}
        for F in (LoginScreen, BoxesScreen):
            frame = F(self.master, self)
            frame.grid(row=0, column=0)
            self.frames[F] = frame

        self.show_frame(LoginScreen)

        print(self.frames)

    def show_frame(self, cls):
        self.frames[cls].tkraise()
        self.frames[cls].test()


APP = Application()
APP.mainloop()
