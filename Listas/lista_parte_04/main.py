cidades = [
    'Brasília',
    'Rio de Janeiro',
    'São Paulo',
    'Belo Horizonte',
    'Goiânia',
    'Palmas',
    'São Luis',
    'Belém',
    'Fortaleza',
    'Porto Alegre',
    'Florianópolis',
    'Brasília',
    'Fortaleza',
    'Belo Horizonte',
    'Brasília',
]

# pesquisa do usuário
pesquisa = input('Informe o nome da cidade a ser pesquisada:').title().strip()

if pesquisa in cidades:
    print(f'{pesquisa} encontrada')
else:
    print(f'{pesquisa} não encontrada')

quantidade = cidades.count(pesquisa)
print(f'{pesquisa} foi encontrado {quantidade} vezes na lista')
