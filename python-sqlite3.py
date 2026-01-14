import sqlite3

filename = "python-sqlite3.db"

con = sqlite3.connect(filename)
cur = con.cursor()

# create a table
cur.execute("CREATE TABLE movie(title, year, score)")

# select one line
res1 = cur.execute("SELECT * FROM movie").fetchone()
print(f'fetchone: {res1}')

# insert data
cur.execute("""
  INSERT INTO movie VALUES
    ('Monty Python and the Holy Grail', 1975, 8.2),
    ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

# select many lines
res2 = cur.execute("SELECT * FROM movie").fetchall()
print(f'fetchall: {res2}')
