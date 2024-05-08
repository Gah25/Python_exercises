"""
# JEITO QUE EU TENTEI FAZER

pessoa = list()
dados = list()
soma = maior_peso = menor_peso = peso = 0
indice_maior_peso = -1
indice_menor_peso = -1

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    dados.append(int(input('Peso: ')))
    pessoa.append(dados[:])
    dados.clear()

    resposta = (str(input('Quer continuar? [S/N] '))).strip().upper()
    soma += 1
    if resposta in 'Nn':
        break


for indice, contador in enumerate(pessoa):
    if contador[2] > maior_peso:
        maior_peso = contador[2]
        indice_maior_peso = indice
    
    if contador[2] < menor_peso:
        menor_peso = contador[2]
        indice_menor_peso = indice

print(f'Ao todo, você cadastrou {soma} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {pessoa[indice_maior_peso][0]} ')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {pessoa[indice_menor_peso][0]} ')
"""

########################################################################################

# PROFESSOR GUANABARA

temporaria = []
principal = []
maior = menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    
    if len(principal) == 0:
        maior = menor = temporaria[1]

    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()
    resposta = (str(input('Quer continuar? [S/N] ')))
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()