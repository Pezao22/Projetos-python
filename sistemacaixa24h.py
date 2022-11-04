###################################
# by Pezao XD
# Sistema bancario simples
###################################

import os
import time
import random

acess = False
extrato = []

def menu():
    print('------------------------------------------------------------------')
    print('                        PÉ BANK SISTEM                            ')
    print('------------------------------------------------------------------')
    print('      1 - Sacar                          2 - Depositar            ')
    print('      3 - Tranferecia                    4 - Extrato              ')
    print('      5 - Saldo                          6 - Sair                 ')
    print('------------------------------------------------------------------\n')

while True:
    if not acess:
        acess = True
        saldo = random.randrange(500,4000)
    os.system('cls') or None
    menu()
    opcao = int(input('\nEscolha a operação: '))

    if opcao > 6 or opcao <= 0:
        print('Escolha uma opcao valido !! ( 1 ao 6 ) ')
        time.sleep(3)
        continue
    
    if opcao == 1:
        sacarValor = int(input('\nQual valor deseja sacar: '))
        if sacarValor <= saldo and sacarValor >= 0:
            if sacarValor > 50000:
                print('\nAceitamos saques de até R$ 50.000')
                time.sleep(3)
                continue
            saldo -= sacarValor
            extrato.append(f'Sacou R$ {sacarValor}')
            print(f'\nVocê sacou R$ {float(sacarValor)} reais')
        elif sacarValor > saldo:
            print('\nSaldo insuficiente')
        else:
            print('\nValor Invalido !!!')

    if opcao == 2:
        depositarValor = int(input('\nQual valor deseja Depositar: '))
        if depositarValor > 0:
            if depositarValor > 50000:
                print('\nAceitamos depositos de até R$ 50.000')
                time.sleep(3)
                continue
            saldo += depositarValor
            extrato.append(f'Depositou R$ {depositarValor}')
            print(f'\nVocê depositou R$ {float(depositarValor)} reais')
        else:
            print('\nValor invelido !!')

    if opcao == 3:
        tranfConta = int(input('\nDigite a conta: '))
        if tranfConta > 0:
            tranfValor = int(input('\nDigite o Valor: '))
            if tranfValor <= saldo and tranfValor > 0:
                extrato.append(f'Transferiu  para conta: {tranfConta} R$ {tranfValor}')
                saldo -= tranfValor
                print('\nTransferencia realizada com sucesso !!!')
            else:
                print('\nValor invalido !')
        else:
            print('\nConta invalida !!')        

    if opcao == 4:
        print('\n')
        if extrato == []:
            print('\nSem Historico')
            time.sleep(3)
            continue
        for linha in extrato:
            print(linha)
        time.sleep(3)


    if opcao == 5:
        print(f'\nSeu saldo: R$ {float(saldo)}')
        time.sleep(3)

    if opcao == 6:
        print('\nATE LOGO ...')
        extrato = None
        opcao = None
        break

    time.sleep(5)
