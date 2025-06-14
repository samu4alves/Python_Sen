import os # módulo para interagir com o sistema operacional

dados = {}

try: # Tentar isso, experimente fazer isso
    dados['nome'] = input('Insira seu nome: ').strip() # Strip, remove espaços indesejados
    dados['cpf'] = input('Insira seu cpf: ').replace(',' , '.') # Replace, troca um caractere por outro
    dados['data'] = input('Insira sua data de nascimento: ')
    dados['email'] = input('Insira seu email: ').strip()
    dados['genero'] = input('Insira seu gênero: ').strip()
    dados['telefone'] = input('Insira seu telefone: ').strip()
    dados['endereco'] = input('Insira seu endereço: ').strip()
    dados['altura'] = float(input('Insira sua altura em metros: ').replace(',' , '.'))
    dados['peso'] = float(input('Insira seu peso em KG: ').replace(',' , '.'))
    dados['sangue'] = input('Insira seu tipo sanguíneo: ').strip()

    os.system("clear") # limpa visualmente a tela no terminal
#                       (Clear, para Linux. Cls, para Windows)

    for pessoa in dados: # Se essa pessoa, estiver dentro dos dados
        print(f"{pessoa.title()}: {dados.get(pessoa)}") # Me mostre esses dados
#                                                       .get, serve para acessar os dados do dicionário

except Exception as e: # AS E, Pega a exceção dê o nome de "e" para que eu possa usá-la como variável
    print(f"Não foi possível rodar programa. {e}.") # Então "e", vai ser o erro exibido na tela