import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    return result

def menu_operacoes() -> str:
    print('Escolha a operação:')
    print('1 - Soma (+)')
    print('2 - Subtração (-)')
    print('3 - Multiplicação (*)')
    print('4 - Divisão (/)')
    opcao = input('Digite o número da operação desejada: ')
    if opcao == '1':
        return '+'
    elif opcao == '2':
        return '-'
    elif opcao == '3':
        return '*'
    elif opcao == '4':
        return '/'
    else:
        return None

if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            operador = menu_operacoes()
            if operador is None:
                print('Opção inválida!')
                time.sleep(2)
                continue
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = calculadora(num1, num2, operador)
            print(f'Resultado: {resultado}')
            input('\nPressione Enter para continuar...')

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
