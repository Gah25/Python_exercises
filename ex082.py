"""
# JEITO QUE EU FIZ

lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)

    resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta in 'Nn':
        break
print(f"A lista completa é: {lista}")
print(f"A lista de números pares é: {lista_par}")
print(f"A lista de números ímpares é: {lista_impar}")"""

#################################################################

# JEITO PROFESSOR GUANABARA

num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

for indice, valor in enumerate(num):
        if valor % 2 == 0:
           pares.append(valor)
        elif valor % 2 == 1:
            impares.append(valor)
print('-=' * 30)
print(f"A lista completa é: {num}")
print(f"A lista de números pares é: {pares}")
print(f"A lista de números ímpares é: {impares}")