import os # módulo para interagir com o sistema operacional

nomes = []
while True:
    print('''           MENU
            1 - Inserir um nome em uma lista
            2 - Exibir lista de nomes
            3 - Pesquisar por um nome na lista
            4 - Alterar um nome na lista
            5 - Excluir um nome na lista
            6 - Sair do programa''')
    central =  input('Escolha a opção:').strip()

    os.system("clear")
    
    match central:
        case '1':
                nome_inserido = input('Insira um nome:').lower().strip() 
                nomes.append(nome_inserido) 
                print('Nome inserido com sucesso')

        case '2': 
            try: 
                for nome_inserido in nomes:
                    print(nome_inserido)
            except Exception as e: 
                 print(f'Não foi possível exibir a lista. {e}')
            finally:
                 continue

        case '3':
                nome_pesquisado = input('Informe o nome a ser pesquisado:').strip().lower()
                os.system("clear")
                if nome_pesquisado in nomes:
                    print(f'{nome_pesquisado} pessoa encontrada')
                else:
                    print(f'{nome_pesquisado} pessoa não encontrada')
                result = nomes.count(nome_pesquisado)
                print(f'{nome_pesquisado} foi encontrado {result} vezes')
                continue
# exibe a lista de posições dos nomes para fazer a alteração
        case '4':
                for nome_inserido in range(len(nomes)):
                    print(f'Posição {nome_inserido}: {nomes[nome_inserido]}')
# usuário informa a posição do nome que deseja alterar
                try:
                    posicao_nome = int(input('Informe o número do posição a ser alterado: '))
                    os.system("clear")
                    if posicao_nome >= 0 and posicao_nome < len(nomes):
                        print(f'Nome encontrado {nomes[posicao_nome]}')
                        nomes[posicao_nome] = input('Informe o nome da nova pessoa: ')
                        os.system("clear")
                        print('Nome alterado com sucesso\n')
                    else:
                        print('Valor do posição inválido')
                except Exception as e:
                    print(f'Não foi possível executar a operação. {e}')
                finally:
                    print('\nNova lista:\n')
                    for posicao_nome in range(len(nomes)):
                        print(f'Posição {posicao_nome}: {nomes[posicao_nome]}')
# exibe a lista de posições dos nomes para fazer a exclusão        
        case '5':
                for nome_antes_del in range(len(nomes)):
                    print(f"Posição {nome_antes_del}: {nomes[nome_antes_del]}.")
# usuário informa a posição do nome que deseja excluir
                try:
                    exclusao_nome = int(input("Informe a posição que deseja excluir: "))
                    os.system("clear")
                    if exclusao_nome >= 0 and exclusao_nome < len(nomes):
                        print(f"Nome a ser excluído: {nomes[exclusao_nome]}")
                        confirma = input(f"Deseja excluir {nomes[exclusao_nome]}? (s/n)").lower().strip()
                        os.system("clear")
                        match confirma:
                            case "s":
                                nome_excluido = nomes[exclusao_nome]
                                del(nomes[exclusao_nome])
                                print(f"Nome {nome_excluido} excluído com sucesso.")
                            case "n":
                                print(f"{nomes[exclusao_nome]} não será excluído.")
                            case _:
                                print("Opção inválida.")
                    else:
                        print("Posição inválido.")
                except Exception as e:
                    print(f"Não foi possível excluir item. {e}.")
                finally:
                    print(f"Nova lista:\n")
                    for novo_nome in range(len(nomes)):
                        print(f"Posição {novo_nome}: {nomes[novo_nome]}.")
# encerramento ou continuação do programa
        case '6':
            parada = input('Deseja continuar? (s/n):')
            if parada == 's':
                continue
            else:
                print('Programa encerrado')
                break
        case _:
              print('Opção errada !')
