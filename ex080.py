lista = []

for valor in range(0,5):
    numeros = int(input(f'Digite um valor: '))
    if valor == 0 or numeros > lista[-1]:
        lista.append(numeros)

    else:
        posicao = 0
        while posicao < len(lista):
            if numeros <= lista[posicao]:
                lista.insert(posicao, numeros)
                break
            posicao += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')