"""
# JEITO QUE EU FIZ -> OBS: ESTÁ CORRETO

import random
import time

numero_sorteado = random.randint(0, 10)
palpite = 0

while numero_sorteado != 0: # Pode usar também while True:
    numero_escolhido = int(input('Escolha um número de 1 a 10: '))
    palpite += 1 # Conta as quantidades de palpite 
    print('PROCESSANDO...')
    time.sleep(2)

    if numero_escolhido != numero_sorteado:
        print('Você errou... Tente novamente')
    else:
        print(f'Você acertou na {palpite}° tentativa. Parabéns')
        break # Sai do loop quando o usuário acerta o número
"""

from random import randint
from time import sleep
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
computador = randint(0, 10)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite: ')) 
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns')