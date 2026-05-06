import customtkinter as ctk
from ui.customers import open_customers
from ui.employees import open_employees
from ui.drugs import open_drugs
from ui.sales import open_invoices

def open_dashboard():
    app = ctk.CTk()
    app.geometry("800x600")
    app.title("Dashboard")

    ctk.CTkLabel(app, text="DASHBOARD", font=("Arial", 22)).pack(pady=20)

    ctk.CTkButton(app, text="Customers", command=open_customers).pack(pady=5)
    ctk.CTkButton(app, text="Employees", command=open_employees).pack(pady=5)
    ctk.CTkButton(app, text="Drugs", command=open_drugs).pack(pady=5)
    ctk.CTkButton(app, text="Invoices", command=open_invoices).pack(pady=5)

    app.mainloop()