# tupla
chaves = ('Nome', 'Idade', 'Email', 'Profissão')
pessoas = [
    {
        chaves[0]: "Alex Machado",
        chaves[1]: 40,
        chaves[2]: "alex@gmail.com",
        chaves[3]: "CEO"
    },
    {
        chaves[0]: "Maria da Silva",
        chaves[1]: 25,
        chaves[2]: "maria@gmail.com",
        chaves[3]: "Assistente Administrativo"
    }
]

# inserindo novo dicionário
pessoa = {}

# inserindo dados no novo dicionário
try:
    for chave in chaves:
        if chave is "Idade":
            pessoa[chave] = int(input('Informe a idade: '))
        else:
            pessoa[chave] = input(f'Informe {chave}:')
    pessoas.append(pessoa)
    print(f'{pessoa.get(chaves[0])} inserida com sucesso')

except Exception as e:
    print(f'Não foi possível cadastrar nova pessoa {e}')
# exibindo a nova lista
finally:
    for pessoa in pessoas:
        print(f'{'-'*40}')
        for chave in pessoa:
            print(f'{chave}: {pessoa.get(chave)}')