import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados
import getpass
import this
import re #módulo que fornece expressões regulares em python

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

#re.search "filtra um padrão".

def Senha_Master():
        print("Cadastre Sua senha Master: ")
        password_master = getpass.getpass("")
        flag = 0
        while True:
            if (len(password_master) < 5):
                 flag = -1
                 break
            elif not re.search("[_@$]", password_master):
                flag = -1
                break
            elif re.search("\s", password_master):
                flag = -1
                break

            else:
                flag = 0
                print("Senha válida! ")
                print("Agora para acessar o sistema digite sua senha master cadastrada:  ")
                senha = getpass.getpass("")


        if flag == -1:
           print("Senha inválida!")
           return Senha_Master()

        print("Agora para acessar o sistema digite sua senha master cadastrada:  ")
        senha = getpass.getpass("")
        if senha != password_master:
            while (password_master != senha):
                print("Senha inválida! Tente outra vez ...")
                password_master = getpass.getpass("Digite sua senha Master: ")
                senha = getpass.getpass("Confirme sua senha Master: ")



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

def MostrarSistemas():
    sql= "select sistema from users;"
    con.execute(sql)

    for sistema in con.fetchall():
        print(sistema)


