import cgi

import mysql.connector
import keyring

if __name__ == '__main__':
    # Open the database new-starter-site.
    # (1) Get MySQL password stored in keyring.
    # (2) Connect to MySQL
    # (3) Create a cursor to execute SQL statements
    pw = keyring.get_password("MySQL", "root")
    db = mysql.connector.connect(
        host="localhost", user="root", password=pw, database="new-starter-site")
    cursor = db.cursor()

    # Connect this program to the HTML form
    form = cgi.FieldStorage()
    fname = form.getvalue('fname')
    lname = form.getvalue('lname')
    msg = form.getvalue('message')
    found_through = form.getvalue('found_through')

    cursor.execute(f"INSERT INTO ForSubmissions VALUES {fname} {lname} {msg} {found_through}")

    db.commit()
    db.close()