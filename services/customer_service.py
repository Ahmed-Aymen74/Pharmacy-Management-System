from db import get_connection

def get_all_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM CUSTOMERS")
    rows = cur.fetchall()
    conn.close()
    return rows

def add_customer(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO CUSTOMERS (name, phone) VALUES (?, ?)",
        (name, phone)
    )
    conn.commit()
    conn.close()

def update_customer(id, name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE CUSTOMERS SET name=?, phone=? WHERE id=?",
        (name, phone, id)
    )
    conn.commit()
    conn.close()

def delete_customer(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM CUSTOMERS WHERE id=?", (id,))
    conn.commit()
    conn.close()