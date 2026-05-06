from db import get_connection

def get_all_employees():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM EMPLOYEES")
    rows = cur.fetchall()
    conn.close()
    return rows

def add_employee(ssn, name, salary):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO EMPLOYEES VALUES (?, ?, ?)",
        (ssn, name, salary)
    )
    conn.commit()
    conn.close()

def update_employee(ssn, name, salary):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE EMPLOYEES SET name=?, salary=? WHERE ssn=?",
        (name, salary, ssn)
    )
    conn.commit()
    conn.close()

def delete_employee(ssn):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM EMPLOYEES WHERE ssn=?", (ssn,))
    conn.commit()
    conn.close()