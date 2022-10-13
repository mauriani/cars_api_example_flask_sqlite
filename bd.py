import sqlite3

conn = sqlite3.connect('cars.sqlite')

cursor = conn.cursor()

# criando a tabela (schema)

sql_query = """CREATE TABLE cars (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER
)"""

cursor.execute(sql_query)

print('Tabela criada com sucesso.')
