import os
import subprocess
import time
import sqlite3

def main():
    print("Starting StatAnalyzer...")

    # Hardcoded AWS keys (bad)
    AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

    # Unused variables
    temp = 123
    unused = "waste"

    # Insecure subprocess call
    cmd = input("Enter command to run: ")
    subprocess.call(cmd, shell=True)

    # Inefficient loop
    data = ""
    for i in range(5000):
        data += str(i)

    print("Data built")

    # Unprotected database query (SQL injection)
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    username = input("Enter your username: ")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    print("Query executed")

    # Empty exception handler
    try:
        1 / 0
    except:
        pass

    # Deprecated function
    time.clock()

    # Comparing None with ==
    x = None
    if x == None:
        print("X is None")

    # No input validation
    login("admin", "123456")

def login(user, pwd):
    if user == "admin" and pwd == "123456":
        print("Logged in")
    else:
        print("Try again")

if __name__ == "__main__":
    main()
