import os
import modulo

# principal
while True:
    try:
        # menu
        print('''1 - SOMAR
2 - SUBTRAIR
3 - MULTIPLICAR
4 - DIVIDIR
5 -  SAIR DO PROGRAMA''')
        opcao = input('Informe a operação desejada: ').strip()

        os.system("cls" if os.name == "nt" else "clear")
        if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
            x = float(input('Informe o valor de x: '.replace(",", ".")))
            y = float(input('Informe o valor de y: '.replace(",", ".")))
        else:
            ...

        match opcao:
            case "1":
                result = modulo.somar(x, y)
                print(f'O valor da soma é {result}')
                continue

            case "2":
                result = modulo.subtrair(x, y)
                print(f'O valor da subtração é {result}')
                continue

            case "3":
                result = modulo.multiplicar(x, y)
                print(f'O valor da multiplicação é {result}')
                continue

            case "4":
                result = modulo.dividir(x, y)
                print(f'O valor da divisão é {result}')
                continue

            case "5":
                print('Programa encerrado')
                break

            case _:
                print('Operação inválida')

    except Exception as e:
        print(f'Não foi possível calcular {e}')
        continue
