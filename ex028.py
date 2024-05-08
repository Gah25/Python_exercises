import random
import time
numero_sorteado = random.randint(0, 5) # Sorteia um número de 0 a 5

numero_escolhido = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
time.sleep(2)

if numero_escolhido == numero_sorteado:
    print(f'Você ganhou! O número escolhido foi {numero_sorteado}')
else:
    print(f'Você perdeu =(... Seu número escolhido foi {numero_escolhido} e o número que saiu foi {numero_sorteado}')
