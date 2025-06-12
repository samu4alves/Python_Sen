# declaração de lista
carrinho = []

while True:
    item = input('Informe o item:').capitalize().strip()
    carrinho.append(item)
    print('Item inserido com sucesso !')
    confirmar = input('Desja inserir outro item? (s/n)').lower().strip()
    match confirmar:
        case 's':
            continue
        case 'n':
            break
        case _:
            print('Opção inválida')
            continue
# Ordena em ordem alfabética
carrinho.sort()
# exibe a lista
for item in carrinho:
    print(item)
