import equacoes
import os

if __name__ == "__main__":
    while True:
        try:
            print('''1 - Equação Primeiro Grau
    2 - Equação Segundo Grau
    3 - Sair do Programa''')
            menu = input('Digite a opção: ')
            os.system("cls" if os.name == "nt" else "clear")
            match menu:
                case "1":
                    a = float(input('Digite um número: ').replace(",", "."))
                    b = float(input('Digite um número: ').replace(",", "."))
                    result = equacoes.equacao_1_grau(a, b)
                    print(f'{a}x + {b} = 0')
                    print(f'x = {result}')
                    continue
                
                case "2":
                    a = float(input('Digite um número: ').replace(",", "."))
                    b = float(input('Digite um número: ').replace(",", "."))
                    c = float(input('Digite um número: ').replace(",", "."))                
                    os.system("cls" if os.name == "nt" else "clear")
                    result = equacoes.equacao_2_grau(a, b, c)
                    for x in result:
                        print(x)
                    continue

                case "3":
                    print('Programa encerrado')
                    break

                case _:
                    print('Opção inválida')
                    continue
        except Exception as e:
            print('Não foi possível executar a operação')