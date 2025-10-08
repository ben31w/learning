# https://docs.python.org/3/library/sqlite3.html

import sqlite3

con = sqlite3.connect("basic_demo.db")
cur = con.cursor()

# DROP/CREATE TABLE
cur.execute("DROP TABLE IF EXISTS movie;")
cur.execute("CREATE TABLE IF NOT EXISTS movie(id INTEGER PRIMARY KEY, title, year, score);")

# sqlite_master is the built-in SQLite Schema table
res = cur.execute("SELECT name FROM sqlite_master;")
print(res.fetchone())

# INSERT example 1
cur.execute("""
    INSERT INTO movie(title, year, score) VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

# INSERT example 2
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie(title, year, score) VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

# con.close()
