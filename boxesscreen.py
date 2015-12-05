"""
This screen will display all of the logged in 
users boxes they have associated with their account
"""

from tkinter import Frame, Label, Button
from baseframe import BaseFrame
#from api import APICall

class BoxesScreen(BaseFrame):
    def create_widgets(self):
        """ Display all the boxes """

        f_main = Frame(self, padx=15, pady=15)
        f_main.pack()

        self.success = Label(f_main, text="Success")
        self.success.grid(row=0, column=0)
        
    def test(self):
        print("FUCK YA")
        