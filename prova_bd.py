import sqlite3 as sql

con = sql.connect('Escola.db')

cursor = con.cursor()

#Criando a tabela!!! receba ============================


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     email TEXT NOT NULL
# )
# """)


#Inserindo valores =======================


# cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Gondin", 49, "Gondin@gmail.com"))
# cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Bruncai", 37, "amebamaior@gmail.com"))
# cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Scomparin", 80, "Scomparin@gmail.com"))

# Listando Registros ====================

# cursor.execute("SELECT * FROM alunos")
# print(cursor.fetchall())

# Listando ID =======================

# cursor.execute("SELECT * FROM alunos WHERE id = '1'")
# print(cursor.fetchall())

# ATUALIZANDO REGISTROS

# cursor.execute("UPDATE alunos SET idade = '76' WHERE nome = 'Bruncai'")

# DELETANDO REGISTROS

# cursor.execute("DELETE FROM alunos WHERE id = '2'")
# cursor.execute("SELECT * FROM alunos")
# print(cursor.fetchall())



con.commit()
con.close()
