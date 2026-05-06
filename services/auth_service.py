from db import get_connection

def login_user(ssn, name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM EMPLOYEES
        WHERE ssn=? AND name=?
    """, (ssn, name))

    user = cur.fetchone()
    conn.close()

    return user