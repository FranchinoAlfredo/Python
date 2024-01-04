import sqlite3

# Connessione al database (o creazione se non esiste)
conn = sqlite3.connect('esempio_database.db')

# Creazione di un cursore per eseguire query SQL
cursor = conn.cursor()

# Creazione di una tabella di esempio
cursor.execute('''
    CREATE TABLE IF NOT EXISTS persone (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        eta INTEGER
    )
''')

# Inserimento di dati nella tabella
cursor.execute("INSERT INTO persone (nome, eta) VALUES (?, ?)", ('Mario Rossi', 30))
cursor.execute("INSERT INTO persone (nome, eta) VALUES (?, ?)", ('Luca Bianchi', 25))

# Commit delle modifiche
conn.commit()

# Esempio di esecuzione di una query SQL
cursor.execute("SELECT * FROM persone")
persone = cursor.fetchall()

# Stampa dei risultati
print("Elenco delle persone nel database:")
for persona in persone:
    print(f"ID: {persona[0]}, Nome: {persona[1]}, Età: {persona[2]}")

# Chiusura della connessione
conn.close()
