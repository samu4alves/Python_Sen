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

        # métodos

# instancia de dois objetos
usuario1 = Pessoa("", 0, "", 0, "", "", "")
usuario2 = Pessoa("", 0, "", 0, "", "", "")

usuario1.nome = input('Seu nome: ').title().strip()
usuario1.idade = int(input('Sua idade: '))
usuario1.email = input('Seu e-mail: ').lower().strip()
usuario1.telefone = int(input('Seu telefone: '))
usuario1.tipo_sanguineo = input('Tipo sanguíneo: ').strip()
usuario1.doenca_sangue = input('Já teve doença transmitida por sangue? (s/n): ').lower().strip()

usuario2.nome = input('Seu nome: ').title().strip()
usuario2.idade = int(input('Sua idade: '))
usuario2.email = input('Seu e-mail: ').lower().strip()
usuario2.telefone = int(input('Seu telefone: '))
usuario2.tipo_sanguineo = input('Tipo sanguíneo: ').strip()

print(f''''Nome: {usuario1.nome}
Idade: {usuario1.idade}
E-mail: {usuario1.email}
Telefone: {usuario1.telefone}
Tipo Sanguíneo: {usuario1.tipo_sanguineo}
Já teve doença no sangue: {usuario1.doenca_sangue}''')

print(f''''Nome: {usuario2.nome}
Idade: {usuario2.idade}
E-mail: {usuario2.email}
Telefone: {usuario2.telefone}
Tipo Sanguíneo: {usuario2.tipo_sanguineo}''')

