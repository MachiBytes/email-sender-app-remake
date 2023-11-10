from src import settings
import customtkinter as ctk
from src.widgets import login_screen, email_sender


class App(ctk.CTk):
    def __init__(self, username="", password="", stay_logged_in=False):
        super().__init__()

        ctk.set_appearance_mode(settings.APPEARANCE_MODE)
        self.geometry(settings.APP_GEOMETRY)
        self.title(settings.APP_TITLE)
        self.resizable(False, False)

        # Frames
        self.login_screen = login_screen.LoginScreen(parent_window=self, username=username, password=password, stay_logged_in=stay_logged_in)
        self.email_sender = email_sender.EmailSender(parent_window=self, parent=self)

        self.login_screen.pack()