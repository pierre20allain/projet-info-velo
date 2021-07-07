import sqlite3

connection = sqlite3.connect('entrainements.db')

with open('baseEntrainements.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO entrainements (label, seance, duree, repetitions, intensite) VALUES (?, ?, ?, ?, ?)",
            ('label', 'seance', 'duree', 'repetitions', 'intensite')
            )

"""
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )
"""

connection.commit()
connection.close()