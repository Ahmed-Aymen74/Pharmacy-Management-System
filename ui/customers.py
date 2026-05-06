import customtkinter as ctk
from services.customer_service import *

def open_customers():
    app = ctk.CTk()
    app.geometry("800x600")
    app.title("Customers")

    id_entry = ctk.CTkEntry(app, placeholder_text="ID (for update/delete)")
    id_entry.pack(pady=5)

    name = ctk.CTkEntry(app, placeholder_text="Name")
    name.pack(pady=5)

    phone = ctk.CTkEntry(app, placeholder_text="Phone")
    phone.pack(pady=5)

    def add():
        add_customer(name.get(), phone.get())
        load()

    def update():
        update_customer(id_entry.get(), name.get(), phone.get())
        load()

    def delete():
        delete_customer(id_entry.get())
        load()

    table = ctk.CTkTextbox(app, width=400, height=200)
    table.pack(pady=10)

    def load():
        table.delete("0.0", "end")
        try:
            rows = get_all_customers()
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