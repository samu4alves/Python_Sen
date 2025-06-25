import random
import os

class Pessoa:
        # construtor
    def __init__(self, nome, idade, email, telefone, genero, tipo_sanguineo, doenca_sangue):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.tipo_sanguineo = tipo_sanguineo
        self.doenca_sangue = doenca_sangue

# Listas para aleatoriedade
tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
respostas_doenca = ['s', 'n']

# instancia de dois objetos
usuario1 = Pessoa("", 0, "", 0, "", "", "")
usuario2 = Pessoa("", 0, "", 0, "", "", "")

try:
    # DADOS USUÁRIO 1 - DOADOR
    usuario1.nome = input('Seu nome: ').title().strip()
    usuario1.idade = int(input('Sua idade: '))
    usuario1.email = input('Seu e-mail: ').lower().strip()
    usuario1.telefone = input('Seu telefone: ').strip()
    usuario1.genero = input('Seu gênero: ').capitalize().strip()
    usuario1.tipo_sanguineo = random.choice(tipos_sanguineos)
    usuario1.doenca_sangue = random.choice(respostas_doenca)
    os.system("cls" if os.name == "nt" else "clear")

    # DADOS USUÁRIO 2 - RECEPTOR
    usuario2.nome = input('Seu nome: ').title().strip()
    usuario2.idade = int(input('Sua idade: '))
    usuario2.email = input('Seu e-mail: ').lower().strip()
    usuario2.telefone = input('Seu telefone: ').strip()
    usuario2.genero = input('Seu gênero: ').capitalize().strip()
    usuario2.tipo_sanguineo = random.choice(tipos_sanguineos)

    # DADOS EXIBIDO USUÁRIO 1 - DOADOR
    print(f'''\n--- Dados do DOADOR {usuario1.nome} ---
    Nome: {usuario1.nome}
    Idade: {usuario1.idade}
    E-mail: {usuario1.email}
    Telefone: {usuario1.telefone}
    Gênero: {usuario1.genero}
    Tipo Sanguíneo: {usuario1.tipo_sanguineo}
    Já teve doença transmitida por sangue?: {usuario1.doenca_sangue}
    ''')

    # DADOS EXIBIDO USUÁRIO 2 - RECEPTOR
    print(f'''--- Dados do RECEPTOR {usuario2.nome} ---
    Nome: {usuario2.nome}
    Idade: {usuario2.idade}
    E-mail: {usuario2.email}
    Telefone: {usuario2.telefone}
    Gênero: {usuario2.genero}
    Tipo Sanguíneo: {usuario2.tipo_sanguineo}
    ''')

    # VERIFICAÇÃO SE O USUÁRIO1 PODE DOAR SANGUE PARA USUÁRIO2
    if usuario1.doenca_sangue == 's':
        print("O doador NÃO pode doar sangue porque já teve doença transmitida por sangue.")

    elif (usuario1.tipo_sanguineo == 'O-' or
        (usuario1.tipo_sanguineo == usuario2.tipo_sanguineo)):
        print(f"O doador PODE doar sangue para {usuario2.nome}!")

    else:
        print("O doador NÃO pode doar sangue: tipo sanguíneo incompatível.")

except Exception as e:
    print(f'Não foi possível executar a operação {e}')