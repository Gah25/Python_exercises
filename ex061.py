print('Gerador de PA')
print('-=' * 10)
primeiro = int(input(f'Primeiro termo: '))
razao = int(input(f'Razão da PA: '))
termo = primeiro
contador = 0

while contador <= 10:
    print(f'{termo} → ', end='')
    termo = termo + razao # termo += razao
    contador += 1
print("ACABOU")
    