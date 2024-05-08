# JEITO QUE EU FIZ

from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

numero_de_vitorias = 0

while True:
    
    computador = randint(0, 11)
    par_ou_impar = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
    numero = int(input('Digite um valor: '))
    par_impar = (numero + computador) %  2 == 0
    impar_par = (numero + computador) %  2 == 1
    soma = numero + computador

    if par_impar:
        print('-' * 60)
        print(f'Você jogou {numero} e o computador {computador}. Total de {soma} DEU PAR')
        print('-' * 60)
    
    else:
        print('-' * 60)
        print(f'Você jogou {numero} e o computador {computador}. Total de {soma} DEU IMPAR')
        print('-' * 60)

    if par_ou_impar == 'P':
        if par_impar:
            print('-' * 60)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-' * 60)
            numero_de_vitorias += 1
        else:
            print('-' * 60)
            print('Você PERDEU!')
            print('-' * 60)
            break
    elif par_ou_impar == 'I':
        if impar_par:
            print('-' * 60)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-' * 60)
            numero_de_vitorias += 1
        else:
            print('-' * 60)
            print('Você PERDEU!')
            print('-' * 60)
            break

print(f'GAME OVER! Você venceu {numero_de_vitorias} vezes')

########################################################################

"""
# JEITO PROFESSOR GUANABARA

from random import randint

vitoria = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ' ) 
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    
    print('Vamos jogar novamente... ')
print(f'GAME OVER! Você venceu {vitoria} vezes')"""