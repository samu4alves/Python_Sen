import os

def calcular_quadrado(lado):
    return lado ** 2
def calcular_retangulo(largura, altura):
    return largura * altura
def calcular_triangulo(base, altura):
    return (base * altura ) / 2
def calcular_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

while True:    
    print('''1- Calcular área de um quadrado
2- Calcular área de um retângulo
3- Calcular área de um triângulo
4- Calcular área de um trapézio
5- Sair do programa''')
    
    menu = input('Escolha a opção: ').strip()
    os.system('cls' if os.name == 'nt' else 'clear')    
    try: 
        match menu:
            case "1": # Área do quadrado
                lado_quadrado = float(input('Digite um número: '))
                print(f'Área do quadrado: {calcular_quadrado(lado_quadrado)}\n')
                continue
            case "2": # Área do retângulo
                largura = float(input('Digite um número: '))
                altura = float(input('Segundo número: '))
                print(f'Área do retângulo: {calcular_retangulo(largura, altura)}\n')
                continue
            case "3": # Área do triângulo
                base = float(input('Primeiro número: '))
                altura = float(input('Segundo número: '))
                print(f'Área do triângulo: {calcular_triangulo(base, altura)}\n')
                continue              
            case "4": # Área do trapézio
                base_maior = float(input('Primeiro número: '))
                base_menor = float(input('Segundo número: '))
                altura = float(input('Terceiro número: '))
                print(f'Área do trapézio: {calcular_trapezio(base_maior, base_menor, altura)}\n')
                continue              
            case "5": # saida ou não
                parada = input('Deseja sair do programa? (s/n):').strip().lower()
                if parada == 's':
                    print('Programa encerrado')
                    break
                else:
                    continue          
            case _:
                print('Opção inválida')    
    except Exception as e:
        print(f'Não foi possível executar a operação {e}')
        retorno = input('Pressione enter para continuar...')
        continue
