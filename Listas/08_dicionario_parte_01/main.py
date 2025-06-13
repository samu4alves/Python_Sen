# dicionário
pessoa = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'cpf': "666.666.666.66"
}

'''# exibir os dados do dicionário tradicionalmente
for dado in pessoa:
    print(f'{dado.capitalize()}: {pessoa[dado]}')
'''

# exibir os dados do dicionário com .get
for dado in pessoa:
    print(f'{dado.capitalize()}: {pessoa.get(dado)}')
