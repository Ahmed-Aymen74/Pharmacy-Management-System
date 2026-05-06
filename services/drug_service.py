from db import get_connection

def get_all_drugs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM DRUGS")
    rows = cur.fetchall()
    conn.close()
    return rows

def add_drug(code, name, price, expiry, category_id, stock):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO DRUGS VALUES (?, ?, ?, ?, ?, ?)",
        (code, name, price, expiry, category_id, stock)
    )
    conn.commit()
    conn.close()

def update_drug(code, name, price, expiry, category_id, stock):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """UPDATE DRUGS 
           SET name=?, price=?, expiry_date=?, category_id=?, stock=? 
           WHERE code=?""",
        (name, price, expiry, category_id, stock, code)
    )
    conn.commit()
    conn.close()

def delete_drug(code):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM DRUGS WHERE code=?", (code,))
    conn.commit()
    conn.close()