# Importações necessárias para rodar arquivo (sempre no topo)
# A biblioteca os consegue executar
# comandos no CMD 
import os
import pandas as pd

# para instalar pandas: pip install pandas


def main():
    """ Descrição da função """

    try:
        os.system('cls')

        # Abrir Excel 
        excel_file = pd.ExcelFile('dados_excel.xlsx')
        print(excel_file)

        # Criar um sistema CRUD 

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()