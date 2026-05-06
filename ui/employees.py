import customtkinter as ctk
from services.employee_service import *

def open_employees():
    app = ctk.CTk()
    app.geometry("800x600")
    app.title("Employees")

    ssn = ctk.CTkEntry(app, placeholder_text="SSN")
    ssn.pack(pady=5)

    name = ctk.CTkEntry(app, placeholder_text="Name")
    name.pack(pady=5)

    salary = ctk.CTkEntry(app, placeholder_text="Salary")
    salary.pack(pady=5)

    def add():
        add_employee(ssn.get(), name.get(), salary.get())
        load()

    def update():
        update_employee(ssn.get(), name.get(), salary.get())
        load()

    def delete():
        delete_employee(ssn.get())
        load()

    table = ctk.CTkTextbox(app, width=400, height=200)
    table.pack(pady=10)

    def load():
        table.delete("0.0", "end")
        try:
            rows = get_all_employees()
            for r in rows:
                table.insert("end", f"{r}\n")
        except Exception as e:
            table.insert("end", f"Error loading data: {e}\n")

    btn_frame = ctk.CTkFrame(app)
    btn_frame.pack(pady=10)

    ctk.CTkButton(btn_frame, text="Add", command=add).grid(row=0, column=0, padx=5)
    ctk.CTkButton(btn_frame, text="Update", command=update).grid(row=0, column=1, padx=5)
    ctk.CTkButton(btn_frame, text="Delete", command=delete).grid(row=0, column=2, padx=5)
    ctk.CTkButton(btn_frame, text="Load", command=load).grid(row=0, column=3, padx=5)

    load()
    app.mainloop()