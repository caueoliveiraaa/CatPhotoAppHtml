# Importações necessárias para rodar arquivo (sempre no topo)
# A biblioteca os consegue executar
# comandos no CMD 
import os


# Comandos para CMD:
# OBS: Troque os nomes arquivo_python.py e nome_do_arquivo
# pelos nomes dos arquivos a serem criados

# Usando o comando cd no terminal, navegue até o diretório
# onde o arquivo .py está e rode o comando abaixo:
# python nome_do_arquivo.py

# Para ver o conteúdo do arquivo no terminal:
# type nome_do_arquivo.py

# Para criar um arquivo .py do zero no terminal:
# echo print('Olá mundo') > arquivo_python.py

# Para mostrar apenas os arquivos Python no diretório/pasta atual
# dir *.py


# Função principal 
def main():
    """ Descrição da função """

    try:
        # Limpar o terminal executando
        # o comando cls no terminal
        os.system('cls')

        # Testar Python ao executar comando
        # python --version que mostra a versão
        # do Python atual que está instalada
        print('testando python')
        os.system('python --version')

        # Declarando variáveis vazias
        lista = []
        dicionario_py = {}
        tupla = ()
        numero_inteiro = 0
        numero_float = 0.0
        string = ''
        boolean_1 = True
        boolean_2 = False
        boolean_3 = None

        # Tipos de dados
        numero_inteiro = 1
        numero_float = 1.9
        string = 'texto alatório'
        boolean_1 = True
        boolean_2 = False
        boolean_3 = 10 > 5

        # Criando lista com variáveis
        lista = [
            numero_inteiro,
            numero_float,
            string,
            boolean_1,
            boolean_2,
            boolean_3,
        ]

        # Printando lista usando posição
        # e a função type() para mostrar
        # o tipo de dado na posição indicada
        print(lista)    
        print('Valor ', lista[0], ' é do tipo ', type(lista[0]))
        print('Valor ', lista[1], ' é do tipo ', type(lista[1]))
        print('Valor ', lista[2], ' é do tipo ', type(lista[2]))
        print('Valor ', lista[3], ' é do tipo ', type(lista[3]))
        print('Valor ', lista[4], ' é do tipo ', type(lista[4]))
        print('Valor ', lista[5], ' é do tipo ', type(lista[5]))
        print('Tipo da variável lista: ', type(lista)  )

        # Tuplas não podem ser alteradas
        tupla = (1, 'texto', (7 > 5), 55.4) 
        print(tupla)    
        print('Tipo da variável tupla: ', type(tupla)  )

        # Dicionário
        dicionario_py = {
            'name': 'python',
            'version': 3.11,
            'os': 'windows',
        }

        print(dicionario_py['name'])
        print(dicionario_py['version'])
        print(dicionario_py['os'])
    except Exception as e:
        # Mostrar o erro caso
        # o mesmo ocorra
        print(e)


# If para rodar o código que será executado
# quando este arquivo for executado de forma
# infividual, mas as funções aqui contidas 
# podem ser importadas e chamadas em outros arquivos .py
if __name__ == '__main__':
    main()