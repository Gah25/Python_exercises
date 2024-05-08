def calculadora_media():
    lista = []

    while True:
        print("""
PARA SAIR DIGITE [ 0 ]
PARA CONTINUAR DIGITE [ 1 ]""")
        print('=-' * 20)

        opcao = int(input('Qual opcao você deseja? '))
        if opcao == 0:
            break

        if opcao == 1:
            numero = float(input('Digite o valor: '))
            lista.append(numero)

    if lista:
        media =  sum(lista) / len(lista)
        print(f'Números inseridos: {lista}')
        print(f'A média da lista de números é {media:.2f}')
    else:
        print('Nenhum número foi inserido.')

calculadora_media()