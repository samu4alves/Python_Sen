from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    # instancia
    usuario = PessoaFisica(nome="", cpf="", profissao="", email="", telefone="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="")

    print(f'{'-' * 20}Dados do usuário{'-' * 20}\n')

    usuario.nome = input('Informe o nome: ').title().strip()
    usuario.cpf = input('Informe o cpf: ').strip()
    usuario.profissao = input('Informe a profissao: ').strip()
    usuario.email = input('Informe o email: ').lower().strip()
    usuario.telefone = input('Informe o telefone: ').strip()

    limpar()
    print(f'{'-' * 20}Dados da empresa{'-' * 20}\n') 

    empresa.razao_social = input('Informe o razão_social: ').title().strip()
    empresa.nome_fantasia = input('Informe o nome_fantasia: ').strip()
    empresa.cnpj = input('Informe o cnpj: ').strip()
    empresa.email = input('Informe o email: ').lower().strip()
    empresa.telefone = input('Informe o telefone: ').strip()

    limpar()
    print(f'{'-' * 20}Dados do usuário{'-' * 20}\n')
    print(f'''Nome: {usuario.nome}
CPF: {usuario.cpf}
Profissão: {usuario.profissao}
E-mail: {usuario.email}
Telefone: {usuario.telefone}''')
    
    print(f'{'-' * 20}Dados da empresa{'-' * 20}\n')
    print(f'''Razão Social: {empresa.razao_social}
Nome Fantasia: {empresa.nome_fantasia}
CNPJ: {empresa.cnpj}
E-mail: {empresa.email}
Telefone: {empresa.telefone}''')