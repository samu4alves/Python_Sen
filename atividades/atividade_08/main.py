'''
#todo - atividade crie um programa onde o usuario possa escolher as seguintes operações:
-calcular área de um quadrado
-calcular área de um retângulo
-calcular área de um triângulo
-calcular área de um trapézio
-sair do programa
#note - o usuario deverá escolher a operação em um menu
#note - o programa deverá ser feito com funções
'''

import math as m
import os

def calcular_quadrado():
    return f'{m.sqrt}'

def calcular_retangulo(largura, altura):
    return largura * altura

def calcular_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = m.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calcular_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

while True:
    print('''1- Calcular área de um quadrado
2- Calcular área de um retângulo
3- Calcular área de um triângulo
4- Calcular área de um trapézio
5- Sair do programa''')
    
    menu = int(input('Escolha a opção: '))
    try: 
        if menu == int:
            match menu:
                case "1": # raiz quadrada
                    quadrado = int(input('Digite um número: '))
                    print(f'Raiz quadrada: {calcular_quadrado()}')
                    continue

                case "2": # retângulo
                    largura = int(input('Digite um número: '))
                    altura = int(input('Digite um número: '))
                    print(f'Retângulo: {calcular_retangulo}')
                
                case "3": # triângulo
                    a = int(input('Primeiro número'))
                    b = int(input('Segundo número'))
                    c = int(input('Terceiro número'))
                    print(f'Triângulo: {calcular_triangulo}')
                
                case "4": # trapézio
                    trapezio
    except Exception as e:
        print(f'Não foi possível executar a operção {e}')
        continue