from db import get_connection

def create_invoice(customer_id, employee_ssn):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO INVOICE (customer_id, employee_ssn, total_amount) OUTPUT INSERTED.inv_id VALUES (?, ?, 0)",
        (customer_id, employee_ssn)
    )
    inv_id = cur.fetchone()[0]

    conn.commit()
    conn.close()
    return inv_id

def add_invoice_item(inv_id, item_no, drug_code, qty):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT price, stock FROM DRUGS WHERE code=?", (drug_code,))
        result = cur.fetchone()

        if not result:
            raise Exception("Drug not found ❌")

        price, stock = result

        if stock < int(qty):
            raise Exception("Not enough stock ❌")

        cur.execute(
            "INSERT INTO INVOICE_ITEM VALUES (?, ?, ?, ?)",
            (inv_id, item_no, drug_code, qty)
        )

        cur.execute(
            "UPDATE DRUGS SET stock = stock - ? WHERE code=?",
            (qty, drug_code)
        )

        subtotal = float(price) * int(qty)
        cur.execute(
            "UPDATE INVOICE SET total_amount = total_amount + ? WHERE inv_id=?",
            (subtotal, inv_id)
        )

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


def get_all_invoices():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM INVOICE")
    rows = cur.fetchall()

    conn.close()
    return rows


def delete_invoice(inv_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM INVOICE_ITEM WHERE inv_id=?", (inv_id,))
        items = cur.fetchall()

        for item in items:
            drug_code = item[2]
            qty = item[3]
            cur.execute("UPDATE DRUGS SET stock = stock + ? WHERE code=?", (qty, drug_code))

        cur.execute("DELETE FROM INVOICE_ITEM WHERE inv_id=?", (inv_id,))
        cur.execute("DELETE FROM INVOICE WHERE inv_id=?", (inv_id,))

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()