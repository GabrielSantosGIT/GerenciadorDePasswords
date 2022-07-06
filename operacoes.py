import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados
import this
db_connection = conexaoBD.conectar()
con = db_connection.cursor()


def Senha_Master():

    password_master = "123456"
    senha = input("Digite sua senha Master: ")
    if senha != password_master:
        print("Senha inválida! Tente outra vez ...")
        exit()


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
            print('username: {}, passwd: {}'.format(username, passwd))
        print('\n')
    except Exception as erro:
        print(erro)

def Atualizar(sis, sistem, novoDado):
    try:
        sql = "update users set {} = '{}' where sistema = '{}'".format(sistem, novoDado, sis)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))

    except Exception as erro:
        print(erro)



