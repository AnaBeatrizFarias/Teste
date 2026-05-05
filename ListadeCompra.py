compras = []
while True:
    print('selecione uma opção abaixo : \n' \
    '1- adicione um item a lista\n' \
    '2- remova um item da lista \n' \
    '3- limpar a lista \n' \
    '4- mostrar a lista\n' \
    '5-sair')
    opcao = int(input("Digite a opção Desejada: "))
    if opcao == 1:
        produto = str(input("digite o produto: "))
        compras.append(produto)
        print("item adicionado a lista")
    elif opcao == 2:
        produto = str(input("digite o produto"))
        compras.remove(produto)
        print("produto removido da lista ")
    elif opcao == 3:
        compras.clear()
        print("lista limpa")
    elif opcao == 4:
        print(compras) 
    elif opcao == 5:
        print("obrigado por utilizar o programa ")
    else:
        print("opção inválida")