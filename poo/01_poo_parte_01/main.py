class Pessoa:
    #atributos
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

# algoritmo principal
if __name__ == "__main__":
    # instancia a classe Pessoa (cria objeto da classe)
    usuario = Pessoa()

# exibe na tela os dados do usuário
print(f'''Nome: {usuario.nome}
Idade: {usuario.idade}
Email: {usuario.email}
Profissão: {usuario.profissao}''')
