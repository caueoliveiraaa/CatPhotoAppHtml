import pandas as pd
import sqlite3

# Criando conexão
conn = sqlite3.connect('mydatabase.db')


# Função do Python (with) que server para abrir arquivos
with open('your_sql_file.sql', 'r') as file:
    sql_query = file.read()

# Executar sql com pandas
result = pd.read_sql_query(sql_query, conn)

# Mostrando resultado
print(result)

# Fechando conexão
conn.close()