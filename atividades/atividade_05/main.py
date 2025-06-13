dados = {

}

dados['nome'] = input('Insira seu nome: ').strip()
dados['cpf'] = input('Insira seu cpf: ').replace(',' , '.')
dados['data'] = input('Insira sua data de nascimento: ')
dados['email'] = input('Insira seu email: ').strip()
dados['genero'] = input('Insira seu gênero: ').strip()
dados['telefone'] = input('Insira seu telefone: ').strip()
dados['endereco'] = input('Insira seu endereço: ').strip()
dados['altura'] = float(input('Insira sua altura em metros: ').replace(',' , '.'))
dados['peso'] = float(input('Insira seu peso em KG: ').replace(',' , '.'))
dados['sangue'] = input('Insira seu tipo sanguíneo: ').strip()

try:
    print(f'''Nome: {dados['nome']}
    Cpf: {dados["cpf"]}
    Data: {dados["data"]}
    Email: {dados["email"]}
    Gênero: {dados["genero"]}
    Telefone: {dados["telefone"]}
    Endereço: {dados["endereco"]}
    Altura: {dados["altura"]}
    Peso: {dados["peso"]}
    Sangue: {dados["sangue"]}''')
except Exception as e:
    print(f'Não foi possível executar {e}')