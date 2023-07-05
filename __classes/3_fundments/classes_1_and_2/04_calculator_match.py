import os


def calculadora_match(operador, numero_1, numero_2):
    """ Utilizar match case para realizar os cálculos básicos
    de uma calculadora """

    match operador:
        case '1':
            return numero_1 + numero_2
        case '2':
            return numero_1 - numero_2
        case '3':
            return numero_1 * numero_2
        case '4':
            return numero_1 / numero_2
        # Usamos _ como default
        case _:
            return "Operador inválido"


if __name__ == '__main__':
    os.system('cls')

    while True:
        try:
            print('Precione ctrl + c para parar o programa.')
            operador = input("Informe a operação (1 = +, 2 = -, 3 = *, 4 = /): ")
            numero_1 = float(input("Entre com o primeiro número: "))
            numero_2 = float(input("Entre com o segundo número: "))

            resultado = calculadora_match(operador, numero_1, numero_2)
            os.system('cls')
            print(f"Resultado: {resultado}\n")
        except KeyboardInterrupt:
            os.system('cls')
            print('Programa parou manualmente.')
            break
        except Exception as e:
            print(str(e))