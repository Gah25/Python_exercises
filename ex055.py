
# JEITO QUE EU FIZ

contador = 0
lista_peso = []
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p}° pessoa? '))
    lista_peso.append(peso)
    contador += 1
    maior_peso = max(lista_peso)
    menor_peso = min(lista_peso)
print(f'O maior peso é {maior_peso}kg')
print(f'O menor peso é {menor_peso}kg')




"""
JEITO QUE O PROFESSOR GUANABARA FEZ

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p}° pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}kg".format(maior))
print("O menor peso lido foi de {}kg".format(menor))"""