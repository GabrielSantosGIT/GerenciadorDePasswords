import operacoes
import this
this.opcao = -1
this.sistem
this.sis

def menu():
    print("*****************************************")
    print('\nEscolha uma das Opções abaixo: \n\n' +
          '1. : Inserir nova Senha\n'             +
          '2. : Consultar Senha\n'                +
          '3. : Atualizar Senha\n'                +
          '0. : Sair\n')
    print("*****************************************")
    this.opcao = int(input())

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
            operacoes.Inserir(sistema, username, senha)
        elif this.opcao == 2:
            print('informe qual sistema você deseja consultar login e Senha:')
            this.sistema = input()
            operacoes.Consultar(this.sistema)
        elif this.opcao == 3:
            print("informe o Sistema ou Serviço que deseja atualizar: ")
            this.sis = input()
            operacoes.Atualizar(this.sis, 'sistema', this.sistem)
            print("informe o novo Username: ")
            this.login = input()
            operacoes.Atualizar(this.sis, 'username', this.login)
            print("informe a nova Senha: ")
            this.password = input()
            operacoes.Atualizar(this.sis, 'passwd', this.password)
        else:
            print('Opção escolhida não é válida!')