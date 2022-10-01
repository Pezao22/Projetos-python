# Projeto Cadastro
# Adivinhe o numero

from asyncio.windows_events import NULL
import random  # necessário para utilizar o módulo random
import os


def randomNum():
    num = random.randrange(10)
    while num == 0:
        num = random.randrange(10)
    return num


def cabecalho():
    print('--------------------------\n')
    print('--  ADIVINHE O NUMERO   --\n')
    print('----------0 A 10----------\n')


loop = True

while loop:
    loop = False
    cabecalho()
    maq = randomNum()
    num1 = '11'

    while num1 != maq:
        os.system('cls') or None
        cabecalho()
        num1 = eval(input('Digite sua sorte: '))
        if num1 == maq:
            print('\nParabens Mizeravi !!!\n')
            prox = input('Deseja continuar (s/n): ')
            if prox == 's' or prox == 'S':
                loop = True
            else:
                loop = False
                break




