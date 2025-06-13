estados = (
    "Distrito Federal",
    "Goiás",
    "Minas Gerais",
    "Tocantins",
    "Rio de Janeiro",
    "Ceará"
)

# listar a tupla
for estado in estados:
    print(estado)

# pesquisar estados

estado_pesquisa = input('Informe o estado que deseja pesquisar: ').title().strip()
qtde_estados = estados.count(estado_pesquisa)

print(f'{estado_pesquisa} foi encontrado {qtde_estados} vezes na tupla')
