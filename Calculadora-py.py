# Operadores logicos PYTHON

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potencia
# // Divisçao Inteira
# % Resto da divisçao

# CALCULADORA SIMPLES EM PYTHON 3
from os import cls

def cabecalho():
    print('--------------------------------------\n')
    print('CALCULADORA SIMPLES\n')
    print('--------------------------------------\n')

    print('1 - Adição\n')
    print('2 - Subtração\n')
    print('3 - Multiplicação\n')
    print('4 - Divisão\n')
    print('5 - Potenciação\n')
    print('6 - Divisçao Inteira\n')
    print('7 - Resto da divisçao\n\n')

def calc():

    opcao = int(input('Escolha uma opcao: '))

    n1 = int(input('\nEntre um numero: '))
    n2 = int(input('\nEntre com outro numero: '))

    if opcao == 1:
        t = n1 + n2
        g = 'Adição'
    elif opcao == 2:
        t = n1 - n2
        g = 'Subtração'
    elif opcao == 3:
        t = n1 * n2
        g = 'Multiplicação'
    elif opcao == 4:
        t = n1 / n2
        g = 'Divisçao'
    elif opcao == 5:
        t = n1 ** n2
        g = 'Potenciação'
    elif opcao == 6:
        t = n1 // n2
        g = 'Divisao inteira'
    elif opcao == 7:
        t = n1 % n2
        g = 'Resto inteiro'
    return t,g

cabecalho()

total,tipo = calc()

print('\nO resultado da {} é {}'.format(tipo,total))
