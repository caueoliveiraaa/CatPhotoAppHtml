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