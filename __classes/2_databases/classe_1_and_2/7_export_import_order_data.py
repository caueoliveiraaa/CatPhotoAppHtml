import os
import sqlite3
import pandas as pd

# pip install xlwt  para poder salvar dados em excel
# pip install xlrd para poder ler dados do excel

# Conectar ao banco de dados SQLite usando uma variável global
conexao = sqlite3.connect('mydatabase.db')

def executar_sql(sql_string):
    """ Função para executar comandos SQL usando Pandas """

    data_frame = pd.read_sql_query(sql_string, conexao)
    return data_frame


def exportar_tabela_para_excel(nome_tabela):
    """ Buscar dados no banco via SELECT e salvar os dados em um excel """

    # Escrever sql com letras minúsculas
    query_string = f"select * from {nome_tabela}"
    data_frame = pd.read_sql_query(query_string, conexao)

    # Salvar DataFrame com dados do banco para um arquivo Excel com a função .to_excel do pandas
    # index=False para não incluir o índice do DataFrame no Excel quando criar o arquivo
    data_frame.to_excel(nome_tabela + '.xls', index=False)  
    os.system('cls')
    print(f"Dados exportados para {nome_tabela}.xls com sucesso.")


def importar_excel_para_banco(excel_file):
    """ Buscar dados no excel via pandas inserir os dados no banco de dados """

    # Ler dados do Excel em um DataFrame/Matriz/Tabela do pandas
    data_frame = pd.read_excel(excel_file)
    os.system('cls')

    # Demonstração split que é uma função built-in para transformar strings em listas
    print('\nsplit(.)  -->  Transformando o nome informado em um lista:')
    print(excel_file.split('.'))

    # Pegando o item na posição zero quando o split divide o nome do arquivo
    print('\nsplit(.)[0]  --> Selecionando o item 0:')
    print(excel_file.split('.')[0])

    # Extrair o nome do arquivo sem o xls para usar como nome da tabela
    nome_tabela = excel_file.split('.')[0]

    # Inserir os dados excel localizados no dataframe no banco de dados com a função do pandas .to_sql
    # if_exists='replace' sobrescreve a tabela caso ela já exista
    # Os outros parâmetros são padrão do .to_sql
    data_frame.to_sql(nome_tabela, conexao, index=False, if_exists='replace')

    # Close the database connection
    conexao.close()

    print(f"\nDados de {excel_file} importados a tabela {nome_tabela} com sucesso.")


def printar_opcoes(colunas_lista):
    """ Função para exibir as opções disponíveis para o usuário escolher """

    print("Colunas disponíveis:")
    for i, coluna in enumerate(colunas_lista):
        print(f"Coluna {i}: {coluna}")
    print()


def agrupar_por(coluna):
    """Função para agrupar por uma coluna """

    sql_string = f"select {coluna}, count(*) from usuarios group by {coluna}"
    resultado = executar_sql(sql_string)
    os.system('cls')
    print(resultado)
    print()


def ordenar_por(coluna):
    """Função para ordenar por uma coluna"""
    sql = f"select * from usuarios order by {coluna}"
    resultado = executar_sql(sql)
    os.system('cls')
    print(resultado)
    print()



contador = 0
os.system('cls')

while True:
    # Obter nome da tabela
    tabela_nome = input("\nInforme o nome da tabela: ")

    # Obter os nomes das colunas da tabela
    sql_colunas = f"PRAGMA table_info({tabela_nome})"
    colunas_data_frame = executar_sql(sql_colunas)
    colunas_list = colunas_data_frame['name'].tolist()

    # Exibir opções e obter entrada do usuário
    printar_opcoes(colunas_list)
    coluna_index = int(input("Informe a posição da coluna para agrupar/ordenar: "))

    # Executar a operação escolhida
    if coluna_index >= 0 and coluna_index <= len(colunas_list):
        menu_input =  "\na = agrupar coluna em tabela"
        menu_input += "\no = ordenar coluna em tabela"
        menu_input += "\ne = exportar dados para excel"
        menu_input += "\ni = importar dados para mydatabase"
        menu_input += "\ns = sair do programa\n"
        menu_input += "\nDigite a operação desejada:  "

        operacao = input(menu_input)
        contador += 1
        coluna_nome = colunas_list[coluna_index]

        if operacao == 'a':
            agrupar_por(coluna_nome)
        elif operacao == 'o':
            ordenar_por(coluna_nome)
        elif operacao == 'e':
            exportar_tabela_para_excel(tabela_nome)
        elif operacao == 'i':
            excel_nome = input('Informe o nome do excel: ')
            if '.xls' not in excel_nome:
                excel_nome += '.xls'
            importar_excel_para_banco(excel_nome)
        elif operacao == 's':
            break
        else:
            print("Operação inválida!")
    else:
        print("Opção inválida!")


# Fechar a conexão com o banco de dados
os.system('cls')
print(f'Programa parou, {contador} operações realizadas.')
conexao.close()
