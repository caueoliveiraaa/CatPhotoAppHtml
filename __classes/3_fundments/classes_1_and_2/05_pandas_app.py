# Importações necessárias para rodar arquivo (sempre no topo)
# A biblioteca os consegue executar
# comandos no CMD 
import os
import pandas as pd
import pyautogui as p

# para instalar pandas: pip install pandas

def main():
    """ Descrição da função """

    try:
        os.system('cls')
        quantidade = input('Informe a quantidade de linhas: ')

        # Abrir Excel 
        excel_file = pd.ExcelFile('dados_excel.xlsx')
        print(excel_file)

        msg_1 = 'Informe uma string para o excel: '
        msg_2 = 'Informe um número para o excel: '
        msg_3 = 'Informe um para o excel: '
        msg_4 = 'Informe um nome para o excel: '

        contador = 0
        while contador < quantidade:
            prompt_1 = p.prompt(text=msg_1, title='Pandas - Excel')
            prompt_2 = p.prompt(text=msg_2, title='Pandas - Excel')
            prompt_3 = p.prompt(text=msg_3, title='Pandas - Excel')
            prompt_4 = p.prompt(text=msg_4, title='Pandas - Excel')

            # salvar no excel com pandas


        # Criar um sistema CRUD 

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()