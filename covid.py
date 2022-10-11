# Ideia do programa
# Desenhar em uma janela a forma do COVID
# Usando a bliblioteca turtle

import turtle

# Variaveis de direção

frete=0
direita=0

# Criação de Janela
Screen = turtle.Screen()   # Janela
Screen.bgcolor('black')

# Criação de Ponteiro

Ponteiro = turtle.Turtle() # Linhas
Ponteiro.pencolor('green')
Ponteiro.speed(0)
Ponteiro.penup()
Ponteiro.goto(0,200)
Ponteiro.pendown()

# Loop de desenho
while True:
    Ponteiro.forward(frete)
    Ponteiro.right(direita)
    frete+=3
    direita+=1
    if direita==210:
        break
    Ponteiro.hideturtle()

turtle.done()