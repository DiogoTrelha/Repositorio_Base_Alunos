# crie  uma funçao chamada calculadora que receba tres parametros
# dois numeros e uma operaçao(+,-,*,/)
# a funçao deve retornar o resultado da operaçao, mas precisa
#tratar as seguintes excecoes:
#divisao por zero(zerodivisionerror)
# tipo de dado invalido(value error)

def calculadora():
    try:
        n = input('digite um numero ou x para sair do sistema: ')
        if n.lower() == 'x':
            print('ate breve.')
            return
        n1=input('digite um numero  ou x para sair do sistema: ')
        if n1.lower() == 'x':
            print('ate breve')
        operador = input('informe um operador matematico (+,-,*,/) ou x para sair do sistema: ')
        if operador.lower() == 'x':
            print('ate breve')
            return
        # converter as entradas (inputs) em float
        n = float(n)
        n1 = float(n1)

        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1
        elif operador == '*':
            resultado = n * n1
        elif operador == '/':
            resultado = n / n1
            if n1 == 0:
                raise ZeroDivisionError('nao e possivel dividir por zero.')
            resultado = n / n1
        else:
            print('voce nao escolheu um operador ou escolheu um comando invalido.')
            return
        print(f'operaçao: {n}{operador}{n1}= {resultado}')
    except ValueError:
        print('voce digitou um caracter invalido, digite somente numeros')
    except ZeroDivisionError as zero:
        print(zero)
calculadora()