"""
Opening login screen
"""

from tkinter import Label, Entry, Frame, Button, StringVar, Tk
from boxesscreen import BoxesScreen
from baseframe import BaseFrame
from api import ApiCall

class LoginScreen(BaseFrame):
    def create_widgets(self):
        """ Login form """

        frame_top = Frame(self, pady=15, padx=15)
        frame_top.pack()

        self.email = StringVar()
        self.email_label = Label(frame_top, text="Email")
        self.email_entry = Entry(frame_top, textvariable=self.email)

        self.password = StringVar()
        self.password_label = Label(frame_top, text="Password")
        self.password_entry = Entry(frame_top,
                                    textvariable=self.password, show='*')

        frame_bottom = Frame(self, pady=15, padx=15)
        frame_bottom.pack()

        self.submit = Button(frame_bottom)
        self.submit["text"] = "Login"
        self.submit["command"] = self.sign_in

        #layout widgets in grid
        self.email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=1)
        self.password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1)
        self.submit.grid(row=2, column=0)

    def sign_in(self):
        """ Run this when login button is pressed """
        api = ApiCall()
        login = api.login(email=self.email_entry.get(), password=self.password_entry.get())

        if login:
            print("success!!")

        print("FUCK!")

    #    self.controller.show_frame(BoxesScreen)
