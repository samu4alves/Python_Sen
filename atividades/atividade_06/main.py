import os

usuario = {}

while True:
    print('''           MENU
            1 - Cadastar um nome em uma lista
            2 - Exibir lista de nomes
            3 - Alterar um nome na lista
            4 - Excluir um nome na lista
            5 - Sair do programa''')

    menu = input('Escolha a opção:').strip()
    os.system('cls')

    match menu:
        case "1":
            try:
                dado = input('Informe o dado que deseja inserir: ')
                usuario[dado] = input('Informe o valor da chave: ')
                os.system('cls')
                print('Dado cadastrado !')
            except Exception as e:
                print(f'Não foi possível cadastrar o dado {e}')
            finally:
                continue
        
        case "2":
                for dado in usuario:
                    print(f"{dado.capitalize()}: {usuario.get(dado)}")
                continue

        case "3":
              for dado in range(len(usuario)):
                   print(f'Posição:{dado} {usuario['nome']}')
              try:
                   dado = int(input('Informe o número da posição a ser alterada:'))
                   if dado >= 0 and dado < len(usuario):
                        print(f'Nome encontrado {usuario[dado]}')
                        usuario[dado] = input('Informe o nome da nova pessoa: ')
                        print('Nome alterado com sucesso\n')
                   else:
                        print('Valor da posição errada')
              except Exception as e:
                   print(f'Não foi possível alterar {e}')
              finally:
                    print('\nNovos nomes:\n')
                    for dado in range(len(usuario)):
                        print(f'{usuario['nome']}')
