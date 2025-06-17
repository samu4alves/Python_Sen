chaves = ('Nome', 'Data de Nascimento', 'Email', 'Cpf', 'Telefone', 'Profissão', 'Gênero')

pessoas = []

# inserindo pessoa
while True:
    nova_pessoa = {}
    menu = input('Escolha uma opção:')
    match menu:
        case '1':
            try:
                for chave in chaves:
                    if chave == "Idade":
                        nova_pessoa[chave] = int(input('Informe a idade: '))
                    else:
                        nova_pessoa[chave] = input(f'Informe {chave}:')
                pessoas.append(nova_pessoa)
                print(f'{nova_pessoa.get(chaves[0])} inserida com sucesso')

            except Exception as e:
                print(f'Não foi possível cadastrar nova pessoa {e}')
            # exibindo a nova lista
        case '2':
            for nova_pessoa in pessoas:
                print(f'{'-'*40}')
                for chave in chaves:
                    print(f'{chave}: {nova_pessoa.get(chave)}')
        case '3':
            for i, nova_pessoa in enumerate(pessoas):
                    print(f'Posição{i}: {nova_pessoa.get('Nome')}')
            
            i = int(input('Informe o número do índice a ser alterado: '))
            if i >= 0 and i < len(pessoas):
                    chave = input('Chave que deseja alterar? Nome, Email...')
                    if chave in chaves:
                         novo_valor = input(f'Novo valor para chave')
                         pessoas[i][chaves]
                    print('Pessoa alterada com sucesso\n')
            else:
                print('Valor do índice inválido')
            for i, nova_pessoa in enumerate(pessoas):
                    print(f'Posição{i}: {nova_pessoa.get('Nome')}')
