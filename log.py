from math import log10

def main():
    while True:
        print("cauculadora de escalas logaritmas")
        print("escolha uma opcao: \n" \
        "1-ph\n" \
        "2-richter\n" \
        "3-sair")
        opcao = int(input("escolha sua opcao:"))
        if opcao==1:
            ph()
        elif opcao==2:
            richter()
        elif opcao==3:
            print("saindo")
            break
        else:
            print("digite uma opcao valida ")

def ph():
    print("calculadora de ph")
    print("-----------------")
    while True:
        print("digite 0 para sair do programa")
        h3o= float(input("digite a quantidade de h3o/mol na formula:"))
        if h3o==0:
            print("saindo")
            break

        else:
            ph=-1*log10(h3o)
            if ph> 7 and ph<= 14:
                print(f'o ph da substancia e de ')       

def richter():
    print("escala richter")
    print("--------------")

    while True:
        print("escolha uma opcao: \n" \
        "1- joules para richter \n " \
        "2- richter para joules \n"  \
        "3- sair do programa")
        opcao = int(input("opcao:"))

        if opcao == 1:
            energia = float(input("digite a quantida de energia (joules:)"))
            if energia<=0:
                print("quantidade de energia invalida")
            else:
                magnetude =(log10(energia)- 4.8) / 1.5
                print(f'o terremoto e de (magnetude:.2f) da escala richter')
        elif opcao == 2:
                magnetude = float(input("digite a magnetude de terremoto:"))
                if magnetude <=0:
                    print("magnetude invalida")
                else:
                    joules = 10**(1.5* magnetude *4.8)
                    print(f'o equivalente em joules e de (joules:.2f)')
        elif opcao == 3:
                    print("saindo")
                    break

main()