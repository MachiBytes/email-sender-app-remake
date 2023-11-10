import customtkinter as ctk
from src.logic import verification

class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent_window, username="", password="", stay_logged_in=False) -> None:
        super().__init__(parent_window, width=500, height=500)
        self.pack_propagate(False)

        # Widget variables
        self.username = ctk.StringVar(value=username)
        self.password = ctk.StringVar(value=password)
        self.stay_logged_in = ctk.BooleanVar(value=stay_logged_in)
        self.error_message = ctk.StringVar()
        self.parent_window = parent_window

        title = ctk.CTkLabel(master=self, text="LOGIN", font=ctk.CTkFont(size=40, weight="bold"))
        title.pack(padx=10, pady=(40, 20))

        username_label = ctk.CTkLabel(master=self, text="Username", font=ctk.CTkFont(size=20))
        username_label.pack(padx=10, pady=(20, 0))

        username_textbox = ctk.CTkEntry(master=self, textvariable=self.username)
        username_textbox.pack(pady=5)

        password_label = ctk.CTkLabel(master=self, text="Password", font=ctk.CTkFont(size=20))
        password_label.pack(padx=10, pady=(20, 0))

        password_textbox = ctk.CTkEntry(master=self, show="*", textvariable=self.password)
        password_textbox.pack(pady=5)

        keep_logged_in = ctk.CTkCheckBox(master=self, text="Keep me logged in", variable=self.stay_logged_in)
        keep_logged_in.pack(pady=10)

        login_button = ctk.CTkButton(master=self, text="Login", command=lambda: verification.verify_credentials(self))
        login_button.pack(pady=(10, 15))

        login_error = ctk.CTkLabel(master=self, font=ctk.CTkFont(size=15), text_color="red", textvariable=self.error_message)
        login_error.pack(padx=10, pady=(0, 0))