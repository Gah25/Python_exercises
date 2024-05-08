from random import randint
from time import sleep


soma = 0
def sorteio(lista):
    print(f'Sorteando os 5 valores da lista: ', end='')
    for i in range(0, 5):
        i = randint(1, 10)
        print(i, end=' ')
        numeros.append(i)
        sleep(0.2)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos a {soma}')


numeros = []
sorteio(numeros)
somaPar(numeros)






