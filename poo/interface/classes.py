from abc import ABC 
from abc import abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, email, endereco, telefone):
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
        #super().__init__()
    @abstractmethod
    def apresentar():
        ...
    @abstractmethod
    def exibir_dados(self):
        print(f"email: {self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        ...

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, profissao, email, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao= profissao
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
        super().__init__(email=email, endereco=endereco, telefone=telefone)

    def apresentar(self):
        return  f"Meu nome {self.nome}"

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()


class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj,email, endereco, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, endereco=endereco,telefone=telefone)
       
    def apresentar(self):
        return  f"Somos a empresa {self.nome_fantasia}"
    #super().apresentar()
    def exibir_dados(self):
        print(f"Razao Social: {self.razao_social}")
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()
    #super().exibir_dados()