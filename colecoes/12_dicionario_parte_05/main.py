# lista de dicionários
pessoas =[
    {
        'nome': "Fulano",
        'idade': 30,
        'email': "fulano@gmail.com",
        'profissão': "Gerente de Projetos"
    },    
    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@gmail.com",
        'profissão': "Gerente de Projetos"
    }
]

# exibição dos dados dos dicionários da lista
'''for pessoa in pessoas:
    for chave in pessoa:
        print(f'{chave.capitalize()}: {pessoa.get(chave)}')
    
    print(f'\n{'-'*40}\n')'''

# novo dicionário
nova_pessoa = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "CEO"
}

# nova pessoa na lista
pessoas.append(nova_pessoa)

for pessoa in pessoas:
    for chave in pessoa:
        print(f'{chave.capitalize()}: {pessoa.get(chave)}')

    print(f'\n{'-'*40}\n')