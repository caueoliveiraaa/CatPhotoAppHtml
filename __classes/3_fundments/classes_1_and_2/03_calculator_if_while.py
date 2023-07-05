import os

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def rodar_calculadora():
    """ Realizar operações básicas de uma calculadora """

    try:
        os.system('cls')
        print("Calculadora:")

        while True:
            print("Selecione a operação: ")
            print("1. Adicionar")
            print("2. Subtrair")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Sair")

            choice = input("Informe a operação (1-5): ")

            if choice == '5':
                os.system('cls')
                print("Programa finalizou.")
                break

            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))

            if choice == '1':
                os.system('cls')
                print("Resultado: ", add(num1, num2), '\n')
            elif choice == '2':
                os.system('cls')
                print("Resultado: ", subtract(num1, num2), '\n')
            elif choice == '3':
                os.system('cls')
                print("Resultado: ", multiply(num1, num2), '\n')
            elif choice == '4':
                if num2 == 0:
                    os.system('cls')
                    print("Erro: Não é possível dividir números por zero!\n")
                else:
                    os.system('cls')
                    print("Resultado: ", divide(num1, num2), '\n')
            else:
                os.system('cls')
                print("Informe uma opção válida!\n")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    rodar_calculadora()