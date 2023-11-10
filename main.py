from src.logic import app_processes
from src.widgets import app

if __name__ == "__main__":
    data, boolean = app_processes.app_initialized()
    username = ""
    password = ""
    if boolean:
        username = data["username"]
        password = data["password"]

    app = app.App(username, password, boolean)
    app.mainloop()
    app_processes.remove_token()
    print("App closed.")
