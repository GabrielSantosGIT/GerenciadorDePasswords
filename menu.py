import gerador
import operacoes
import this

this.opcao = -1
this.opcaoA = -1 #Váriavel utilizada no menu atualizar


def menu():
    print("*****************************************")
    print('\nEscolha uma das Opções abaixo: \n\n'         +
          '1. : Inserir nova Senha\n'                     +
          '2. : Consultar Senha\n'                        +
          '3. : Atualizar Senha\n'                        +
          '4. : Exluir Senha\n'                           +
          '5. : Consultar Sistemas Cadastrados\n'         +
          '6. : Gerar Senha Aleatória\n'                  +
          '0. : Sair\n')
    print("*****************************************")
    this.opcao = int(input())

def MenuAtualizar():
    print('\nEscolha qual campo deseja atualizar: \n\n' +
          '1. Atualizar Username\n'                     +
          '2. Atualizar Senha\n'                        +
          '0. Voltar')
    this.opcaoA = int(input())



def operacao():
    print("*****************************************")
    operacoes.Senha_Master()
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('informe o sistema: ')
            sistema = input()
            print('informe o username: ')
            username = input()
            print('informe a senha: ')
            senha = input()
            operacoes.validarSenha(username, senha)
            operacoes.Inserir(sistema, username, senha)
        elif this.opcao == 2:
            print('informe qual sistema você deseja consultar login e Senha:')
            this.sistema = input()
            operacoes.Consultar(this.sistema)
        elif this.opcao == 3:
            while (this.opcaoA != 0):
                MenuAtualizar()
                print("informe o Sistema ou Serviço que deseja atualizar seus dados: ")
                this.sis= str(input())
                if this.opcaoA == 1:
                    print("informe o novo Username: ")
                    this.login = input()
                    operacoes.Atualizar(this.sis, 'username', this.login)
                elif this.opcaoA == 2:

                    print("informe a nova Senha: ")
                    this.password = input()
                    operacoes.Atualizar(this.sis, 'passwd', this.password)

        elif this.opcao == 4:
            print("Informe o Sistema para exclusão dos dados: ")
            this.sis = input()
            operacoes.excluir(this.sis)
        elif this.opcao == 5:
            operacoes.MostrarSistemas()
        elif this.opcao == 6:
            print("Sua Senha Aleatória Gerada é:\n")
            gerador.GerarSenha()
        elif this.opcao == 0:
            print("Saíndo...")
    else:
        print('Opção escolhida não é válida!')
