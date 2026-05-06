import customtkinter as ctk
from services.invoice_service import *
from services.drug_service import get_all_drugs

def open_invoices():
    app = ctk.CTk()
    app.geometry("900x650")
    app.title("Invoice System")

    ctk.CTkLabel(app, text="Invoice System", font=("Arial", 22, "bold")).pack(pady=10)

    cust = ctk.CTkEntry(app, placeholder_text="Customer ID")
    cust.pack(pady=5)

    emp = ctk.CTkEntry(app, placeholder_text="Employee SSN")
    emp.pack(pady=5)

    msg = ctk.CTkLabel(app, text="", text_color="red")
    msg.pack(pady=5)

    drugs = get_all_drugs()
    drug_names = [f"{d[0]} - {d[1]} (Stock: {d[5]})" for d in drugs]

    selected_drug = ctk.StringVar(value="Select Drug")
    drug_menu = ctk.CTkOptionMenu(app, values=drug_names, variable=selected_drug)
    drug_menu.pack(pady=5)

    qty_entry = ctk.CTkEntry(app, placeholder_text="Quantity")
    qty_entry.pack(pady=5)

    table = ctk.CTkTextbox(app, width=700, height=250)
    table.pack(pady=10)

    current_items = []
    current_invoice_id = None


    def create_invoice_ui():
        nonlocal current_invoice_id, current_items

        try:
            if not cust.get() or not emp.get():
                msg.configure(text="Customer and Employee IDs required ❌")
                return

            current_invoice_id = create_invoice(cust.get(), emp.get())
            current_items = []

            table.insert("end", f"\nInvoice Created ✔ ID: {current_invoice_id}\n")
            msg.configure(text="Invoice Ready ✔")

        except Exception as e:
            msg.configure(text=str(e))

    def add_item():
        try:
            if not current_invoice_id:
                msg.configure(text="Create invoice first ❌")
                return

            drug_text = selected_drug.get()
            if " - " not in drug_text:
                msg.configure(text="Select valid drug ❌")
                return

            drug_code = int(drug_text.split(" - ")[0])
            qty_str = qty_entry.get()
            if not qty_str:
                msg.configure(text="Enter quantity ❌")
                return
            
            qty = int(qty_str)
            if qty <= 0:
                msg.configure(text="Quantity must be > 0 ❌")
                return

            add_invoice_item(
                current_invoice_id,
                len(current_items) + 1,
                drug_code,
                qty
            )

            current_items.append((drug_code, qty))

            table.insert("end", f"Added Drug {drug_code} x{qty}\n")
            msg.configure(text="Item Added ✔")

        except Exception as e:
            msg.configure(text=str(e))

    def load():
        table.insert("end", "\n--- All Invoices ---\n")
        rows = get_all_invoices()
        for r in rows:
            table.insert("end", f"{r}\n")

    def delete():
        nonlocal current_invoice_id, current_items
        try:
            dialog = ctk.CTkInputDialog(text="Enter Invoice ID to delete:", title="Delete Invoice")
            inv_id_str = dialog.get_input()
            
            if not inv_id_str:
                return
                
            inv_id = int(inv_id_str)
            
            delete_invoice(inv_id)
            table.insert("end", f"\nInvoice {inv_id} Deleted successfully\n")
            
            if inv_id == current_invoice_id:
                current_invoice_id = None
                current_items = []
                
            msg.configure(text=f"Invoice {inv_id} Deleted ✔")
        except ValueError:
            msg.configure(text="Invoice ID must be a number ❌")
        except Exception as e:
            msg.configure(text=str(e))

    btn_frame = ctk.CTkFrame(app)
    btn_frame.pack(pady=10)

    ctk.CTkButton(btn_frame, text="Create Invoice", command=create_invoice_ui).grid(row=0, column=0, padx=10)
    ctk.CTkButton(btn_frame, text="Add Item", command=add_item).grid(row=0, column=1, padx=10)
    ctk.CTkButton(btn_frame, text="Load Invoices", command=load).grid(row=0, column=2, padx=10)
    ctk.CTkButton(btn_frame, text="Delete Invoice", command=delete).grid(row=0, column=3, padx=10)

    app.mainloop()