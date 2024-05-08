from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA            
''')  # print('O computador escolheu {}'.format(itens[computador])) -> apenas para ver o que o computador jogou
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

"""
JEITO QUE EU FIZ

import random
opcao = ['papel', 'pedra', 'tesoura']
computador = random.choice(opcao)

nome = str(input('Jogador, informe o seu nome: '))
minha_escolha = str(input(f'{nome} escolha entre PEDRA[ 0 ], PAPEL[ 1 ] OU TESOURA[ 2 ]: ')).lower()

if minha_escolha == computador:
    print(f'{minha_escolha.upper()} empata com {computador.upper()}... EMPATE')

elif minha_escolha == 'papel' and computador == 'pedra':
    print(f'{minha_escolha.upper()} ganha de {computador.upper()}... O VENCEDOR É: {nome}')

elif minha_escolha == 'papel' and computador == 'tesoura':
    print(f'{minha_escolha.upper()} perde para {computador.upper()}... O VENCEDOR É: COMPUTADOR')

elif minha_escolha == 'pedra' and computador == 'papel':
    print(f'{minha_escolha.upper()} perde para {computador.upper()}... O VENCEDOR É: COMPUTADOR')

elif minha_escolha == 'pedra' and computador == 'tesoura':
    print(f'{minha_escolha.upper()} ganha de {computador.upper()}... O VENCEDOR É: {nome}')

elif minha_escolha == 'tesoura' and computador == 'papel':
    print(f'{minha_escolha.upper()} ganha de {computador.upper()}... O VENCEDOR É: {nome}')

elif minha_escolha == 'tesoura' and computador == 'pedra':
    print(f'{minha_escolha.upper()} perde para {computador.upper()}... O VENCEDOR É: COMPUTADOR')

else:
    print('Escolha uma opção válida...')"""