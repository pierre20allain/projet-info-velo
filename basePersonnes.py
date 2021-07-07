import sqlite3

connection = sqlite3.connect('personnes.db')

with open('basePersonnes.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# il faut ajouter une case username et une case mdp

cur.execute("INSERT INTO personnes (nom, prenom, age, pma, lthr, ftp, duree, username, mdp, jour) VALUES (?, ?, ?, ?, ?, ?, ?,?,?,?)",
            ('nom', 'prenom', 'age', 'pma', 'ftp', 'lthr', 'duree','username', 'mdp', 'jour')
            )



connection.commit()
connection.close()