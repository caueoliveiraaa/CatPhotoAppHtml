# No começo do arquivo realizamos os imports
import sqlite3


""" Criar conexão com banco de dados e criar uma tabela com dois valores """

# O try tenta executar o códgio que está dentro de seu bloco
# Conectar com o arquivo mydatabase.db
conn = sqlite3.connect('mydatabase.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela 
cursor.execute('''

    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )

''')

# Inserir dados na tabela criada
# Insert data into the table
cursor.execute('''

    INSERT INTO alunos (nome, idade) VALUES ('Mr. Robot', 25)

''')

# Comitar mudanças para o banco de dados
conn.commit()

# Importante: Fechar a conexão com o banco de dados 
conn.close()
