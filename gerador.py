import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados
import string
from random import random, choice  #Random = Gerar número Randômico no Python, choice serve para escolher um item da lista, aleatóriamente.




def GerarSenha():

    valores = string.ascii_letters #Todas as letras Maisculas e Mínusculas
    valores += string.digits #números
    valores += string.punctuation   #caracteres
    tamanho = 15
    senha = ""

    for i in range(tamanho):
        senha += choice(valores)

    print(senha)
