import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados


db_connection = conexaoBD.conectar()
con = db_connection.cursor()


def Senha_Master():

        password_master = input("Digite sua senha Master:" )
        senha = input("Confirme sua senha Master: " )

        if senha != password_master:
           while(password_master != senha):
                print("Senha inválida! Tente outra vez ...")
                password_master = input("Digite sua senha Master: ")
                senha = input("Confirme sua senha Master: ")





def Inserir(sistema, username, passwd):
     try:
         sql = "insert into users(sistema, username, passwd) values('{}', '{}', '{}')".format(sistema, username, passwd)
         con.execute(sql)
         db_connection.commit() #Inserção de dados no BD
         print("{} Inserido com Sucesso".format(con.rowcount))


     except Exception as erro:
         return erro


def Consultar(sistem):
    try:
        sql = "select * from users where sistema = '{}'".format(sistem)
        con.execute(sql)


        for(sistema, username, passwd) in con:
            print('username: {}, pass0wd: {}'.format(username, passwd))
        print('\n')
    except Exception as erro:
        print(erro)

def Atualizar(sis,campo, novoDado):
    try:
        sql = "update users set {} = '{}' where sistema = '{}'".format(campo, novoDado, sis)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))

    except Exception as erro:
        print(erro)

def validarSenha(username, senha):

    while (username == senha):
        print("Sua senha deve ser diferente do username: ")
        print('informe a senha: ')
        senha = input()


def excluir(sis):
    try:
        sql = "delete from users where sistema = '{}'".format(sis)
        con.execute(sql)
        db_connection.commit()
        print('{} Dados Excluídos!'.format(con.rowcount))
    except Execption as erro:
         print(erro)