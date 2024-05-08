print('Gerador de PA')
print('-=' * 10)
primeiro = int(input(f'Primeiro termo: '))
razao = int(input(f'Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais # total = total + mais
    while contador <= total:
        print(f'{termo} → ', end='')
        termo = termo + razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos finalizada')