import os

nomes = []
while True:
    print('''MENU
            1 - Inserir um nome em uma lista
            2 - Exibir lista de nomes
            3 - Pesquisar por um nome na lista
            4 - Sair do programa''')
    central =  input('Escolha a opção:').strip()

    os.system("cls") # limpa visualmente no terminal 
    match central:
        case '1':
                pessoa = input('Insira um nome:').lower().strip()
                nomes.append(pessoa)
                print('Nome inserido com sucesso')
        case '2':
            try:
                for pessoa in nomes:
                    print(pessoa)
            except Exception as e:
                 print(f'Não foi possível exibir a lista. {e}')
            finally:
                 continue
        case '3':
                nome_pesquisado = input('Informe o nome a ser pesquisado:').strip().lower()
                os.system("cls")
                if nome_pesquisado in nomes:
                    print(f'{nome_pesquisado} encontrada')
                else:
                    print(f'{nome_pesquisado} não encontrada')
                result = nomes.count(nome_pesquisado)
                print(f'{nome_pesquisado} foi encontrado {result} vezes')
                continue
        case '4':
            parada = input('Deseja continuar? (s/n):')
            if parada == 's':
                continue
            else:
                print('Programa encerrado')
                break
        case _:
              print('Opção errada !')
