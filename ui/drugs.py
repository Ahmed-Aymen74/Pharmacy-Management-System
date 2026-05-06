import customtkinter as ctk
from services.drug_service import *

def open_drugs():
    app = ctk.CTk()
    app.geometry("800x600")
    app.title("Drugs")

    code = ctk.CTkEntry(app, placeholder_text="Code")
    code.pack(pady=5)

    name = ctk.CTkEntry(app, placeholder_text="Name")
    name.pack(pady=5)

    price = ctk.CTkEntry(app, placeholder_text="Price")
    price.pack(pady=5)

    expiry = ctk.CTkEntry(app, placeholder_text="Expiry (YYYY-MM-DD)")
    expiry.pack(pady=5)
    expiry.insert(0, "2026-01-01")

    category_id = ctk.CTkEntry(app, placeholder_text="Category ID")
    category_id.pack(pady=5)
    category_id.insert(0, "1")

    stock = ctk.CTkEntry(app, placeholder_text="Stock")
    stock.pack(pady=5)

    def add():
        add_drug(code.get(), name.get(), price.get(), expiry.get(), category_id.get(), stock.get())
        load()

    def update():
        update_drug(code.get(), name.get(), price.get(), expiry.get(), category_id.get(), stock.get())
        load()

    def delete():
        delete_drug(code.get())
        load()

    table = ctk.CTkTextbox(app, width=500, height=150)
    table.pack(pady=10)

    def load():
        table.delete("0.0", "end")
        try:
            rows = get_all_drugs()
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