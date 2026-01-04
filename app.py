# app.py

import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability (intentional)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    return cursor.fetchall()

def login():
    # Hardcoded credentials (security issue)
    username = "admin"
    password = "admin123"

    if username == "admin" and password == "admin123":
        print("Login successful")

if __name__ == "__main__":
    login()
    print(get_user(1))
