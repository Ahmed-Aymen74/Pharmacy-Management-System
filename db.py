import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=Ammar;"
            "Database=pharmacy_db;"
            "Trusted_Connection=yes;"
        )
        print("DB Connected successfully")
        return conn

    except Exception as e:
        print("DB Connection Error:", e)
        return None