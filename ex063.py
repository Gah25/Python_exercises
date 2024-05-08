print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
numero = int(input('Quantos termos você quer mostrar? '))

termo1 = 0
termo2 = 1

print('~' * 30)
print(f'{termo1} → {termo2}', end='')

contador = 3
while contador <= numero:
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' → FIM')