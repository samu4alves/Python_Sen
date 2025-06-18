chaves = ('nome', 'data de nascimento', 'email', 'CPF', 'telefone', 'profissao', 'genero')

pessoas = []

while True:
    pessoa = {}
    menu = input("O que deseja fazer:\n 1- Inserir dados do novo usuario\n 2- Exibir lista de usuario\n 3- Alterar dados de um usuario\n 4- Excluir usuario da lista\n 5- Sair do programa\n")
    match menu:
        case "1":
            for chave in chaves:
                if chave == 'idade':
                    pessoa[chave] = int(input(f"Digite {chave}: "))
                else:
                    pessoa[chave] = input(f"Digite {chave}: ")
            pessoas.append(pessoa)
            
        case "2":
            for pessoa in pessoas:
                print(f"{'-'*40}")
                for chave in chaves:
                    print(f"{chave.capitalize()}: {pessoa.get(chave)}")
                print(f"{'-'*40}")

        case "3":
            for i, pessoa in enumerate(pessoas):
                print(f"{i}: {pessoa.get('nome')}")
            

            try:
                i = int(input("Digite o índice do usuário que deseja alterar: "))
                if i >= 0 and i < len(pessoas):
                    chave = input("Digite a chave que deseja alterar (ex: nome, email, etc): ")
                    if chave in chaves:
                        novo_valor = input(f"Digite o novo valor para '{chave}': ")
                        pessoas[i][chave] = novo_valor
                        print("Dados atualizados com sucesso.")
                    else:
                        print("Chave inválida.")
                else:
                    print("Índice fora do intervalo.")
            except Exception as e:
                print(f"Você precisa digitar um número válido para o índice. {e}")

        case "4":
            for i, pessoa in enumerate(pessoas):
                print(f"{i}: {pessoa.get('nome')}")

            delete = int(input("Digite o dicionario que deseja deletar"))
            if delete in range(len(pessoas)):
                del pessoas[delete]
                print("Pessoa deletada com sucesso")
        
        case "5":
            break