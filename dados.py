from random import randint

def main(): 
    rolagens =[] 
    validos =[4,6,8,10,12,20,100]
    dado = int(input("digite um dado para rolagem"))
    if dado not in validos:
        print(" dado invalido")
    else:
        quantidade = int(input("digite a quantidade"))
        if quantidade<=0:
            print("quantidade invalida")

        else:
            for i in range(quantidade):
                rolagem=randint(1,dado)
                rolagens.append(rolagem)
            print(f"a soma das rolagens e{sum(rolagens)}")
            print(f"as rolagens foram{rolagens}")