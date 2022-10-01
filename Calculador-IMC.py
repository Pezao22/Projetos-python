#Criar uma calculadora de IMC
# Logica peso dividido pela Altura ao quadrado

print("CALCULADOR DE IMC\n\n")
peso = eval(input("Digite Seu Peso: "))
Altura = eval(input("Digite sua altura: "))

Result = peso / (Altura ** 2)

print('Seu IMC é {:.2f}'.format(Result))