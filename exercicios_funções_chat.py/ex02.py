def impar_par():
    numero1 = int(input('1° Jogador digite um número: '))
    numero2 = int(input('2° Jogador digite um número: '))

    numero = numero1 + numero2
    print(f'A soma dos números escolhido pelos jogadores 1° e 2° é: {numero}')

    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')

impar_par()