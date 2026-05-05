def menu():
    print("Escolha qual tempreatura você quer converter: \n" \
    "1 - Celsius p/ farenheit \n" \
    "2 - Farenheit p/ celsius")
    opcao = int(input("escolha: "))
    temp = float(input("Agora digite a temperatura para converter: "))
    match opcao:
        case 1:
            CpF(temp)
        case 2:
            FpC(temp)
        case _:
            print("Opção inválida")

def CpF(n):
    F = (n * 9/5) + 32
    print(f'{n}ºC são {F}ºF')

def FpC(n):
    C= (n - 32) * 5/9
    print(f"{n}ºF são {C}ºC")

menu()