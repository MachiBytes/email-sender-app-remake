import tkinter as tk
import customtkinter as ctk
from src.logic import email_processing


class EmailSender(ctk.CTkFrame):
    def __init__(self, parent_window, parent):
        super().__init__(parent_window, width=500, height=500)
        self.pack_propagate(False)

        # Widget Variables
        self.subject = ctk.StringVar()
        self.template = ctk.StringVar()
        self.data = ctk.StringVar()
        self.message = ctk.StringVar()

        title = ctk.CTkLabel(master=self, text="Email Sender", font=ctk.CTkFont(size=30, weight="bold"))
        title.pack(padx=10, pady=20)

        subject_label = ctk.CTkLabel(master=self, text="Subject", font=ctk.CTkFont(size=15))
        subject_label.pack(pady=(10, 0))

        subject = ctk.CTkEntry(master=self, height=20, width=350, textvariable=self.subject)
        subject.pack(pady=(0, 5))

        template_label = ctk.CTkLabel(master=self, text="Template", font=ctk.CTkFont(size=15))
        template_label.pack(pady=(10, 0))

        template_path = ctk.CTkEntry(master=self, height=20, width=400, state="disabled", textvariable=self.template)
        template_path.pack(pady=(0, 5))

        template_button = ctk.CTkButton(master=self, height=30, width=60, text="Open", command=lambda: self.open_file(self.template))
        template_button.pack(pady=(0, 20))

        data_label = ctk.CTkLabel(master=self, text="Data", font=ctk.CTkFont(size=15))
        data_label.pack(pady=(10, 0))

        data_path = ctk.CTkEntry(master=self, height=20, width=400, state="disabled", textvariable=self.data)
        data_path.pack(pady=(0, 5))

        data_button = ctk.CTkButton(master=self, height=30, width=60, text="Open", command=lambda: self.open_file(self.data))
        data_button.pack(pady=(0, 10))

        ctk.CTkButton(master=self, height=30, width=100, text="Submit", command=lambda: email_processing.submit(self)).pack(
            pady=(30, 0)
        )

        ctk.CTkLabel(master=self, text="Data", font=ctk.CTkFont(size=10), textvariable=self.message).pack(pady=(5, 0))
    
    def open_file(self, string_var):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            string_var.set(file_path)