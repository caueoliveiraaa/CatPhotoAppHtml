import pyautogui as p
import os


def main(input_texto):
    """
        Este bot abre o notepad
        e escreve manipulando
        o teclado com pyautogui

    """

    try:
        # Usando hotkey para precinar 
        # teclas em sequência
        p.hotkey('win', 'r')
        p.sleep(0.2)

        # Escrever notepad via teclado
        p.typewrite('notepad')
        p.sleep(0.2)

        # Precionar enter
        p.press('enter')
        p.sleep(0.2)

        # Maximizar
        p.hotkey('win', 'up')

        # Clicar no centro da tela
        p.click(800, 600)
        p.sleep(0.2)

        # Transformar o input nas teclas que o robô 
        # irá precionar através do laço for
        lista_texto = list(input_texto)

        for letra in lista_texto:
            p.sleep(0.1)   
            p.press(letra) 

        # Mostrando mensagem de finalização do programa
        p.sleep(2)
        p.alert('Programa finalizado.')

        # Usando comando taskkill (eliminar tarefa)
        # Para parar o programa notepad
        os.system('taskkill /f /im notepad.exe')
    except Exception as e:
        print(str(e))
        

if __name__ == '__main__':
    try:
        os.system('cls')
        # Ler dados do usuário
        string_texto = p.prompt(
            text='Digite o texto',
            title='Input texto' ,
            default=''
        )

        # Chamar a função que roda o robô        
        main(input_texto=string_texto)
    except Exception as e:
        print(str(e))






