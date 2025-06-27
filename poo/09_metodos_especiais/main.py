from classes import Pessoa
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = Pessoa(nome="", profissao="", idade="")

    while True:
        print('''1- Inserir dados e exibir
2- Sair do programa''')
        
        opcao = input('Escolha a opção: ').strip()
        limpar()
        match opcao:
            case "1":
                try:
                    usuario.nome = input('Informe o nome: ').strip().title()
                    usuario.idade = int(input('Informe a idade: '))
                    usuario.profissao = input('Informe a profissão: ').strip()
                    
                    print(f'''Nome: {usuario.nome}
                Profissão: {usuario.profissao}
            Idade: {usuario.idade}''')
                    
                    limpar()
                    print(usuario)
            #        print(f'Idade de {usuario.nome}: {len(usuario)} anos')
                    continue
            #        del(usuario)
                except Exception as e:
                    print(f'Não foi possível executar a operação {e}')
            #        del(usuario)
                    break
            case "2":
                break

            case _:
                print('Opção inválida')
                continue