import os

usuario = {}
while True:
    print("1 - Cadastrar nova chave")
    print("2 - Exibir dados do usuário")
    print("3 - Alterar valor da chave")
    print("4 - Excluir chave")
    print("5 - Sair do programa")
    menu = input("Informe a opção desejada: ")

    os.system("clear") # No windows, cls
    match menu:
        case "1":
            chave = input("Informe a chave que deseja inserir:").lower().strip()
            usuario[chave] = input("Informe o valor da chave: ")

            os.system("clear") # No windows, cls
            print("Chave cadastrada com sucesso!")
            continue

        case "2":
            for chave in usuario: 
                print(f"{chave.capitalize()}: {usuario.get(chave)}.") 

            print("\n")
            continue
        case "3":
            chave = input("Informe a chave que deseja alterar: ").lower().strip()

            if chave in usuario:
                usuario[chave] = input("Informe o valor da chave: ")
                os.system("clear") # No windows, cls
                print("Valor da chave alterado com sucesso!")
            else:
                os.system("clear") # No windows, cls
                print("Chave não encontrada.")
            
            continue
        case "4":
            chave = input("Informe a chave que deseja excluir: ").lower().strip()
            confirmacao = input(f"Tem certeza de que deseja excluir {chave}? (s/n)").lower().strip()
            os.system("clear") # No windows, cls
            
            if confirmacao is "s":
                del usuario[chave]
                print("Chave excluída com sucesso!")
            else:
                print("Chave não foi excluída.")
            
            continue
        case "5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue