import customtkinter as ctk
from services.auth_service import login_user
from ui.dashboard import open_dashboard
import threading

def open_login():
    app = ctk.CTk()
    app.geometry("600x400")
    app.title("Login")

    ctk.CTkLabel(app, text="Pharmacy Management System\n\nLogin:", font=("Arial", 18)).pack(pady=10)

    ssn_entry = ctk.CTkEntry(app, placeholder_text="SSN")
    ssn_entry.pack(pady=10)

    name_entry = ctk.CTkEntry(app, placeholder_text="Name")
    name_entry.pack(pady=10)

    msg = ctk.CTkLabel(app, text="")
    msg.pack()

    def process_login():
        ssn = ssn_entry.get()
        name = name_entry.get()

        try:
            user = login_user(ssn, name)

            if user:
                app.after(0, lambda: handle_success(app))
            else:
                msg.configure(text="Invalid Login ❌")

        except Exception as e:
            print(e)
            msg.configure(text="DB Error ❌")

    def handle_success(app):
        app.destroy()
        open_dashboard()

    ctk.CTkButton(
        app,
        text="Login",
        command=lambda: threading.Thread(target=process_login, daemon=True).start()
    ).pack(pady=10)

    app.mainloop()