import random
import string

def gerador():
    while True:
        print("--gerador de senha--")
        print("gere senha de 6 a 19 caracteres")
        caracteres =string.ascii_letters +string.digits +string.punctuation
        senha=""
        tam=int(input("digite o temanho da senha:"))
        if tam<=5 or tam>=20:
            print("quantidade de caracteres invalida")
        else:
            for i in range(tam):
                senha+= random.choice(caracteres)
        print(f"a senha e : {senha}")

gerador() 