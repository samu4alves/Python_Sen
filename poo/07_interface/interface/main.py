import classes
import os

if __name__ == "__main__":
   usuario = classes.PessoaFisica("","","","","","")
   empresa = classes.PessoaJuridica("","","","","","")

   while True:
        print('''1 - inserir dados do usuario
2 - inserir dados da empresa
3 - Exibir dados
4- Sair do programa''')
        opcao = input("informe a opção desejada:").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                try:
                    usuario.nome = input("informe o nome do usuario: ").title().strip()
                    usuario.cpf = input("informe o cpf do usuario: ").title().strip()
                    usuario.profissao = input("informe a profissao do usuario: ").title().strip()
                    usuario.email = input("informe o email do usuario: ").title().strip()
                    usuario.endereco = input("informe o endereço do usuario: ").title().strip()
                    usuario.telefone = input("informe o telefone do usuario: ").title().strip()

                    os.system("cls" if os.name == "nt" else "clear")

                except Exception as e:
                    print(f"não foi possivel inserir os dados")
                finally:
                    continue
                
            case "2":
                try:
                    empresa.razao_social = input("informe a razao social: ").strip().title()
                    empresa.nome_fantasia = input("informe o nome fantasia: ").strip().title()
                    usuario.cnpj = input("informe o CNPJ: ").strip()
                    usuario.email = input("informe o email da empresa: ").lower().strip()
                    usuario.endereco = input("informe o endereco da empresa: ").title().strip()
                    usuario.telefone = input("informe o telefone da empresa: ").strip()
                except Exception as e:
                    print(f"não foi possível {e}")
                finally:
                    continue

            case "3":
                try:
                    opcao = input("Digite:\n 1- para exibir dados do usuario \nou\n 2- para exibir dados da empresa.\n")
                    if opcao == "1":
                        usuario.exibir_dados()
                    elif opcao == "2":
                        empresa.exibir_dados()
                    else:
                        print("Opção invalida")

                except Exception as e:
                    print(f"Não foi possivel exibir dados. {e}")

            case "4":
                print("Encerrando o programa...")
                break

            case _:
                print("opção inválida")
                continue