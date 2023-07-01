import pyautogui as p
import os

# documentação:
# https://pyautogui.readthedocs.io/en/latest/screenshot.html


def ler_dados():
    """ Retornar dados do usuário """

    # Primeiro prompt 
    p.confirm(text='', title='', buttons=['RUN'])

    # Ler dados do usuário
    string_texto = p.prompt(
        text='Digite qualquer text que você desejar!',
        title='Input texto' ,
        default=''
    )

    # Retornar texto informado pelo usuário
    return string_texto


def main(input_texto):
    """
        Este bot abre o notepad
        e escreve manipulando
        o teclado com pyautogui

    """

    try:
        # Usando hotkey para precionar 
        # teclas em sequência
        p.hotkey('win', 'r')
        p.sleep(0.1)

        # Escrever notepad via teclado
        p.typewrite('notepad')
        p.sleep(0.1)

        # Precionar enter
        p.press('enter')
        p.sleep(0.1)

        # Maximizar
        p.hotkey('win', 'up')

        # Clicar no centro da tela
        p.click(800, 600)
        p.sleep(0.1)

        # Transformar o input nas teclas que o robô 
        # irá precionar através do laço for
        lista_texto = list(input_texto)

        # Digitar o texto
        for palavra in lista_texto:
            palavra = list(palavra)

            for letra in palavra: 
                p.press(letra)

        # Prompt final
        p.alert('Ao clicar em ok o programa notepad será finalizado!')

        # Usando comando taskkill (eliminar tarefa)
        # Para parar o programa notepad
        os.system('taskkill /f /im notepad.exe')
    except Exception as e:
        print(str(e))
        

if __name__ == '__main__':
    # NOTE: É necessário instalar o pyautogui
    # com o comando pip install pyautogui
    os.system('cls')
    
    try:
        # Rodar robô
        string_texto = ler_dados()
        main(input_texto=string_texto)
    except Exception as e:
        print(str(e))






