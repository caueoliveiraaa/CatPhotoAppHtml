# Importações necessárias
import sqlite3
import pandas as pd
import os

# Instalar o pandas na nossa máquina local
# com o comando pip install pandas


# Usamos o def para criar uma função no Python (como o function do JavaScript)
def executar_comandos_sql(sql_string):
    """ Primeiro doctring: Função para executar SQL usando Pandas """

    # Criar conexão
    conn = sqlite3.connect('mydatabase.db')

    # A função do pandas read_sql_query executa comandos SQL
    # e espera como parâmetros uma string com o SQL a ser executado 
    # e a conexão com a base de dados
    retorno_sql = pd.read_sql_query(sql_string, conn)

    # Fechar conexão
    conn.close()

    return retorno_sql


def mostrar_opcoes(colunas_lista):
    """ Função para mostrar opções """

    # O enumerate permite que seja possível rodar o for com duas variáveis
    # uma sendo o indice (i) da linha, e a outra o valor (dado) que está naquele índice/posição
    print("Colunas disponíveis:")
    for indice, coluna_string in enumerate(colunas_lista):
        print(f"Coluna {indice}: {coluna_string}")

    print() # Printa uma linha vazia


def retornar_media_coluna(coluna_nome):
    """ Função para retornar média da coluna """

    # Comandos SQL
    sql_string = f"SELECT AVG({coluna_nome}) FROM usuarios"

    # Executando SQL
    resultado = executar_comandos_sql(sql_string)

    # O método iloc é fornecido pela biblioteca Pandas
    # e é usado para acessar dados em um DataFrame com
    # base em sua posição numérica. "iloc" significa "localização inteira".
    # Um DataFrame no Pandas, são os dados retornados de um excel ou banco de dados
    # que estão em formato de tabela, ou seja, matrix, com índices como [0][0], [0][1], [1][3], etc...
    # DataFrame é o nome dessa tabela/matrix quando estamos trabalhando com Pandas
    print(f"\nEXECUTANDO SQL: AVG {coluna_nome}: {resultado.iloc[0, 0]}")
    # OBS: Ao informar a posição para linha 0 e coluna 0, para buscar o item nessa posição que é
    # o resultado do AVG que trás a média de uma coluna
    print()


def contar_linhas_da_coluna(coluna_nome):
    """ Função para dar um COUNT na coluna informada por parâmetro """

    # Escrever comandos SQL
    sql_string = f"SELECT COUNT({coluna_nome}) FROM usuarios"

    # Executar SQL
    resultado = executar_comandos_sql(sql_string)

    # Mostrar o resultado final com o iloc (integer location) do Pandas
    print(f"\nEXECUTANDO SQL: COUNT {coluna_nome}: {resultado.iloc[0, 0]}\n")
    print()


def buscar_palavra_em_coluna(coluna_nome, tipo_busca, string_usuario):
    """ Função para buscar partes específicas das palavras usando LIKE """

    # Criar a string para a busca no padrão do SQL
    string_de_busca = ''
    if tipo_busca == 1:
        string_de_busca = f"'{string_usuario}%'"
    elif tipo_busca == 2:
        string_de_busca = f"'%{string_usuario}%'"
    elif tipo_busca == 3:
        string_de_busca = f"'%{string_usuario}'"
    else:
        print("Tipo de busca inválido!")
        # Com o return aqui a função não irá executar
        return

    # Escrever comandos SQL
    sql_string = f"SELECT * FROM usuarios WHERE {coluna_nome} LIKE {string_de_busca}"

    # Executar SQL
    resultado = executar_comandos_sql(sql_string)

    # Mostrar resultado final 
    print(f"EXECUTANDO SQL: LIKE {string_de_busca} {coluna_nome}:\n{resultado}")
    print()


def retornar_min_or_max(coluna_nome):
    """ Retornar o maior e o menor valor da coluna """

    # Escrever comandos SQL
    sql_string = f"SELECT MIN({coluna_nome}), MAX({coluna_nome}) FROM usuarios"

    # Execução SQL
    resultado = executar_comandos_sql(sql_string)
    
    # Printar os dois números que correspondem ao menor valor e o maior valor da coluna
    print(f"EXECUTANDO SQL: MIN {coluna_nome}: {resultado.iloc[0, 0]}")
    print(f"EXECUTANDO SQL: MAX {coluna_nome}: {resultado.iloc[0, 1]}")
    print()


### START ###
# Início do programa
os.system('cls')

# Usar PRAGMA table_info para retornar as colunas da tabela
sql_string_colunas = "PRAGMA table_info(usuarios)"
# Chamar função que executa strings com SQL para 
colunas_resultado = executar_comandos_sql(sql_string_colunas)
# print(colunas_resultado)

# Transformar todos os nomes em uma lista com a função built-in do Python .tolist()
colunas_lista = colunas_resultado['name'].tolist()
# OBS: O name representa as colunas nas informações retornadas sobre a tabela acima 

# Variável para calcular quantas operações foram feitas
contador = 0


rodar_programa = True
while rodar_programa is True:
    # Mostrar opções de colunas
    mostrar_opcoes(colunas_lista + '\n -> s para sair')

    # Ler indice da coluna para extrair o nome 
    indice_coluna = input("\nInforme a posição da coluna: ")

    # Verificar se o usuário quer para o programa
    if indice_coluna == 's' or indice_coluna == 'S':
        break

    # Se o usuário não informou s, converter para inteiro
    indice_coluna = int(indice_coluna)

    # Validar indice da coluna
    if indice_coluna >= 0 and indice_coluna <= len(colunas_lista):
        # Selecionar a coluna onde a operação será realizada
        coluna_nome = colunas_lista[indice_coluna]
        print(f'\nColuna "{coluna_nome}" selecionada!')
        # Incrementar o contador cada vez que o usuário informar um coluna válida
        contador += 1

        # String para input
        operacoes_menu =  "\n1 = retornar média usando AVG na coluna"
        operacoes_menu += "\n2 = retornar COUNT na coluna"
        operacoes_menu += "\n3 = retornar busca usando LIKE na coluna"
        operacoes_menu += "\n4 = retornar maior/menor valor da coluna com MIN e MAX"
        operacoes_menu += "\n5 = break no Python para parar o programa\n"
        operacoes_menu += "\nInforme a operação SQL: "

        # Ler a operação SQL que será exectada com o pandas
        operacao = input(operacoes_menu)
        # Usar o int para transformar a operacao em um número inteiro
        operacao = int(operacao) 

        # Chamar a função que corresponde a operação informada
        if operacao == 1:
            # Retornar a média da coluna informada
            retornar_media_coluna(coluna_nome)
        elif operacao == 2:
            # Retornar a quantidade de linhas da coluna
            contar_linhas_da_coluna(coluna_nome)
        elif operacao == 3:
            # Variável com menu para input quebrando linhas com \n
            menu_input =  "\n1 = Início da palavra"
            menu_input += "\n2 = Meio da palavra"
            menu_input += "\n3 = Fim da palavra"
            menu_input += "\nInforme a opção:"

            # Usar o int para transformar a busca em um número
            tipo_busca = int(input(menu_input))
            # Ler a string que será usada para busca no banco de dados
            string_usuario = input("\nInforme a string que irá para busca no banco: ")

            # Buscar palavra na conluna informada
            buscar_palavra_em_coluna(coluna_nome, tipo_busca, string_usuario)
        elif operacao == 4:
            # Retornar o menor e o maior valor da coluna
            retornar_min_or_max(coluna_nome)
        elif operacao == 5:
            # Parar o programa usando uma variável que está no while em vez de break
            rodar_programa = False
        else:
            print("\nOperação inválida!!")
    else:
        print("\nÍndice inválido!!")


### END ###
os.system('cls')
print(f'Operações realizadas: {contador}')
print('Programa finalizado.')
